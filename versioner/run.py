import argparse
import os
import subprocess

def run():
    """Ejecuta el archivo principal del proyecto."""
    parser = argparse.ArgumentParser(description="Ejecuta tareas específicas del proyecto")
    parser.add_argument('--file','-f', help='Archivo específico a ejecutar (opcional)')
    args = parser.parse_args()

    # Archivos posibles a ejecutar
    candidates = ["app.py", "main.py", "test.py"]
    if args.file:
        candidates = [args.file]

    found_files = [file for file in candidates if os.path.exists(file)]
    
    if not found_files:
        print("No se encontraron archivos ejecutables.")
        return
    
    if len(found_files) == 1:
        print(f"Ejecutando {found_files[0]}...")
        subprocess.run(["python", found_files[0]], check=True)
    else:
        print("Se encontraron varios archivos ejecutables:")
        for i, file in enumerate(found_files, start=1):
            print(f"{i}. {file}")
        choice = input("Selecciona el archivo a ejecutar (número): ")
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(found_files):
                print(f"Ejecutando {found_files[choice_index]}...")
                subprocess.run(["python", found_files[choice_index]], check=True)
            else:
                print("Selección inválida. Abortando.")
        except ValueError:
            print("Entrada inválida. Abortando.")