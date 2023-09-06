import subprocess
import sys

def instalar_pip():
    try:
        # Verifica se o pip já está instalado
        import pip
    except ImportError:
        # Baixa o script get-pip.py
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--default-pip"])
        print("pip foi instalado com sucesso!")

def instalar_graphviz():
    try:
        # Comando para instalar o pacote graphviz usando o pip
        comando = [sys.executable, "-m", "pip", "install", "graphviz"]

        # Executa o comando usando subprocess
        subprocess.check_call(comando)
        print("O pacote 'graphviz' foi instalado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao instalar 'graphviz': {e}")

# Instala o pip (caso não esteja instalado)
instalar_pip()

# Instala o pacote graphviz
instalar_graphviz()
