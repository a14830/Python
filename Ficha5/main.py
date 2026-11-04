from functions import add, update_final_price, print_products, menu

products = []
escolha = menu()


while True:
    match (escolha):
        case "1":
            prd = input("Digite o nome do produto: ")
            pri = float(input("Digite o preço do produto: "))
            iva = float(input("Iva do produto: "))
            products.append(add(prd,float(pri),float(iva)))
        case "2":
            for product in products:
                if "final_price" not in product.keys():
                    update_final_price(product)
                print(print_products(product))
                input("Pressione Enter para continuar...")
        case "3":
            for product in products:
                update_final_price(products[0])
        case "4":
                encontrei = False
                pesquisa = input("Digite o nome do produto que deseja pesquisar: ")
                for p in products:
                    if p ["product"] == pesquisa:
                        print(print_products(p))
                        encontrei = True
                        if not encontrei:
                            print("Produto não encontrado")
        case "5":
            break
    # os.system("clear")
    escolha = menu()

    

products.append(add("camisa",12.23,0.13))