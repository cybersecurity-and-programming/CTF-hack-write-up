#!/usr/bin/python3
from argparse import ArgumentParser
import base64
'''
###################################################
#    script de python para la maquina baseMe      #
#    de la plataforma de HackMyVM                 #  
#    Fecha: 15-Agoosto-2024                       #      
###################################################
'''
def convert_wordlist(wordlist, archivo_salida):
    try:
        with open(wordlist, 'r') as file:
            words = file.read().splitlines()
        
        if not words:
            raise ValueError("El archivo de entrada está vacío.")
            
        encoded_words = [base64.b64encode(word.encode()).decode() for word in words]

        # Escribir las palabras codificadas en un nuevo archivo
        with open(archivo_salida, 'w') as file:
            for word in encoded_words:
                file.write(f"{word}\n")
        print("[+] Archivo convertido correctamente")
    except FileNotFoundError as fnf_error:
        print("Error: No se ha encontrado el archivo solicitado")
    except IOError as io_error:
        print("Error de E/S: {}".format(io_error))
    except ValueError as value_error:
        print("Error: {}".format(value_error))
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
    
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-w", "--wordlist", help="diccionario elegido para convertir", required=True)
    parser.add_argument("-o", "--output", help="Nombre del archivo de salida")
        
    args = parser.parse_args()  
    archivo_salida = args.output
    if archivo_salida == None:
        archivo_salida = 'encoded_wordlist.txt'
    convert_wordlist(args.wordlist,archivo_salida)
    
