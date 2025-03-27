import json
from json.decoder import JSONDecodeError

import os
from time import sleep

## Utilizar variaveis globais não é muito recomendado, mas decidi utilizar já que a lista será modifica o tempo todo, e os dados serão salvos rapidamente


tarefas = []
desfeitos = []

caminho_JSON = r"C:\Users\Herick\Desktop\Exercicios\exercicios_udemy\Python\lista_de_tarefas_com_json\tarefas.json"

def carregar():
    global tarefas
    try:
        with open(caminho_JSON, "r", encoding="utf-8") as arquivo:
            carregado = json.load(arquivo)
            tarefas = carregado
            return
    except JSONDecodeError:
        return []
    
    except FileNotFoundError:
        criar()


def criar():
    global tarefas
    with  open(caminho_JSON, "x", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo)
        return

        
def salvar():
    global tarefas
    try:
        with open(caminho_JSON, "w", encoding="utf-8") as arquivo:
            json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)
    except JSONDecodeError:
        print("\nNão foi possível salvar")
        sleep(0.5)


def desfazer():
    global tarefas
    global desfeitos
    
    try:
        desfeitos.append(tarefas[-1])
        tarefas.pop()
    except IndexError:
        print("\nNão há tarefas para desfazer")
        sleep(0.5)


def refazer():
    global tarefas
    global desfeitos
    
    try:
        tarefas.append(desfeitos[-1])
        desfeitos.pop()
        
    except IndexError:
        print("\nNão há tarefas para refazer")
        sleep(0.5)


def listar():
    global tarefas  
        
    if len(tarefas) == 0:
        print("\nNÃO HÁ TAREFAS PARA LISTAR.")
        sleep(0.5)
        
    print("------------------TAREFAS----------------")
    for c in tarefas:
        print("\t"+c)
    print("-" * 40)
    print()
        


def adicionar(tarefa):
    global tarefas
    
    if tarefa not in tarefas:
        tarefas.append(tarefa)
        return
    
    print(f"\na tarefa {tarefa} já está presente na sua lista 😉\n")
    sleep(1.2)
    
    
def remover_tarefa():
    global tarefas
    clear()
    listar()
    
    
    while True:
        try:
            remover = str(input("Qual tarefa deseja remover? "))
            
            indice = tarefas.index(remover)
            
            tarefas.pop(indice)
        except ValueError:
            print("O item não está presente na lista.")
            sleep(1)
            
            continue
        
        return

def clear():
    os.system("cls")

carregar()

while True:

    executar = str(input("\nComandos (desfazer, refazer, listar, clear, remover tarefa)\n\n Digite um comando ou tarefa:"))
    print()
    comando = {"remover tarefa" : lambda: remover_tarefa(),
               "adicionar" : lambda: adicionar(tarefa=executar),
               "desfazer" : lambda: desfazer(),
               "refazer" : lambda: refazer(),
               "listar" : lambda: listar(),
               "clear" : clear
               }
    

    comando.get(executar)() if executar in comando else comando["adicionar"]()
    clear()
    salvar()
    listar()

