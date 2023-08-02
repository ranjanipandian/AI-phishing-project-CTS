import  requests
import re
from urllib.parse import urlparse
from tld import get_tld
from bs4 import BeautifulSoup
import whois
import socket
class urlfetcher:
    def __init__(self,url):
        self.url=url
def get_details_from_url(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extracting URL details
            url_length = len(url)
            parsed_url = urlparse(url)
            hostname = parsed_url.netloc
            hostname_length = len(hostname)
            ip = socket.gethostbyname(hostname)

            # Counting occurrences of specific characters in URL
            nb_dots = 1 if '.' in hostname else 0
            nb_hyphens = 1 if '-' in hostname else 0
            nb_at = 1 if '@' in hostname else 0
            nb_qm = 1 if '?' in hostname else 0
            nb_and =1 if '&' in hostname else 0
            nb_or =1 if '|' in hostname else 0
            nb_eq = 1 if '=' in hostname else 0
            nb_underscore = 1 if '_' in hostname else 0
            nb_tilde = 1 if '~' in hostname else 0
            nb_percent = 1 if '%' in hostname else 0
            nb_slash = 1 if '/' in hostname else 0
            nb_star = 1 if '*' in hostname else 0
            nb_colon = 1 if ':' in hostname else 0
            nb_comma = 1 if ',' in hostname else 0
            nb_semicolon =1 if ';' in hostname else 0
            nb_dollar = 1 if '$' in hostname else 0
            nb_space = 1 if ' ' in hostname else 0
            nb_www = 1 if 'www' in hostname else 0
            nb_com = 1 if '.com' in hostname else 0
            nb_dslash = 1 if '//' in hostname else 0

            # Check if URL uses http or https
            http_in_path = 1 if 'http://' in url else 0
            https_token = 1 if 'https' in url else 0

            # Ratios of digits in URL and hostname
            ratio_digits_url = sum(1 for c in url if c.isdigit()) / len(url)
            ratio_digits_host = sum(1 for c in hostname if c.isdigit()) / len(hostname)

            # Extracting domain details
            tld_in_path = 1 if get_tld(url, fail_silently=True) in parsed_url.path else 0
            tld_in_subdomain = 1 if get_tld(url, fail_silently=True) in hostname.split('.')[:-1] else 0
            abnormal_subdomain = 1 if re.match(r"^(www|mail|webmail|email)\.", hostname) else 0
            nb_subdomains = len(hostname.split('.')) - 1
            prefix_suffix = 1 if '-' in parsed_url.netloc else 0
            random_domain = 1 if re.search(r"[0-9]{4,}", hostname) else 0
            shortening_service = 1 if 'bit.ly' in hostname or 'tinyurl' in hostname else 0

            # Path details
            path_extension = parsed_url.path.split('.')[-1]
            nb_redirection = len(soup.find_all('meta', attrs={'http-equiv': 'refresh'}))
            nb_external_redirection = len([link for link in soup.find_all('a') if 'http' in link.get('href', '')])
            
            # ... Continue fetching other details as required ...

            return {
                # Add all the extracted details here as key-value pairs
                'url_length': url_length,
                'length_hostname': hostname_length,
                'ip': ip,
                'nb_dots': nb_dots,
                'nb_hyphens': nb_hyphens,
                'nb_at': nb_at,
                'nb_qm': nb_qm,
                'nb_and': nb_and,
                'nb_or': nb_or,
                'nb_eq': nb_eq,
                'nb_underscore': nb_underscore,
                'nb_tilde': nb_tilde,
                'nb_percent': nb_percent,
                'nb_slash': nb_slash,
                'nb_star': nb_star,
                'nb_colon': nb_colon,
                'nb_comma': nb_comma,
                'nb_semicolon': nb_semicolon,
                'nb_dollar': nb_dollar,
                'nb_space': nb_space,
                'nb_www': nb_www,
                'nb_com': nb_com,
                'nb_dslash': nb_dslash,
                'http_in_path': http_in_path,
                'https_token': https_token,
                'ratio_digits_url': ratio_digits_url,
                'ratio_digits_host': ratio_digits_host,
                'tld_in_path': tld_in_path,
                'tld_in_subdomain': tld_in_subdomain,
                'abnormal_subdomain': abnormal_subdomain,
                'nb_subdomains': nb_subdomains,
                'prefix_suffix': prefix_suffix,
                'random_domain': random_domain,
                'shortening_service': shortening_service,
                'path_extension': path_extension,
                'nb_redirection': nb_redirection,
                'nb_external_redirection': nb_external_redirection,
                # ... Continue adding other details ...
            }

        else:
            print(f"Failed to fetch data from the URL. Status code: {response.status_code}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Replace 'your_url_here' with the actual URL you want to fetch data from
url = input()
details = get_details_from_url(url)

if details:
    # Print all the fetched details here
    print(details)