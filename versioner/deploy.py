import argparse
from versioner.tools import validate_commit_message, increment_version

def deploy():
    """Despliega el proyecto e incrementa la versión de deploy (minor)."""
    try:
        parser = argparse.ArgumentParser(description="Despliega el proyecto")
        parser.add_argument('--message', "-m", required=True, help='Mensaje de commit')
        args = parser.parse_args()
        validate_commit_message(args.message)
        print(f"Desplegando el proyecto con el mensaje: '{args.message}'")
        # Incrementar la versión de minor
        new_version = increment_version("minor")
        print(f"Versión actualizada a: {new_version}")
        print("Proyecto desplegado correctamente.")
    except ValueError as e:
        print(e)
    except SystemExit:
        print("Error: Argumentos inválidos.")
        print("Usa --help para ver las opciones disponibles.")