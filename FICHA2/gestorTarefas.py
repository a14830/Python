import os

tarefas = []
resposta = ""

while True:
    # Limpa o ecrã a cada ciclo para o menu ficar organizado
    os.system("clear")  

    print("=== GESTOR DE TAREFAS ===")
    print("1- Ver lista de tarefas")
    print("2- Adicionar tarefa")
    print("3- Adicionar tarefa em posição específica")
    print("4- Remover tarefa por nome")
    print("5- Remover última tarefa")
    print("0- Sair")
    print("=========================")

    # CORREÇÃO 1: Texto direto dentro do input
    resposta = input("Insira o número: ")

    # CORREÇÃO 2: Comparação usando strings ("1" em vez de 1)
    if resposta == "1":
        print("\n--- Lista de Tarefas ---")
        if not tarefas:
            print("A lista está vazia!")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f"{i}: {tarefa}")
        input("\nPressione Enter para continuar...") # Pausa para conseguir ler o ecrã

    elif resposta == "2":
        nova_tarefa = input("\nDigite a nova tarefa: ")
        tarefas.append(nova_tarefa) # CORREÇÃO 3: Usar a variável 'tarefas'
        print(f"Tarefa '{nova_tarefa}' adicionada!")
        input("\nPressione Enter para continuar...")

    elif resposta == "0":
        print("\nA sair do programa...")
        break
        
    else:
        print("\nOpção inválida!")
        input("\nPressione Enter para tentar novamente...")
