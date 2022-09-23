# Portifólio
 Projeto portifólio

## •Instalação e utilização da aplicação
•Instalação
1. Baixe o Python

    No site oficial do Python na aba de downloads procure pelo seu sistema operacional e siga os passos de instalação.
    https://www.python.org/downloads/

2. Adicionando ao Path (sistemas Windows somente)

    Durante a instalação do Python no Windows se a opção de adicionar o Python no Path não for assinalada o sistema operacional não vai conseguir reconhecer o comando 'python' na linha de comando como uma variável de ambiente que remete as funções do Python, essa funcionalidade é necessária para a utilização da nossa aplicação. Portanto **DURANTE A INSTALAÇÃO DO PYTHON NO WINDOWS ASSINALE A OPÇÃO "ADD PYTHON <VERSÃO> TO PATH"**

•UTILIZANDO A APLICAÇÃO
1. Crie um diretório
- Crie um diretório e navegue até ele atraves da linha de comando.

```console
    mkdir <nome do diretório>
    cd <nome do diretório>
```

2. Clone o repositório

```console
    git clone https://github.com/Yetgvg/Portifolio.git
```
3. Crie um ambiente virutal

```terminal do VS Code
    python -m venv <nome do ambiente>
```
- Utilizamos a variável de ambiente 'python' citada na sessão de instalação, caso esse comando falhe no seu ambiente tente:
```terminal do VS Code
    python3 -m venv <nome do ambiente>
```
- Caso mesmo assim o diretório com o nome do ambiente não seja criado assegure-se que o **python está configurado em suas variáveis de ambiente** e tente novamente o processo.

4. Executar o ambiente virtual

- No Windows:

```terminal do VS Code
    cd <nome do ambiente>\Scripts
    activate.bat
```

- No Unix(Linux)/MacOS:
```console
    source <nome do ambiente>/bin/activate
```

5. Instalando dependências:

- Navegue até a raiz do diretório e execute o comando:
```terminal do VS Code
    pip install -r requirements.txt
```

6. Executando a aplicação

- Navegue até a pasta src dentro dessa pasta raíz através da linha de comando e execute o arquivo 'app.py'.

```terminal do VS Code
    cd src
    python app.py
```  

7. Entrando na aplicação
- Abra o navegador e digite a url que aparecerá no cmd após a execução do 'app.py'.

