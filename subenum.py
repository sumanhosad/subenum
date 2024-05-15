import requests

def domain_scanner(domain_name, sub_domnames):
    print('----URL after scanning subdomains----')
    for subdomain in sub_domnames:
        url = f"https://{subdomain}.{domain_name}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f'[+] {url}')
            else:
                print(f'[-] {url} returned status code {response.status_code}')
        except requests.ConnectionError:
            pass

if __name__ == '__main__':
    try:
        dom_name = input("Enter the Domain Name: ").strip()
        with open('subdomainwordlist.txt', 'r') as file:
            sub_dom = file.read().splitlines()
        domain_scanner(dom_name, sub_dom)
    except FileNotFoundError:
        print("Error: The file 'subdomain_names1.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

