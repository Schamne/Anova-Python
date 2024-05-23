import tkinter as tk
from tkinter import ttk
from openai import OpenAI
import os

Chave_API = os.getenv('OPEN_AI_KEY')

#Interface do Chat
class Interface:
    def __init__(self, window_principal):
        self.window_principal = window_principal

        #Título da Janela
        window_principal.title('Chatbot')

        #Cor do Fundo
        window_principal.configure(bg='#000000')

        #Tela do Chat
        self.tela_do_chat = tk.Frame(window_principal, bg='#000000')
        self.tela_do_chat.pack(padx=10, pady=10)

        #Texto dentro da Tela do Chat
        self.texto_do_chat = tk.Text(self.tela_do_chat, height=20, width=50, bg='white', bd=0, wrap='word', font=('Times New Roman*', 11))
        self.texto_do_chat.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        #Barra de Rolagem
        self.barra_de_rolagem = tk.Scrollbar(self.tela_do_chat, command=self.texto_do_chat.yview)
        self.barra_de_rolagem.pack(side=tk.RIGHT, fill=tk.Y)
        self.texto_do_chat.config(yscrollcommand=self.barra_de_rolagem.set)

        #Campo da Pergunta
        self.campo_pergunta = tk.Frame(window_principal, bg='#000000')
        self.campo_pergunta.pack(padx=10, pady=10, fill=tk.X)

        #Texto/Input da Pergunta
        self.input_pergunta = ttk.Entry(self.campo_pergunta, width=5, font=('Times New Roman', 11))
        self.input_pergunta.pack(side=tk.LEFT, fill=tk.X, expand=True)

        #Botão de Enviar
        self.botao_enviar = ttk.Button(self.campo_pergunta, text='Enviar', command=self.enviar_pergunta)
        self.botao_enviar.pack(side=tk.RIGHT)

        self.chatbot = OpenAI(api_key = Chave_API)

    def enviar_pergunta(self):
        pergunta = self.input_pergunta.get()
        self.texto_do_chat.insert(tk.END, 'Você: {}\n'.format(pergunta), 'user')


        #Parâmetros do Bot
        comportamento_chatbot = 'Você é um assistente virtual amigável de uma empresa de tecnologia e deve auxiliar os usuários com as suas dúvidas.'

        conclusao = self.chatbot.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': comportamento_chatbot},
                {'role': 'user', 'content': pergunta}],
            
            #Índice de Aleatoriedade do Bot, varia de 0 a 2
            temperature=1,

            #Quantidade máxima de Tokens utilizados para gerar a Resposta, 1 Token é aproximadamente igual a 4 caracteres
            max_tokens=256,

            top_p=1,

            #Quanto maior este valor, mais penaliza o bot por se repetir verbalmente, varia de 0 a 2
            frequency_penalty=0,

            #Quanto maior este valor, mais penaliza o bot por se manter no mesmo assunto, varia de 0 a 2
            presence_penalty=0

        )

        #Filtrar a resposta no JSON
        resposta = conclusao.choices[0].message.content
        self.texto_do_chat.insert(tk.END, 'Chatbot: {}\n\n'.format(resposta), 'chatbot')
        #Limpar input
        self.input_pergunta.delete(0, tk.END)
def main():

    root = tk.Tk()

    #Tamanho da Janela do Chat
    root.geometry('300x420')

    #Pode Redimensionar a janela?
    root.resizable(False, False)

    gui = Interface(root)
    gui.texto_do_chat.tag_configure('user', foreground='black', font=('Arial', 11, 'bold'))
    gui.texto_do_chat.tag_configure('chatbot', foreground='#0D47A1', font=('Arial', 11, 'bold'))

    root.mainloop()

if __name__ == '__main__':
    main()
