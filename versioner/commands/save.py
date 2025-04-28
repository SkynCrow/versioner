import argparse
import subprocess
from versioner.utils.version_manager import GREEN, RED, RESET, read_version, validate_commit_message, increment_version, write_version

def save():
    """Guarda el estado del proyecto e incrementa la versión de save (patch)."""
    old_version = read_version()
    print("Versión actual:",GREEN,old_version,RESET)
    try:
        parser = argparse.ArgumentParser(description="Guarda el estado del proyecto")
        parser.add_argument('--message','-m', required=True, help='Mensaje de commit')
        parser.add_argument('--upload','-u', action='store_true', help='Sube el commit al repositorio remoto')
        args = parser.parse_args()
        validate_commit_message(args.message)
        print(f"Guardando el estado del proyecto con el mensaje: '{args.message}'")
        new_version = increment_version("patch")
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", args.message], check=True)
        if args.upload:
            subprocess.run(["git", "push"], check=True)
        print("Versión actualizada a",GREEN, new_version,RESET)
        return True
    except ValueError as e:
        print(e)
    except SystemExit:
        print("Error: Argumentos inválidos.")
        print("Usa --help para ver las opciones disponibles.")
    # Si ocurre un error, revertir a la versión anterior
    print(f"{RED}Algo fallo. Revirtiendo versión...",GREEN, old_version,RESET)
    write_version(old_version)
    return False
