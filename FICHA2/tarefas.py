import os

tarefas = []

while True:
    os.system("clear")  

    print("=== GESTOR DE TAREFAS (COMPLETO) ===")
    print("1- Ver lista de tarefas")
    print("2- Adicionar tarefa")
    print("3- Adicionar tarefa em posição específica")
    print("4- Remover tarefa por nome")
    print("5- Remover última tarefa")
    print("6- Remover todas as tarefas (Limpar)")
    print("7- Contar ocorrências de uma tarefa")
    print("8- Encontrar índice de uma tarefa")
    print("9- Ordenar tarefas (Ordem Alfabética)")
    print("10- Inverter ordem das tarefas")
    print("11- Copiar lista de tarefas (Backup)")
    print("0- Sair")
    print("====================================")

    resposta = input("Insira o número: ")

    if resposta == "1":
        print("\n--- Lista de Tarefas ---")
        if not tarefas:
            print("A lista está vazia!")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f"{i}: {tarefa}")
        input("\nPressione Enter para continuar...")

    elif resposta == "2":
        nova_tarefa = input("\nDigite a nova tarefa: ")
        tarefas.append(nova_tarefa)
        print(f"Tarefa '{nova_tarefa}' adicionada!")
        input("\nPressione Enter para continuar...")

    elif resposta == "3":
        nova_tarefa = input("\nDigite a tarefa: ")
        posicao = int(input(f"Digite a posição (0 a {len(tarefas)}): "))
        if 0 <= posicao <= len(tarefas):
            tarefas.insert(posicao, nova_tarefa)
            print(f"Tarefa inserida na posição {posicao}!")
        else:
            print("Posição inválida!")
        input("\nPressione Enter para continuar...")

    elif resposta == "4":
        nome_tarefa = input("\nDigite o nome exato da tarefa a remover: ")
        if nome_tarefa in tarefas:
            tarefas.remove(nome_tarefa)
            print(f"Tarefa '{nome_tarefa}' removida!")
        else:
            print("Tarefa não encontrada!")
        input("\nPressione Enter para continuar...")

    elif resposta == "5":
        if tarefas:
            removida = tarefas.pop()
            print(f"Última tarefa '{removida}' removida!")
        else:
            print("A lista já está vazia!")
        input("\nPressione Enter para continuar...")

    # 6. Remover todas as Tarefas
    elif resposta == "6":
        tarefas.clear()
        print("\nLista totalmente limpa com sucesso!")
        input("\nPressione Enter para continuar...")

    # 7. Contar Ocorrências de Tarefa
    elif resposta == "7":
        busca = input("\nDigite a tarefa que quer contar: ")
        quantidade = tarefas.count(busca)
        print(f"A tarefa '{busca}' aparece {quantidade} vez(es) na lista.")
        input("\nPressione Enter para continuar...")

    # 8. Encontrar Índice de Tarefa
    elif resposta == "8":
        busca = input("\nDigite a tarefa para localizar o índice: ")
        if busca in tarefas:
            indice = tarefas.index(busca)
            print(f"A primeira ocorrência de '{busca}' está na posição: {indice}")
        else:
            print("Tarefa não encontrada na lista.")
        input("\nPressione Enter para continuar...")

    # 9. Ordenar Tarefas
    elif resposta == "9":
        tarefas.sort()
        print("\nTarefas ordenadas por ordem alfabética!")
        input("\nPressione Enter para continuar...")

    # 10. Inverter Ordem das Tarefas
    elif resposta == "10":
        tarefas.reverse()
        print("\nA ordem das tarefas foi invertida!")
        input("\nPressione Enter para continuar...")

    # 11. Copiar Lista de Tarefas
    elif resposta == "11":
        copia_tarefas = tarefas.copy()
        print(f"\nCópia de segurança criada com sucesso!")
        print(f"Original: {tarefas}")
        print(f"Cópia (Independente): {copia_tarefas}")
        input("\nPressione Enter para continuar...")

    elif resposta == "0":
        print("\nA sair do programa...")
        break
        
    else:
        print("\nOpção inválida!")
        input("\nPressione Enter para tentar novamente...")
