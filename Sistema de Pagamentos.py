print(f'{" Lojas do Mário ":=^40}')

def pagamento():
    preco = float(input("Preço da compra: R$ "))

    print("""
FORMAS DE PAGAMENTO

[1] - À vista (dinheiro - 10% de desconto)
[2] - À vista (cartão - 5% de desconto)
[3] - 2x no cartão
[4] - 3x ou mais no cartão (10% de juros)
""")

    opção = int(input("Qual a opção? "))

    if opção == 1:
        total = preco - (preco * 10 / 100)
        print(f"O valor final da sua compra é R${total:.2f}")
    elif opção == 2:
        total = preco - (preco * 5 / 100)
        print(f"O valor final da sua compra é R${total:.2f}")
    elif opção == 3:
        total = preco
        parcela = preco / 2
        print(f"Sua compra será parcelada em 2x de R${parcela}")
        print(f"O valor final da sua compra é R${total:.2f}")
    elif opção == 4:
        total = preco + (preco *20 / 100)
        tot_parcelas = int(input("Em quantas vezes você quer dividir? "))
        parcela = total / tot_parcelas
        print(f"Sua compra será parcelada em {tot_parcelas} vezes de R${parcela:.2f}")
        print(f"O valor final da sua compra é R${total:.2f}")
    else:
        print("OPÇÃO INVÁLIDA!")

    def again():
        pag_again = input("""
    Deseja tentar novamente? 'S' para SIM ou 'N' para NÂO
    """)
        if pag_again.upper() == "S":
            pagamento()
        elif pag_again.upper() == "N":
            print("Ok, obrigado")
        else:
            again()

pagamento()
