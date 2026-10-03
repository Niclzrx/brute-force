# Brute Force Browser Automator

Ferramenta de automação para testes de autenticação utilizando **Python** e **Selenium**. Diferente de scripts baseados em requisições HTTP puras, este automatizador interage com a instância real do navegador Firefox, permitindo contornar validações simples de JavaScript e visualizar a interação em tempo real.

## 🚀 Funcionalidades

*   **Integração com Firefox**: Utiliza o WebDriver para controlar o navegador.
*   **Configuração Modular**: Sistema de seletores CSS que permite adaptar o script para qualquer site sem alterar a lógica principal do código.
*   **Suporte a Wordlists**: Leitura de arquivos de texto para teste de múltiplas credenciais.
*   **Modo Headless**: Opção para executar a automação em segundo plano (sem interface gráfica).

## 🛠️ Pré-requisitos

Antes de rodar o script, você precisará de:

1.  **Python 3.x** instalado.
2.  **Firefox** instalado no sistema.
3.  **GeckoDriver**: O driver necessário para o Selenium controlar o Firefox.
    *   [Baixe o GeckoDriver aqui](https://github.com/mozilla/geckodriver/releases) e adicione-o ao PATH do seu sistema ou coloque-o na mesma pasta do script.

## 📦 Instalação

Instale a dependência necessária via pip:

```bash
pip install selenium
```

## ⚙️ Configuração

O script é totalmente configurável através do dicionário `CONFIG` no início do arquivo `.py`. 

| Campo | Descrição |
| :--- | :--- |
| `url` | Link da página de login do alvo. |
| `usuario` | E-mail ou nome de usuário fixo para o teste. |
| `tipo_user` | Valor para campos de nível de acesso (ex: ADM, USER). |
| `wordlist` | Caminho para o arquivo `.txt` contendo as senhas. |
| `sel_email` | Seletor CSS do campo de usuário. |
| `sel_senha` | Seletor CSS do campo de senha. |
| `sel_botao` | Seletor CSS do botão de enviar/logar. |
| `msg_erro` | Texto que aparece na tela quando a senha é incorreta. |

### Como encontrar os seletores CSS?
1. Abra o site no Firefox.
2. Clique com o botão direito sobre o campo de entrada $\rightarrow$ **Inspecionar**.
3. No console de desenvolvedor, clique com o botão direito sobre a linha de código do elemento $\rightarrow$ **Copiar** $\rightarrow$ **Seletor CSS**.

## 🖥️ Como usar

1. Crie um arquivo chamado `senhas.txt` na mesma pasta do script e insira uma senha por linha.
2. Ajuste as configurações de `url` e `seletores` no código.
3. Execute o script:

```bash
python nome_do_arquivo.py
```

## ⚠️ Observações

*   **Velocidade**: Como o script abre o navegador e renderiza a página, ele é mais lento que um ataque de pacotes (requests), porém é mais eficaz contra sites que exigem renderização de DOM.
*   **Bloqueios**: O uso intensivo pode causar o bloqueio do seu IP pelo servidor alvo (WAF/Firewall).
