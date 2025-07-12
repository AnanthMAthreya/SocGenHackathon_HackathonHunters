import feedparser
import json

# Read feed URLs from feeds.txt
with open("feeds.txt", "r") as f:
    feed_urls = [line.strip() for line in f if line.strip()]

all_items = []

for url in feed_urls:
    print(f"Fetching from: {url}")
    feed = feedparser.parse(url)
    
    for entry in feed.entries:
        item = {
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "published": entry.get("published", ""),
            "summary": entry.get("summary", "")
        }
        all_items.append(item)

# Save to output.json
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(all_items, f, indent=4)

print(f"✅ Collected {len(all_items)} feed items. Saved to output.json")
