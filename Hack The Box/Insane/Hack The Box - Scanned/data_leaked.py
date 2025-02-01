import requests
import sys
import re
import struct
from argparse import ArgumentParser

def main(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    response = re.findall(r"sys_57311\(\) = 0x([a-f0-9]+)", r.text, re.MULTILINE)
    data = b""
    for val in response:
        data += struct.pack("Q", int(val, 16))

    try:
        print(data.decode())
    except UnicodeDecodeError as e:
        print(f"Error decoding exfiltrated data: {e}")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-u", "--url", help="Direccion web del host a analizar", required=True)
    args = parser.parse_args()
    main(args.url)
	
onedayyoufeellikecrying