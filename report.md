# 📝 Caprae Capital AI-Readiness Challenge Report  
### Project: Smart Lead Scraper  
**Candidate:** Poojitha Dolai  
**Duration:** Completed within 5-hour constraint

---

## 🧠 Objective

To build a lightweight tool that addresses a common bottleneck in lead generation: extracting business contact information (emails, social media) from websites. The solution is designed to be fast, easy to use, and able to collect useful data for sales or outreach efforts.

---

## 💻 Tools & Technologies

- **Python 3**
- **Requests** – Fetch HTML content
- **BeautifulSoup** – Parse website HTML
- **Regex (re)** – Extract email addresses
- **Pandas** – Store and append data to CSV

---

## ⚙️ Approach

- The user enters a business website URL.
- The tool scrapes:
  - **Emails** using regex pattern matching
  - **Social media links** (LinkedIn, Twitter, Facebook) from anchor tags
- All results are stored and **appended** into `leads_output.csv`, making the tool suitable for repeated use across many websites.
- The scraper handles missing content gracefully by returning "Not Found" when no data is available.

---

## 🧪 Output Sample

| Website             | Emails                                  | LinkedIn   | Twitter    | Facebook    |
|---------------------|------------------------------------------|------------|------------|-------------|
| https://stripe.com  | navin.grawal@example.com, navodita.grawal@example.com | Not Found | Not Found | Not Found |

---

## 🎯 Business Use Case

This tool simulates a key feature of [SaaSquatchLeads](https://www.saasquatchleads.com) — collecting high-impact contact data for cold outreach. In a real-world setting, such a script can power CRM enrichment, sales prospecting, or startup sourcing pipelines. It offers a low-complexity, high-utility solution for data collection teams.

---

## ⚖️ Tradeoffs

- Does not handle JavaScript-rendered content (due to using `requests`)
- No advanced email verification (for simplicity)
- Appends data without duplication checks (assumes manual filtering)

These were accepted trade-offs to meet the 5-hour limit while delivering a focused, testable solution.

---

## ✅ Conclusion

This project aligns with Caprae Capital’s AI-driven business enhancement vision by demonstrating practical automation of a common business task. The code is clean, modular, and extendable — ready for integration into broader M&A or sales enablement workflows.

