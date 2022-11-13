# Simulador de dados

import random #biblioteca para valores aleatórios

class Simulador: #classe para simular valor do dado
    def __init__(self):
        self.valor_min = 1 #valor minimo
        self.valor_max = 6 #valor máximo
        self.mensagem = 'Gerar novo valor pro dado: ' #entrada de dados onde se é solicitado ao usuario 

    def Iniciar(self): #função iniciar que iniciar a rodada
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's': #solicitando resposta sim ou não com o if else
                self.ValorDoDado()
            elif resposta == 'não' or resposta == 'n':
                print('Obrigado por jogar nosso jogo')
            else:
                print('Por favor digite uma opção válida')
        except:
            print('ERRO!') #mensagem de exessão

    def ValorDoDado(self):
        print(random.randint(self.valor_min, self.valor_max)) #gerando valor aleatório
#com base no minimo e maximo
simulador = Simulador() #chamada da classe
simulador.Iniciar() #chamada da função iniciar com o objeto simulador