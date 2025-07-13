import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
LLM_MODEL = "llama2"  # Change to your local model name

def summarize(text):
    payload = {
        "model": LLM_MODEL,
        "prompt": f"Summarize this threat intel report for a security analyst:\n{text}"
    }
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "")

def process_summaries():
    with open("data/feeds.json") as f:
        feeds = json.load(f)
    summaries = []
    for entry in feeds:
        summary = summarize(entry["summary"])
        summaries.append({
            "title": entry["title"],
            "link": entry["link"],
            "published": entry["published"],
            "summary": summary
        })
    with open("data/summaries.json", "w") as f:
        json.dump(summaries, f, indent=2)
    return summaries

if __name__ == "__main__":
    process_summaries()
