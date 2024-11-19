
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import pandas as pd
# import time
# import urllib.parse

# # Function to load job listings using Selenium
# def load_indeed_jobs_div(url):
#     options = Options()
#     options.add_argument('--headless')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
#     options.add_argument('--window-size=1920x1080')
#     options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.120 Safari/537.36')

#     service = Service('E:/SEM5-EDI/Scraping/chromedriver.exe')  # Update with the path to your WebDriver
#     driver = webdriver.Chrome(service=service, options=options)
    
#     driver.get(url)
#     time.sleep(5)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     driver.quit()
    
#     return soup

# # Function to extract job information
# def extract_job_information_indeed(driver, soup):
#     jobs_list = []
#     job_elems = soup.find_all("div", class_="job_seen_beacon")  # Adjust class based on the actual structure

#     for job_elem in job_elems:
#         title_elem = job_elem.find("a")
#         title = title_elem.find("span").text.strip() if title_elem and title_elem.find("span") else 'N/A'

#         company_elem = job_elem.find("span", {"data-testid": "company-name"})  # Using data-testid to ensure accurate scraping
#         company = company_elem.text.strip() if company_elem else 'N/A'

#         location_elem = job_elem.find("div", {"data-testid": "text-location"})  # Ensuring the correct location class
#         location = location_elem.text.strip() if location_elem else 'N/A'

#         # Get job description by clicking the job link
#         job_url = "https://www.indeed.co.in" + title_elem['href'] if title_elem and title_elem['href'] else None
#         description = scrape_job_description(driver, job_url) if job_url else 'N/A'

#         role_elem = job_elem.find("div", {"class": "jobMetaDataGroup"})  # Extracting role-related information if available
#         role = role_elem.text.strip() if role_elem else 'N/A'

#         formatted_summary = f"Company: {company}\nLocation: {location}\nDescription: {description}\nRole: {role}"

#         jobs_list.append({
#             'Title': title,
#             'Company': company,
#             'Location': location,
#             'Description': description,
#             'Role': role,
#             'Summary': formatted_summary
#         })

#     return jobs_list, len(jobs_list)

# # Function to scrape the job description from a specific job page
# def scrape_job_description(driver, job_url):
#     driver.get(job_url)
#     time.sleep(3)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
    
#     # Extracting the full job description from the job detail page
#     description_elem = soup.find("div", {"id": "jobDescriptionText", "class": "jobsearch-JobComponent-description"}) or \
#                        soup.find("div", class_="css-16y4thd eu4oa1w0")
#     description = description_elem.text.strip() if description_elem else 'N/A'
    
#     return description

# # Function to get the next page URL
# def get_next_page_url(soup):
#     try:
#         next_page_elem = soup.find("a", {"data-testid": "pagination-page-next"})
#         if next_page_elem and "href" in next_page_elem.attrs:
#             return "https://www.indeed.co.in" + next_page_elem["href"]
#         else:
#             return None
#     except Exception as e:
#         print(f"Error finding next page: {e}")
#         return None

# # Function to find jobs from one location and return as a DataFrame
# def find_jobs_from(url, max_pages=5):
#     options = Options()
#     options.add_argument('--headless')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
#     options.add_argument('--window-size=1920x1080')
#     options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.120 Safari/537.36')

#     service = Service('E:/Scraping/ClonedWork/Scraping/chromedriver.exe')  # Update with the path to your WebDriver
#     driver = webdriver.Chrome(service=service, options=options)
    
#     jobs_list = []
#     current_page = 0
#     while url and current_page < max_pages:
#         current_page += 1
#         print(f"Scraping page {current_page}: {url}")
        
#         soup = load_indeed_jobs_div(url)
#         new_jobs, num_listings = extract_job_information_indeed(driver, soup)
#         jobs_list.extend(new_jobs)
        
#         url = get_next_page_url(soup)
    
#     driver.quit()
    
#     return pd.DataFrame(jobs_list)

# # Main function to scrape jobs from Pune and Mumbai, and save to Excel
# def main():
#     website = 'https://www.indeed.co.in/jobs'
#     job_title = 'Backend Developer'
#     locations = ['Pune', 'Mumbai']  # Scraping jobs from Pune and Mumbai
#     filename = 'job_results.xlsx'
    
#     all_jobs_list = []  # Collect all job data

#     for location in locations:
#         encoded_job_title = urllib.parse.quote(job_title)
#         encoded_location = urllib.parse.quote(location)
        
#         url = f'{website}?q={encoded_job_title}&l={encoded_location}'
#         print(f"Scraping jobs from: {location}")
        
#         df = find_jobs_from(url)
#         all_jobs_list.append(df)  # Append DataFrame for each location

#     # Concatenate all job DataFrames into a single DataFrame
#     final_df = pd.concat(all_jobs_list, ignore_index=True)

