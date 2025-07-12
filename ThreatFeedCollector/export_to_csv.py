import json
import csv

# Load the final cleaned & deduplicated data
with open("final_feeds.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Define CSV output file
csv_file = "feeds.csv"

# Save to CSV
with open(csv_file, "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "link", "published", "summary"])
    writer.writeheader()
    writer.writerows(data)

print(f"✅ Exported {len(data)} entries to feeds.csv")
