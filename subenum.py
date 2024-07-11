import requests
import time
import signal
import sys

def check_subdomain(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f'[+] {url}')
        else:
            print(f'[-] {url} returned status code {response.status_code}')
    except requests.RequestException:
        pass

def domain_scanner(domain_name, sub_domnames):
    print('----URLs after scanning subdomains----')
    urls = [f"https://{subdomain}.{domain_name}" for subdomain in sub_domnames]
    start_time = time.time()
    try:
        for url in urls:
            check_subdomain(url)
    except KeyboardInterrupt:
        print("\nScan interrupted by user")
        sys.exit(0)
    end_time = time.time()
    print(f"Scan completed in {end_time - start_time:.2f} seconds")

def signal_handler(signum, frame):
    print("\nScan interrupted by user")
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    try:
        dom_name = input("Enter the Domain Name: ").strip()
        with open('subdomainwordlist.txt', 'r') as file:
            sub_dom = file.read().splitlines()
        domain_scanner(dom_name, sub_dom)
    except FileNotFoundError:
        print("Error: The file 'subdomainwordlist.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

