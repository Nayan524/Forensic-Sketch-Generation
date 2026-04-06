# File: preprocess_llama3_enhanced_dataset.py

import os
import json
import requests
from datasets import Dataset
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def enhance_caption_ollama(prompt: str, model="llama3") -> str:
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": f"Describe this face for a forensic sketch. Avoid blanks or templates:\n{prompt}",
                "stream": False
            },
            timeout=600
        )
        return response.json()["response"].strip()
    except Exception as e:
        print(f"[ERROR] Failed to enhance: {prompt[:40]}... -> {e}")
        return prompt  # fallback

def validate_and_enhance(entry, image_dir, model="llama3"):
    try:
        image_path = os.path.join(image_dir, os.path.basename(entry["file_name"]))
        if os.path.exists(image_path):
            enhanced = enhance_caption_ollama(entry["text"], model)
            return {"image_path": image_path, "caption": enhanced}
    except Exception:
        return None

def preprocess_dataset(jsonl_path, image_dir, output_jsonl, max_samples=5000, num_workers=10, model="llama3"):
    # Load original entries
    with open(jsonl_path, "r") as f:
        all_entries = [json.loads(line.strip()) for line in f]

    # Load already processed captions (if resuming)
    processed = set()
    if os.path.exists(output_jsonl):
        with open(output_jsonl, "r") as f:
            for line in f:
                try:
                    processed.add(json.loads(line.strip())["file_name"])
                except:
                    continue

    print(f"🔁 Resuming — {len(processed)} already processed.")

    entries = [e for e in all_entries if e["file_name"] not in processed]

    if not entries:
        print("✅ All entries are already processed.")
        return

    print(f"🚀 Enhancing {min(len(entries), max_samples)} new captions...")

    count = 0
    with ThreadPoolExecutor(max_workers=num_workers) as executor, open(output_jsonl, "a") as out:
        futures = [executor.submit(validate_and_enhance, e, image_dir, model) for e in entries[:max_samples * 2]]
        for future in tqdm(as_completed(futures), total=len(futures), desc="Enhancing"):
            result = future.result()
            if result:
                out.write(json.dumps(result) + "\n")
                out.flush()
                count += 1
                if count >= max_samples:
                    break

    print(f"✅ Saved {count} new captions to: {output_jsonl}")
