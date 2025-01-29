import tldextract
import requests
from bs4 import BeautifulSoup

def extract_domain(url):
    ext = tldextract.extract(url)
    return ext.domain, ext.suffix

def is_phishing(url):
    # Basic checks
    suspicious_keywords = ['login', 'secure', 'account', 'update', 'verify']
    if any(word in url for word in suspicious_keywords):
        return True
    
    # Check if URL uses HTTPS
    if not url.startswith("https://"):
        return True

    # Further checks: Extract domain and check if it looks suspicious
    domain, suffix = extract_domain(url)
    suspicious_domains = ['fakeexample', 'phishingsite', 'maliciousdomain']
    if domain in suspicious_domains:
        return True

    return False

def fetch_page_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string if soup.title else 'No title found'
    except requests.exceptions.RequestException as e:
        return f"Error fetching page: {e}"

# Test the phishing detection function with suspicious URLs
url = "https://www.linkedin.com/pulse/how-simplify-your-linkedin-url-brenda-meller-zawacki--1/"
if is_phishing(url):
    print(f"Phishing detected: {url}")
else:
    print(f"Safe URL: {url}")

# Fetch page title for further analysis
print(f"Page title: {fetch_page_title(url)}")
