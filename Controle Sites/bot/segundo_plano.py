import subprocess

# Comando que será executado em segundo plano
cmd = 'python game.py'

# Executa o comando em segundo plano usando o subprocess
subprocess.Popen(cmd, shell=True)
