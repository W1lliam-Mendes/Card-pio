PRECOS_HAMBURGUERES = {
    1: ("X Salada",      22),
    2: ("X Burguer",     24),
    3: ("X Egg",         26),
    4: ("Smash Burguer", 28),
}

PRECOS_REFRIGERANTES = {
    1: ("Coca Lata",        8),
    2: ("Fanta Lata",       8),
    3: ("Coca-Cola 2L",    14),
    4: ("Fanta Laranja 2L", 14),
}

PRECOS_MOLHOS = {
    1: ("Maionese Caseira", 2),
    2: ("Ketchup",          2),
    3: ("Mostarda",         2),
}

FRETE = {
    1: ("Dentro de Criciúma", 5),
    2: ("Fora de Criciúma",  10),
}

DESCONTO_MINIMO  = 50
DESCONTO_PERCENT = 0.10

def ler_int(mensagem: str) -> int:
    """Lê um inteiro do usuário, repetindo até receber entrada válida."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("  ⚠  Digite apenas números, por favor.")


def escolher_item(opcoes: dict, titulo: str, ultima_opcao: str) -> tuple[int, int]:
    """
    Exibe um menu, pede a escolha e a quantidade.
    Retorna (preco_unitario, quantidade). Retorna (0, 0) se o usuário recusar.
    """
    print(f"\n### {titulo} ###")
    for num, (nome, preco) in opcoes.items():
        print(f"  {num}. {nome:<22} R$ {preco:.2f}")
    ultimo_num = max(opcoes) + 1
    print(f"  {ultimo_num}. {ultima_opcao}")

    while True:
        escolha = ler_int("\nEscolha uma opção: ")
        if escolha == ultimo_num:
            print("  Ok!\n")
            return 0, 0
        if escolha in opcoes:
            nome, preco = opcoes[escolha]
            quantidade = ler_int(f"Quantos(as) '{nome}' você quer? ")
            if quantidade <= 0:
                print("  ⚠  Quantidade inválida, tente novamente.")
                continue
            print(f"  ✔  {quantidade}x {nome} adicionado(a) ao carrinho!\n")
            return preco, quantidade
        print("  ⚠  Opção inválida, tente novamente.")


def escolher_frete() -> int:
    """Exibe as opções de frete e retorna o valor escolhido."""
    print("\n### Endereço de Entrega ###")
    for num, (descricao, valor) in FRETE.items():
        print(f"  {num}. {descricao:<25} R$ {valor:.2f}")

    while True:
        escolha = ler_int("\nQual seu endereço? ")
        if escolha in FRETE:
            descricao, valor = FRETE[escolha]
            print(f"  ✔  Frete para '{descricao}' adicionado ao carrinho!\n")
            return valor
        print("  ⚠  Opção inválida, tente novamente.")

def main() -> None:
    print("\n" + "=" * 38)
    print("       BEM-VINDO À HAMBURGUERIA!")
    print("=" * 38 + "\n")

    carrinho: float = 0.0

    preco, qtd = escolher_item(PRECOS_HAMBURGUERES, "Hambúrgueres", "Não quero nenhum")
    carrinho += preco * qtd

    preco, qtd = escolher_item(PRECOS_REFRIGERANTES, "Refrigerantes", "Não quero nenhum")
    carrinho += preco * qtd

    preco, qtd = escolher_item(PRECOS_MOLHOS, "Molhos", "Não quero nenhum")
    carrinho += preco * qtd

    carrinho += escolher_frete()

    print("=" * 38)
    if carrinho > DESCONTO_MINIMO:
        desconto = carrinho * DESCONTO_PERCENT
        carrinho -= desconto
        print(f"  🎉 Pedido acima de R$ {DESCONTO_MINIMO:.2f}!")
        print(f"     Desconto de 10% aplicado: -R$ {desconto:.2f}")

    print(f"\n  💰 Total do pedido: R$ {carrinho:.2f}")
    print("=" * 38)
    print("\n  Obrigado pelo pedido! Bom apetite! 🍔\n")


if __name__ == "__main__":
    main()