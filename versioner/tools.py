import os
import re

VERSION_FILE = "version.txt"
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
def read_version():
    """Lee la versión actual del archivo version.txt."""
    if not os.path.exists(VERSION_FILE):
        return "1.0.0"  # Versión inicial por defecto
    with open(VERSION_FILE, "r",encoding='utf-8') as f:
        return f.read().strip()

def write_version(version):
    """Escribe la nueva versión en el archivo version.txt."""
    with open(VERSION_FILE, "w",encoding='utf-8') as f:
        f.write(version)
    # Editamos el toml de la aplicación, y actualizamos la versión
    with open("pyproject.toml", "r",encoding='utf-8') as f:
        lines = f.readlines()
    with open("pyproject.toml", "w",encoding='utf-8') as f:
        for line in lines:
            if line.startswith("version = "):
                f.write(f'version = "{version}"\n')
            else:
                f.write(line)

def increment_version(part,write=True):
    """
    Incrementa la versión según la parte especificada.
    - part = "major": Incrementa el número base (1 -> 2).
    - part = "minor": Incrementa el número de deploy (1.0 -> 1.1).
    - part = "patch": Incrementa el número de save (1.0.0 -> 1.0.1).
    """
    version = read_version()
    major, minor, patch = map(int, version.split("."))
    
    if part == "major":
        major += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    elif part == "patch":
        patch += 1
    
    new_version = f"{major}.{minor}.{patch}"
    if write:
        write_version(new_version)
    return new_version


def validate_commit_message(message):
    """
    Valida si el mensaje de commit cumple con el estándar de Conventional Commits.
    Ejemplo válido: 'feat(auth): añadir soporte para autenticación con OAuth'
    """
    pattern = r"^(feat|fix|docs|style|refactor|perf|test|chore)(\([\w\-]+\))?: .{1,50}$"
    if not re.match(pattern, message):
        raise ValueError(
            f"El mensaje \"{message}\" de commit no cumple con el estándar de Conventional Commits.\n"
            "Ejemplo válido: 'feat(auth): añadir soporte para autenticación con OAuth'\n"
            "Opciones válidas:\n"
            "-  feat: Nueva funcionalidad\n"
            "-  fix: Corrección de errores\n"
            "-  docs: Cambios en la documentación\n"
            "-  style: Cambios en el formato del código \n"
            "-  refactor: Cambios en el código que no afectan a la funcionalidad\n"
            "-  perf: Mejora del rendimiento\n"
            "-  test: Añadir pruebas o corregir pruebas existentes\n"
            "-  chore: Cambios menores o tareas de mantenimiento\n"
        )