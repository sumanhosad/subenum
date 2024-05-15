# Subdomain Enumerator

This Python script enables you to enumerate subdomains of a given domain using a wordlist file. It leverages concurrent execution to expedite the scanning process.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/sumanhosad/subenum.git
   ```

2. Navigate to the directory:

   ```bash
   cd subenum
   ```

3. Run the script:

   ```bash
   python subdomain_scanner.py
   ```

4. Follow the prompts to enter the domain name and commence the scan.

## Dependencies

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```bash
pip install requests
```

## Wordlist

Ensure that you have a wordlist file named `subdomainwordlist.txt` in the same directory as the script. This file should contain a list of subdomains to scan.

## Example

For instance, if you wish to scan subdomains of `example.com`, your `subdomainwordlist.txt` file might contain entries like:

```
www
blog
mail
admin
...
```

## Contributing

Pull requests are welcome. For significant changes, please open an issue first to discuss what you would like to alter.

Please ensure to update tests as appropriate.
