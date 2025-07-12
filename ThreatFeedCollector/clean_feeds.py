import json

# Step 1: Load raw feed data
with open("output.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

normalized_data = []

# Step 2: Clean and normalize each entry
for item in raw_data:
    normalized_item = {
        "title": item.get("title", "").strip(),
        "link": item.get("link", "").strip(),
        "published": item.get("published", "").strip(),
        "summary": item.get("summary", "").strip()
    }

    # Keep only entries with title and link
    if normalized_item["title"] and normalized_item["link"]:
        normalized_data.append(normalized_item)

print(f"✅ Cleaned {len(normalized_data)} entries")

# Step 3: Remove duplicate entries by 'link'
unique_data = []
seen_links = set()

for entry in normalized_data:
    if entry["link"] not in seen_links:
        seen_links.add(entry["link"])
        unique_data.append(entry)

# Step 4: Save final cleaned + deduplicated data
with open("final_feeds.json", "w", encoding="utf-8") as f:
    json.dump(unique_data, f, indent=4)

print(f"✅ Final feed count after de-duplication: {len(unique_data)}")
print("📁 Saved to final_feeds.json")
