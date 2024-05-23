
# Projeto Tkinter OpenAI Chatbot

Este é um simples ChatBot desenvolvido em Python que utiliza a biblioteca Tkinter para a interface gráfica e a API da OpenAI para processar as perguntas dos usuários e fornecer respostas. O programa permite que os usuários insiram perguntas e obtenham respostas da API da OpenAI através de uma interface.

## Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado em sua máquina:

- Python 3.10 +
- Uma chave de API da OpenAI válida

## Instalação

1. **Clone o repositório:**

   ```sh
   git clone https://github.com/Schamne/Anova-Python.git
   cd Anova-Python
   ```


2. **Instale as dependências:**

   ```sh
   pip install openai python-dotenv
   ```

   Nota: A biblioteca `tkinter` geralmente já está incluída com o Python, então você pode não precisar instalá-la explicitamente.

## Configuração

1. **Obtenha uma chave de API da OpenAI:**

   Visite o [site da OpenAI](https://beta.openai.com/signup/) e registre-se para obter uma chave de API.

2. **Configure a chave de API:**

   No arquivo .env, você deve definir sua chave de API da seguinte forma:

   ```python
   OPEN_AI_KEY='SuaChavedeAPI'


   ```


## Uso

1. **Execute o programa:**

   ```sh
   python main.py
   ```

2. **Interaja com a interface:**

   - Uma janela Tkinter será aberta.
   - Digite sua pergunta no campo de entrada.
   - Clique no botão para enviar a pergunta.
   - Aguarde a resposta antes de interagir novamente com a interface.
   - A resposta da API da OpenAI será exibida na interface.

