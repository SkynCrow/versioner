import argparse
import os
import subprocess

def setup():
    """Configura el proyecto verificando y creando el entorno virtual."""
    parser = argparse.ArgumentParser(description="Configura el proyecto")
    parser.add_argument('--path', '-p', default=".venv", help='Nombre del entorno virtual (por defecto: .venv)')
    args = parser.parse_args()

    venv_path = args.venv
    
    if os.path.exists(venv_path):
        print(f"El entorno virtual '{venv_path}' ya existe.")
    else:
        print(f"Creando el entorno virtual '{venv_path}'...")
        subprocess.run(["python", "-m", "venv", venv_path], check=True)
        print(f"Entorno virtual '{venv_path}' creado correctamente.")
    
    requirements_path = "requirements.txt"
    if os.path.exists(requirements_path):
        print("Instalando dependencias desde requirements.txt...")
        subprocess.run([os.path.join(venv_path, "bin", "pip"), "install", "-r", requirements_path], check=True)
        print("Dependencias instaladas correctamente.")
    else:
        print("No se encontró un archivo requirements.txt. Saltando instalación de dependencias.")