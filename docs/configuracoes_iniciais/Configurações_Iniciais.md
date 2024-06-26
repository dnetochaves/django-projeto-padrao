***Configurações Iníciais (Projeto)***

**Dev: Dmeval Neto**

### **Configurações Iníciais (Projeto)**

- **Configurações Windows/Linux**
    
    Primeiro passo de tudo é ter o python instalado no seu sistema operacional. 
    
    Para Windows:
    
    ```bash
    https://www.python.org/downloads/windows/
    
    Release Stable 3.10.11. 
    
    Atualmente eu uso essa versão no Windows.
    ```
    
    Para Linux:
    
    ```bash
    sudo apt-get update
    
    sudo apt-get install build-essential libssl-dev zlib1g-dev libncurses5-dev \
    libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev \
    libbz2-dev libexpat1-dev liblzma-dev tk-dev libffi-dev
    
    sudo apt-get install python3.10
    sudo apt-get install python3-pip
    
    python3 --version
    python3.10 --version
    ```
    
      
    
    **Git bash para Windows:** https://git-scm.com/downloads
    
    Depois vamos instalar a IDE para começar a programar. Existe varias alternativas, nesse curso vou utilizar o vscode por ser mais facil de usar e gerenciar os plugins.
    
    **Para Windows:**
    
    ```python
    https://code.visualstudio.com/download
    Faça o download e instala normalmente.
    ```
    
    **Para Linux:**
    
    ```python
    Primeira Opção:
    https://code.visualstudio.com/download
    Faça o download para Linux .deb e instala com gerenciador de pacotes do linux.
    
    Segunda Opção:
    Terminal
    sudo wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
    sudo apt-get update
    sudo apt-get install code
    ```
    
   