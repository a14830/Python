# Crie uma função que receba o nome do produto, o preço e o iva e guarde a
# informação em um dicionário onde as chaves serão product, price e tax. A função
# deve ser denominada add.


def add( id: int, titulo, autor ):
    return {
        "Id": id,
        "Titulo": titulo,
        "Autor": autor
    }
    


# Crie uma função que permita incluir em um dicionário uma nova chave
# ‘final_price’ que calcule o seu preço final (price * (1+tax)).


def update_livraria(d):
    d["final_livraria"] = d["id"] ["titulo"] ["Autor"]


def print_livraria(d):
    print("========================================")
    print("          LIVRO CADASTRADO           ")
    print("========================================")
    return f"O Livro tem o id {d["id"]} com o titulo {d["titulo"]} e o autor O Livro tem o id {d["autor"]}

def menu():
        print("\n========================================")
        print("          SISTEMA DE PRODUTOS           ")
        print("========================================")
        print(" [1] Inserir um novo produto")
        print(" [2] Listar os produtos existentes")
        print(" [3] Atualizar o preço final de todos os produtos")
        print(" [4] Imprimir os dados de um produto específico")
        print(" [5] Terminar a aplicação")
        print("========================================\n")
        
        opcao = input("Escolha uma opção (1-5): ")
        return opcao