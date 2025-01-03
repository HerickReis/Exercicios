lista_tarefas = []
removidos = []


def desfazer(lista_completa= None):
    if not lista_completa:
        print("NENHUMA TAREFA PARA DESFAZER.")
        return
    if lista_completa == None:
        lista_completa = []
        
    removido = lista_completa[-1]
    lista_completa.pop()
    
    return removido, lista_completa


def refazer(lista_completa=None, removidos=None):
    if not lista_completa or removidos:
        print("NENHUMA TAREFA PARA REFAZER.")
        return
    if lista_completa and removidos == None:
        lista_completa, removidos = []
    
    elif lista_completa == None:
        lista_completa = []
    
    elif removidos == None:
        removidos = None
        

    lista_completa.append(removidos[-1])
    removidos.pop()
    
    return lista_completa, removidos
    
    
def listar(lista):
    print("\nTAREFAS:\n")
    if not lista:
        print("NENHUMA TAREFA REGISTRADA")
        return 
    for t in lista:
        print(t, end="\n")


def clear():
    import os
    
    os.system("cls")



while True:
    lista_tarefas
    removidos
    
    entrada = str(input("\nCOMANDOS: (desfazer, refazer, listar, clear)\nDigite um comando ou tarefa : "))
    
    if entrada == "desfazer":
        desfeito = desfazer(lista_tarefas)
        if not desfeito:
            continue
        lista_tarefas = desfeito[1]
        removidos.append(desfeito[0])
        
    elif entrada == "refazer":
        refeito = refazer(lista_tarefas, removidos)
        if not refeito:
            continue
        lista_tarefas = refeito[0]
        removidos = refeito[1]
        
    elif entrada == "listar":
        listar(lista_tarefas)
        
    elif entrada == "clear":
        clear()
        
    else:
        lista_tarefas.append(entrada)
