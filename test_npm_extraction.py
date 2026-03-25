import subprocess
import json
import os

# Caminho para o npm no Windows
npm_path = r"C:\Program Files\nodejs\npm.cmd"

# Caminho do seu projeto Node
repo_path = r"C:\Users\Rafael\Desktop\TaskReactVite"

def test_npm_list():
    current_dir = os.getcwd()
    try:
        os.chdir(repo_path)
        print("Rodando npm list para extrair dependências...")
        result = subprocess.run(
            [npm_path, "ls", "--json", "--all", "--long"],
            capture_output=True,
            text=True,
            check=False
        )
        if result.returncode not in (0, 1):
            print(f"Erro ao executar npm list: {result.stderr}")
            return

        npm_data = json.loads(result.stdout)
        print("Nome do projeto:", npm_data.get("name"))
        print("Versão do projeto:", npm_data.get("version"))
        print("Dependências encontradas:", list(npm_data.get("dependencies", {}).keys()))
    
    except Exception as e:
        print("Erro:", str(e))
    finally:
        os.chdir(current_dir)

if __name__ == "__main__":
    test_npm_list()