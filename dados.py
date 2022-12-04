# Simulador de dados
import random
#from typing import Self  # biblioteca para valores aleatórios
from PySimpleGUI import PySimpleGUI as sg

class SimuladorDeDados: #classe para simular valor do dado
    def __init__(self):
        self.valor_min = 1 #valor minimo
        self.valor_max = 6 #valor máximo
        self.mensagem = 'Gerar novo valor pro dado: ' #entrada de dados onde se é solicitado ao usuario 
        
        #layout
        sg.theme('DarkAmber')
    
        self.layout = [
            [sg.Text('Gerar Valor?')],
            [sg.Button('sim'),sg.Button('não')]
        ]

        
    def Iniciar(self): #função iniciar que iniciar a rodada
        #criar uma janela
            self.janela = sg.Window('Sistema de dados', layout=self.layout)
        #ler os valores da tela
            self.eventos, self.valores = self.janela.Read()
        
            #while True:
            try:
                if self.eventos == 'sim' or self.eventos == 's': #solicitando resposta sim ou não com o if else
                    self.ValorDeDados()
                elif self.eventos == 'não' or self.eventos == 'n':
                    print('Obrigado por jogar nosso jogo')
                else:
                    print('Por favor digite uma opção válida')
            except:
                print('ERRO!') #mensagem de exessão

    def ValorDeDados(self):
        print(random.randint(self.valor_min, self.valor_max)) #gerando valor aleatório
#com base no minimo e maximo
        simulador = SimuladorDeDados() #chamada da classe
        simulador.Iniciar() #chamada da função iniciar com o objeto simulador