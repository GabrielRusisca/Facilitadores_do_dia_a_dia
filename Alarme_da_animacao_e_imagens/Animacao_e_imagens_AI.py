from time import sleep
from random import choice
from imagens_AI import imagens_AI

def main():
    e = 'oi'
    path_to_phrases = r"C:\Users\grusi\Gabriel\Programacao\MeusProjetos\Mini_Programas\Alarme_da_animacao_e_imagens\mensagens_positivas.txt"
    while e not in [0,1,2]:
        try:
            e = int(input('Escolha:\n0 - Adicionar uma nova frase\n1 - Colocar mensagens em loop!\n2 - Sair!\nEscolha: '))
        except ValueError:
            print('Escolha corretamente.')
    if e == 1:
        imagens_AI() # Adiciona o temporizador com alarme da imagem
        while True:
            try:
                tempo = int(input('De quanto em quanto tempo deseja que o programa troque a mensagem.\nTempo (em segundos): '))
                break
            except ValueError:
                pass
        msg1 = msg = contador = 0
        with open(path_to_phrases, 'r') as f:
            msgs = f.readlines()
        while True:
            msg = choice(msgs)
            if msg1 == msg:
                continue
            msg1 = msg
            contador += 1
            print('-'*len((str(contador), '-', msg)))
            print(contador, '-', msg[:-1]) # Tirar o \n, por isso [:-1]
            sleep(tempo)
    elif e == 0:
        e = 2
        while e != 1:
            new_msg = input('Digite a sua nova mensagem abaixo ou 9991 para sair do modo "Nova mensagem"\nNova mensagem: ')
            if new_msg == '9991':
                return
            try:
                print('-'*len('Nova mensagem: ' + new_msg))
                e = int(input('Para confirmar a mensagem acima digite 1 ou aperte qualquer outra tecla para digitar de novo.\nEscolha: '))
                if e != 1:
                    raise ValueError
            except ValueError:
                pass 

        new_msg = new_msg + '\n'
        with open(path_to_phrases, 'a') as f:
            f.write(new_msg)
    return None
if __name__ == '__main__':
    while True:
        main()
        try:
            escolha = int(input('Para reiniciar o programa digite 1 ou aperte qualquer outra tecla para sair.\nEscolha: '))
            if escolha != 1:
                raise ValueError
        except ValueError:
            exit()