#     # Save the final DataFrame to Excel
#     final_df.to_excel(filename, index=False)
#     print(f"Job postings retrieved and stored in {filename}.")

# if __name__ == "__main__":
#     main()

















# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import pandas as pd
# import time
# import urllib.parse

# # Function to load job listings using Selenium
# def load_indeed_jobs_div(url):
#     options = Options()
#     options.add_argument('--headless')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
#     options.add_argument('--window-size=1920x1080')
#     options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.120 Safari/537.36')

#     service = Service('E:/SEM5-EDI/Scraping/chromedriver.exe')  # Update with the path to your WebDriver
#     driver = webdriver.Chrome(service=service, options=options)
    
#     driver.get(url)
#     time.sleep(5)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     driver.quit()
    
#     return soup

# # Function to extract job information
# def extract_job_information_indeed(driver, soup):
#     jobs_list = []
#     job_elems = soup.find_all("div", class_="job_seen_beacon")  # Adjust class based on the actual structure

#     for job_elem in job_elems:
#         title_elem = job_elem.find("a")
#         title = title_elem.find("span").text.strip() if title_elem and title_elem.find("span") else 'N/A'

#         company_elem = job_elem.find("span", {"data-testid": "company-name"})  # Using data-testid to ensure accurate scraping
#         company = company_elem.text.strip() if company_elem else 'N/A'

#         location_elem = job_elem.find("div", {"data-testid": "text-location"})  # Ensuring the correct location class
#         location = location_elem.text.strip() if location_elem else 'N/A'

#         # Get job description by clicking the job link
#         job_url = "https://www.indeed.co.in" + title_elem['href'] if title_elem and title_elem.get('href') else None
#         description = scrape_job_description(driver, job_url) if job_url else 'N/A'

#         role_elem = job_elem.find("div", {"class": "jobMetaDataGroup"})  # Extracting role-related information if available
#         role = role_elem.text.strip() if role_elem else 'N/A'

#         formatted_summary = f"Company: {company}\nLocation: {location}\nDescription: {description}\nRole: {role}"

#         jobs_list.append({
#             'Title': title,
#             'Company': company,
#             'Location': location,
#             'Description': description,
#             'Role': role,
#             'URL': job_url,  
#             'Summary': formatted_summary
#         })

#     return jobs_list, len(jobs_list)


# # Function to scrape the job description from a specific job page
# def scrape_job_description(driver, job_url):
#     driver.get(job_url)
#     time.sleep(3)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
    
#     # Extracting the full job description from the job detail page
#     description_elem = soup.find("div", {"id": "jobDescriptionText", "class": "jobsearch-JobComponent-description"}) or \
#                        soup.find("div", class_="css-16y4thd eu4oa1w0")
#     description = description_elem.text.strip() if description_elem else 'N/A'
    
#     return description

# # Function to get the next page URL
# def get_next_page_url(soup):
#     try:
#         next_page_elem = soup.find("a", {"data-testid": "pagination-page-next"})
#         if next_page_elem and "href" in next_page_elem.attrs:
#             return "https://www.indeed.co.in" + next_page_elem["href"]
#         else:
#             return None
#     except Exception as e:
#         print(f"Error finding next page: {e}")
#         return None

# # Function to find jobs from one location and return as a DataFrame
# def find_jobs_from(url, max_pages=5):
#     options = Options()
#     options.add_argument('--headless')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
#     options.add_argument('--window-size=1920x1080')
#     options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.120 Safari/537.36')

#     service = Service('E:/Scraping/ClonedWork/Scraping/chromedriver.exe')  # Update with the path to your WebDriver
#     driver = webdriver.Chrome(service=service, options=options)
    
#     jobs_list = []
#     current_page = 0
#     while url and current_page < max_pages:
#         current_page += 1
#         print(f"Scraping page {current_page}: {url}")
        
#         soup = load_indeed_jobs_div(url)
#         new_jobs, num_listings = extract_job_information_indeed(driver, soup)
#         jobs_list.extend(new_jobs)
        
#         url = get_next_page_url(soup)
    
#     driver.quit()
    
#     return pd.DataFrame(jobs_list)

# # Main function to scrape jobs from Pune and Mumbai, and save to Excel
# def main():
#     website = 'https://www.indeed.co.in/jobs'
#     job_title = 'Backend Developer'
#     locations = ['Pune', 'Mumbai']  # Scraping jobs from Pune and Mumbai
#     filename = 'job_results.xlsx'
    
#     all_jobs_list = []  # Collect all job data

#     for location in locations:
#         encoded_job_title = urllib.parse.quote(job_title)
#         encoded_location = urllib.parse.quote(location)
        
#         url = f'{website}?q={encoded_job_title}&l={encoded_location}'
#         print(f"Scraping jobs from: {location}")
        
