import adivinhacao
import forca

def escolhe_jogo():
    print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_')
    print('**********Escolha o seu jogo!**********')
    print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_')

    print('(1) Forca ou (2) Adivinhação')
    jogo = int(input('Qual jogo? '))

    if jogo == 1:
        print('Jogando Forca')
        forca.jogar()
    elif jogo == 2:
        print('Jogando Adivinhação')
        adivinhacao.jogar()
    else:
        print('Você não escolheu um jogo disponível!')

if __name__ == '__main__':
    escolhe_jogo()