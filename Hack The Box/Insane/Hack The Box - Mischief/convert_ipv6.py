#!/usr/bin/python3
from argparse import ArgumentParser
def convert_ipv6(encoded_ipv6):
    parts = encoded_ipv6.split(".")
    if len(parts) != 16:
        raise ValueError("La cadena codificada debe tener 16 partes.")
    ipv6 = ""
    for i in range(0, len(parts), 2):
        segment = hex(int(parts[i]))[2:].rjust(2, '0') + hex(int(parts[i+1]))[2:].rjust(2, '0')
        ipv6 += segment + ":"
    ipv6 = ipv6[:-1]
    return ipv6

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-e", "--encoded_ipv6", help="Direccion web del host a analizar", required=True)
    
    #encoded_ipv6 = "222.173.190.239.0.0.0.0.2.80.86.255.254.148.114.166"
    args = parser.parse_args()
    print(convert_ipv6(args.encoded_ipv6))
