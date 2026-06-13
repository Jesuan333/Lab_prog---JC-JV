import random
import customtkinter as ctk

janela = ctk.CTk()

janela.title("Jogo de advinhação")
janela.geometry("1000x500")  # fix 1: "x" em vez de ", "

titulo = ctk.CTkLabel(janela, text='Menu inicial', font=("Black Ops One", 24))
titulo.pack(pady=20)
numb_user = 0

def chutes():
    
    numb = random.randint(1, 100)
    chutes = []
    
    nome = input('Insira o nome ou número do desfiante: ')
    nomes = []
    nomes.append(nome)
    
    while True:  
        global numb_user
        numb_user = int(input("Insira um chute: ")) 

        if valor > numb:
            print('O número é menor que esse.')
            chutes.append(numb_user)

        elif numb_user < numb:
            print('O número é maior que esse.')
            chutes.append(numb_user)

        else:  # acertou
            print('Parabéns', nome, 'você conseguiu achar o número!')
            print('Total de tentativas:', len(chutes) + 1)
            print('Seus chutes:', chutes)

def prox_jogador():
    resposta = input('Deseja jogar novamente? (s ou n): ')  

    while True:  # fix 5: while True em vez de while resposta == 's'
        if resposta == 's':
            numb = random.randint(1, 100)
            chutes = []
            nome = input('Insira o nome ou número do desafiante: ')
            nomes = []
            nomes.append(nome)
            
            print("Bem vindo!", nome, "tente adivinhar o número entre 1 e 100.")
            return  # encerra a função
        elif resposta == 'n':
            print("Obrigado por jogar!")
            break  # sai do loop de resposta, continua o jogo
        else:
            print('Erro, digite novamente')
            resposta = input('Deseja jogar novamente? (s ou n): ')
        
                    
def encerrarsessao():
    janela.destroy()


def salva_numb():
    global valor
    valor = int(input_chute.get())
    

input_chute = ctk.CTkEntry(janela, placeholder_text="Digite seu seu chute")
input_chute.pack(pady=10)

botao_insereresp = ctk.CTkButton(janela, text="Salvar", command=salva_numb)
botao_insereresp.pack(pady=10)

janela.mainloop()
    
botao_iniciar = ctk.CTkButton(janela, text='Iniciar jogo', font =("Black Ops One", 12), command=jogo)  
botao_iniciar.pack(pady=20)


botao_encerrasessao = ctk.CTkButton(janela, text='Encerrar Sessão', command= encerrarsessao)
botao_encerrasessao.pack(pady=100)



janela.mainloop() 