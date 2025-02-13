#!/bin/bash
function exit_script(){
	echo -e "\n[!] Saliendo"
}

for i in {1..254}; do
	timeout 1 bash -c "ping -c 1 172.17.0.$i" &>/dev/null && echo "[+] Host activo: 172.17.0.$i" &
done; wait
