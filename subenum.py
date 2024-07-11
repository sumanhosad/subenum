import aiohttp
import asyncio
import time
import signal

async def check_subdomain(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                print(f'[+] {url}')
            else:
                print(f'[-] {url} returned status code {response.status}')
    except aiohttp.ClientError:
        pass

async def domain_scanner(domain_name, sub_domnames):
    print('----URLs after scanning subdomains----')
    urls = [f"https://{subdomain}.{domain_name}" for subdomain in sub_domnames]
    async with aiohttp.ClientSession() as session:
        tasks = [check_subdomain(session, url) for url in urls]
        await asyncio.gather(*tasks)

def signal_handler(signum, frame):
    print("\nScan interrupted by user")
    exit(0)

if __name__ == '__main__':
    try:
        signal.signal(signal.SIGINT, signal_handler)
        dom_name = input("Enter the Domain Name: ").strip()
        with open('subdomainwordlist.txt', 'r') as file:
            sub_dom = file.read().splitlines()

        start_time = time.time()
        asyncio.run(domain_scanner(dom_name, sub_dom))
        end_time = time.time()
        print(f"Scan completed in {end_time - start_time:.2f} seconds")
    except FileNotFoundError:
        print("Error: The file 'subdomainwordlist.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

