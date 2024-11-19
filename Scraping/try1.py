





import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import urllib.parse

# Function to load job listings using Selenium
def load_indeed_jobs_div(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920x1080')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.120 Safari/537.36')

    service = Service('E:/SEM5-EDI/Scraping/chromedriver.exe')  # Update the WebDriver path
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.get(url)
    time.sleep(5)  # Allow page to load
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    
    return soup

# Function to extract job information
def extract_job_information_indeed(soup):
    jobs_list = []
    job_elems = soup.find_all("div", class_="job_seen_beacon")

    for job_elem in job_elems:
        # Extract title
        title_elem = job_elem.find("a")
        title = title_elem.find("span").text.strip() if title_elem and title_elem.find("span") else 'N/A'

        # Extract company name
        company_elem = job_elem.find("span", {"data-testid": "company-name"})
        company = company_elem.text.strip() if company_elem else 'N/A'

        # Extract location
        location_elem = job_elem.find("div", {"data-testid": "text-location"})
        location = location_elem.text.strip() if location_elem else 'N/A'

        # Extract job URL
        job_url = f"https://www.indeed.co.in{title_elem['href']}" if title_elem and title_elem.get('href') else None

        # Extract role
        role_elem = job_elem.find("div", {"class": "jobMetaDataGroup"})
        role = role_elem.text.strip() if role_elem else 'N/A'

        # Append data to the jobs list
        jobs_list.append({
            'Title': title,
            'Company': company,
            'Location': location,
            'Role': role,
            'URL': job_url
        })

    return jobs_list

# Function to get the next page URL
def get_next_page_url(soup):
    try:
        next_page_elem = soup.find("a", {"data-testid": "pagination-page-next"})
        if next_page_elem and "href" in next_page_elem.attrs:
            return f"https://www.indeed.co.in{next_page_elem['href']}"
        return None
    except Exception as e:
        print(f"Error finding next page: {e}")
        return None

# Function to scrape jobs from Indeed
def find_jobs_from(url, max_pages=5):
    jobs_list = []
    current_page = 0

    while url and current_page < max_pages:
        current_page += 1
        print(f"Scraping page {current_page}: {url}")
        
        soup = load_indeed_jobs_div(url)
        new_jobs = extract_job_information_indeed(soup)
        jobs_list.extend(new_jobs)
        
        url = get_next_page_url(soup)
    
    return pd.DataFrame(jobs_list)

# Main function to scrape jobs from Pune and Mumbai and save to Excel
def main():
    website = 'https://www.indeed.co.in/jobs'
    job_title = 'Backend Developer'
    locations = ['Pune', 'Mumbai']
    filename = 'job_results_1.xlsx'
    
    all_jobs_list = []

    for location in locations:
        encoded_job_title = urllib.parse.quote(job_title)
        encoded_location = urllib.parse.quote(location)
        
        url = f'{website}?q={encoded_job_title}&l={encoded_location}'
        print(f"Scraping jobs from: {location}")
        
        df = find_jobs_from(url)
        all_jobs_list.append(df)

    # Combine all job data into a single DataFrame
    final_df = pd.concat(all_jobs_list, ignore_index=True)

    # Save the DataFrame to Excel
    final_df.to_excel(filename, index=False)
    print(f"Job postings retrieved and stored in {filename}.")

if __name__ == "__main__":
    main()


