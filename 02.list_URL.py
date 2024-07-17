Question_2 = """
            Write a Python function that takes a list of URLs, attempts to download their content, and retries up to 3 times if an error occurs. Use appropriate error handling to manage different types of exceptions.
"""

import requests

from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout

def download_urls(url_list):
    def fetch_url(url, retries=3):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.text
        except (HTTPError, ConnectionError, Timeout) as e:
            if retries > 0:
                return fetch_url(url, retries - 1)
            else:
                print(f"Failed to retries {url} after 3 attempts: {e}")
                return None
        except RequestException as e:
                      print(f"An error occured fo {url}: {e}")
                      return None
        
    results = {}

    for url in url_list:
         results[url] = fetch_url(url)
    return results

urls = [
    "https://www.example.com",
    "https://www.nonexistenwebsite",
    "https://www.google.com"
]

content = download_urls(urls)
for url, text in content.items():
    if text:
        print(f"content of {url}:\n{text[:200]}...\n")
    else:
         print(f"Failed to retrieve content from {url}\n")
     