#         df = find_jobs_from(url)
#         all_jobs_list.append(df)  # Append DataFrame for each location

#     # Concatenate all job DataFrames into a single DataFrame
#     final_df = pd.concat(all_jobs_list, ignore_index=True)

#     # Save the final DataFrame to Excel
#     final_df.to_excel(filename, index=False)
#     print(f"Job postings retrieved and stored in {filename}.")

# if __name__ == "__main__":
#     main()





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

    service = Service('E:/SEM5-EDI/Scraping/chromedriver.exe')  # Update with the path to your WebDriver
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    
    return soup

# Function to extract job information
def extract_job_information_indeed(driver, soup):
    jobs_list = []
    job_elems = soup.find_all("div", class_="job_seen_beacon")  # Adjust class based on the actual structure

    for job_elem in job_elems:
        title_elem = job_elem.find("a")
        title = title_elem.find("span").text.strip() if title_elem and title_elem.find("span") else 'N/A'

        company_elem = job_elem.find("span", {"data-testid": "company-name"})  # Using data-testid to ensure accurate scraping
        company = company_elem.text.strip() if company_elem else 'N/A'

        location_elem = job_elem.find("div", {"data-testid": "text-location"})  # Ensuring the correct location class
        location = location_elem.text.strip() if location_elem else 'N/A'

        # Get job description by clicking the job link
        job_url = "https://www.indeed.co.in" + title_elem['href'] if title_elem and title_elem.get('href') else None
        description = scrape_job_description(driver, job_url) if job_url else 'N/A'

        role_elem = job_elem.find("div", {"class": "jobMetaDataGroup"})  # Extracting role-related information if available
        role = role_elem.text.strip() if role_elem else 'N/A'

        # Create a formatted summary
        formatted_summary = f"Company: {company}\nLocation: {location}\nDescription: {description}\nRole: {role}\nURL: {job_url}"

        jobs_list.append({
            'Title': title,
            'Company': company,
            'Location': location,
            'Description': description,
            'Role': role,
            'URL': job_url,  
            'Summary': formatted_summary
        })

    return jobs_list, len(jobs_list)


# Function to scrape the job description from a specific job page
def scrape_job_description(driver, job_url):
    driver.get(job_url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Extracting the full job description from the job detail page
    description_elem = soup.find("div", {"id": "jobDescriptionText", "class": "jobsearch-JobComponent-description"}) or \
                       soup.find("div", class_="css-16y4thd eu4oa1w0")
    description = description_elem.text.strip() if description_elem else 'N/A'
    
    return description

# Function to get the next page URL
def get_next_page_url(soup):
    try:
        next_page_elem = soup.find("a", {"data-testid": "pagination-page-next"})
        if next_page_elem and "href" in next_page_elem.attrs:
            return "https://www.indeed.co.in" + next_page_elem["href"]
        else:
            return None
    except Exception as e:
        print(f"Error finding next page: {e}")
        return None

# Function to find jobs from one location and return as a DataFrame
def find_jobs_from(url, max_pages=2):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920x1080')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.120 Safari/537.36')

    service = Service('E:/Scraping/ClonedWork/Scraping/chromedriver.exe')  # Update with the path to your WebDriver
    driver = webdriver.Chrome(service=service, options=options)
    
    jobs_list = []
    current_page = 0
    while url and current_page < max_pages:
        current_page += 1
        print(f"Scraping page {current_page}: {url}")
        
        soup = load_indeed_jobs_div(url)
        new_jobs, num_listings = extract_job_information_indeed(driver, soup)
        jobs_list.extend(new_jobs)
        
        url = get_next_page_url(soup)
    
    driver.quit()
    
    return pd.DataFrame(jobs_list)

# Main function to scrape jobs from Pune and Mumbai, and save to Excel
def main():
    website = 'https://www.indeed.co.in/jobs'
    job_title = 'Backend Developer'
    locations = ['Pune', 'Mumbai']  # Scraping jobs from Pune and Mumbai
    filename = 'job_results.xlsx'
    
    all_jobs_list = []  # Collect all job data
    
    for location in locations:
        encoded_job_title = urllib.parse.quote(job_title)
        encoded_location = urllib.parse.quote(location)
        
        url = f'{website}?q={encoded_job_title}&l={encoded_location}'
        print(f"Scraping jobs from: {location}")
        
        df = find_jobs_from(url)
        all_jobs_list.append(df)  # Append DataFrame for each location

    # Concatenate all job DataFrames into a single DataFrame
    final_df = pd.concat(all_jobs_list, ignore_index=True)

    # Save the final DataFrame to Excel
    final_df.to_excel(filename, index=False)
    print(f"Job postings retrieved and stored in {filename}.")

if __name__ == "__main__":
    main()
