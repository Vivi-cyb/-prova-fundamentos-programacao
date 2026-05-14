# Sistema de Vendas

# Variáveis de controle
total_vendas = 0
valor_total = 0
maior_venda = 0

while True:

    print("\n=== SISTEMA DE VENDAS ===")
    print("1 - Registrar venda")
    print("2 - Ver resumo parcial")
    print("3 - Encerrar sistema")

    opcao = input("Escolha uma opção: ")

    # REGISTRAR VENDA
    if opcao == "1":

        nome_produto = input("Nome do produto: ")

        valor_unitario = float(input("Valor unitário: R$ "))
        quantidade = int(input("Quantidade: "))

        # cálculo do valor bruto
        valor_bruto = valor_unitario * quantidade

        print(f"Valor bruto da venda: R$ {valor_bruto:.2f}")

        # cálculo de desconto
        desconto = 0

        if valor_bruto >= 500:
            desconto = valor_bruto * 0.20

        elif valor_bruto >= 200:
            desconto = valor_bruto * 0.10

        valor_final = valor_bruto - desconto

        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Valor final: R$ {valor_final:.2f}")

        # atualização dos totais
        total_vendas += 1
        valor_total += valor_final

        # maior venda
        if valor_final > maior_venda:
            maior_venda = valor_final

    # RESUMO PARCIAL
    elif opcao == "2":

        print("\n=== RESUMO PARCIAL ===")
        print(f"Quantidade de vendas: {total_vendas}")
        print(f"Valor total vendido: R$ {valor_total:.2f}")
        print(f"Maior venda registrada: R$ {maior_venda:.2f}")

    # ENCERRAR SISTEMA
    elif opcao == "3":

        print("\n=== RELATÓRIO FINAL ===")
        print(f"Total de vendas realizadas: {total_vendas}")
        print(f"Valor total vendido: R$ {valor_total:.2f}")
        print(f"Maior venda registrada: R$ {maior_venda:.2f}")

        print("\nSistema encerrado.")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida. Tente novamente.")