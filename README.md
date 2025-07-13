# SocGenHackathon_HackathonHunters
👨‍💻 Author
- Ananth M Athreya [GitHub](https://github.com/AnanthMAthreya)
- Varun Banda [Github](https://github.com/Varun7sept)
- Abhay GK [Linkedin](https://www.linkedin.com/in/abhay-gk/)
- Parth Shukla

🔐 Threat Feed Collector – SocGen Hackathon
This is the Feed Collector module for an AI-powered Threat Intelligence Feed Aggregator. It is responsible for fetching, cleaning, and organizing cyber threat intelligence from various open-source RSS/Atom feeds.

📌 What It Does
✅ Collects cyber threat feeds from 45+ sources
✅ Cleans and normalizes titles, links, summaries, and publish dates
✅ Removes duplicate entries based on links
✅ Stores cleaned data in both JSON and CSV formats for downstream processing
📁 Project Structure
ThreatFeedCollector/
├── feeds.txt               # List of RSS/Atom URLs (1 per line)
├── main.py                 # Script to fetch raw feed data from sources
├── clean_feeds.py          # Cleans and normalizes raw data
├── final_feeds.json        # Cleaned and deduplicated JSON output
├── feeds.csv               # Final CSV version for dashboard integration
├── export_to_csv.py        # Converts JSON to structured CSV
🚀 How to Run
1. Install Dependencies
Make sure you have Python 3.x installed.

Install the required library:

pip install feedparser
2. Run the Fetch Script
python main.py
This will fetch and store raw RSS/Atom feed data into output.json.

3. Clean and Deduplicate
python clean_feeds.py
This will:

Clean entries (remove whitespace, check for missing fields)
Remove duplicates based on feed links
Save to final_feeds.json
4. Export to CSV (for dashboards, ML, etc.)
python export_to_csv.py
This will generate feeds.csv — a structured, readable dataset.

📦 Output Example (CSV)
Title	Link	Published	Summary
"New phishing malware targeting banks"	https://example.com/article	2024-01-12	A detailed breakdown of a new phishing campaign...
🧠 Next Modules (In Progress)
IOC Extractor: Extract IPs, URLs, and hashes using regex/HTML parsers
LLM Summarizer: Use local LLMs (via Ollama) to generate summaries
Interactive Dashboard: Visualize feeds and IOCs using Gradio
🤝 Contributing
If you're part of the team:

Make sure to pull latest before pushing
Commit meaningful messages
Keep scripts modular and well-commented


📜 License
MIT License – feel free to use and adapt.
