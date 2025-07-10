import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_pattern, text)

def extract_social_links(soup):
    links = soup.find_all('a', href=True)
    social_links = {
        'LinkedIn': None,
        'Twitter': None,
        'Facebook': None
    }
    for link in links:
        href = link['href']
        if 'linkedin.com' in href and not social_links['LinkedIn']:
            social_links['LinkedIn'] = href
        elif 'twitter.com' in href and not social_links['Twitter']:
            social_links['Twitter'] = href
        elif 'facebook.com' in href and not social_links['Facebook']:
            social_links['Facebook'] = href
    return social_links

def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        emails = list(set(extract_emails(response.text)))
        social = extract_social_links(soup)

        data = {
            'Website': url,
            'Email(s)': ', '.join(emails) if emails else "Not Found",
            'LinkedIn': social['LinkedIn'] or "Not Found",
            'Twitter': social['Twitter'] or "Not Found",
            'Facebook': social['Facebook'] or "Not Found"
        }
        return data
    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        return None

def main():
    url = input("🔗 Enter a company website URL (with https://): ").strip()

    print(f"🔍 Scraping {url}...")
    data = scrape_website(url)
    if data:
        df = pd.DataFrame([data])
        
        file_path = "leads_output.csv"
        file_exists = os.path.exists(file_path)
        
        df.to_csv(file_path, mode='a', header=not file_exists, index=False)
        print(f"✅ Done! Data added to '{file_path}'.")
    else:
        print("⚠️ No data scraped.")

if __name__ == "__main__":
    main()
