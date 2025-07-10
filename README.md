# 🔍 Smart Lead Scraper – Caprae Capital AI Challenge

This project was developed as part of Caprae Capital’s AI-Readiness Pre-Screening Challenge. The goal was to build a practical tool, within a 5-hour window, that replicates or improves key features of the lead generation platform [SaaSquatchLeads](https://www.saasquatchleads.com).

---

## 🚀 Project Overview

**Smart Lead Scraper** is a lightweight Python tool that scrapes business websites for:

- Contact Emails
- Social Media Links (LinkedIn, Twitter, Facebook)
- Website URL

It saves the output to a clean, appendable CSV file (`leads_output.csv`), making it easy to run across multiple websites and build a lead list.

---

## 💡 Why This Tool?

Lead generation teams often struggle with:
- Manually collecting contact info from websites
- Finding social links for outreach
- Organizing data quickly without complex tools

This script automates that process in a simple, command-line format using HTML parsing — fast, reliable, and easy to modify.

---

## 🧰 Tech Stack

- Python 3
- `requests` – for fetching website content
- `BeautifulSoup` – for HTML parsing
- `re` – to extract emails
- `pandas` – to store CSV data

---

## ⚙️ How to Use

1. **Install dependencies:**

```bash
pip install requests beautifulsoup4 pandas
```

2. **Run the script:**

    ```bash
    python lead_scraper.py
    ```

3. **Enter a website URL** when prompted  
   _(e.g., `https://stripe.com`)_

4. **Output is saved to** `leads_output.csv`  
   - The file will **append** new entries automatically  
   - No data is overwritten, so you can build your lead list over time

## 📁 Sample Output

| Website | Email(s) | LinkedIn | Twitter | Facebook |
|---------|----------|----------|---------|----------|
| [https://stripe.com](https://stripe.com) | navin.grawal@example.com, navodita.grawal@example.com | Not Found | Not Found | Not Found |

## 📌 Limitations

- Only works on HTML-visible content (not JavaScript-rendered data)
- Doesn't verify emails or find all social media (only those present in raw HTML)
- Duplicate site entries may be appended if not filtered manually

## 📄 Submission Details

- **Developed by:** Poojitha Dolai  
- **Challenge Time Limit:** 5 hours  

### 📁 Repository Includes:
- `lead_scraper.py` – Python script
- `leads_output.csv` – Sample output file
- `report.md` – One-page report (explaining approach)
- `README.md` – Project overview and usage instructions
