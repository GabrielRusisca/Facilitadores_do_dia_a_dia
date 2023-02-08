import os
from time import sleep
import threading as th



def perg(txt= '\n- Qualquer tecla para reiniciar o alarme\n- 9991 para sair do temporizador\nDIGITE: \n'):
    try:
        global decision
        decision = 2
        valor = int(input(txt))
        if valor != 9991:
            raise ValueError
        decision = 1
    except ValueError:
        decision = 0


def main(tempo=300):
    file = r"C:\Users\grusi\Gabriel\Programacao\MeusProjetos\Mini_Programas\Alarme_da_animação_e_imagens\Alarme_imagens_AI.mp3"
    while True:
        sleep(tempo)
        t = th.Thread(target= perg)
        t.start()
        while True:
            if decision == 0:
                break
            elif decision == 1:
                print('\nTemporizador encerrado!')
                force_close_music_program()
                exit()
            os.system(f"{file}")
            sleep(31)            



def imagens_AI():
    tempo = int(input('\nDuração do temporizador: '))
    ai = th.Thread(target= main,args=[tempo])
    ai.start()


def force_close_music_program():
    os.system('taskkill /IM Music.UI.exe /F')

if __name__ == '__main__':
    main()