from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


class Despesa:
    def __init__(self, descricao, categoria, valor):
        self.descricao = descricao
        self.categoria = categoria
        self.valor = valor


class Investimento:
    def __init__(self, nome, tipo, quantidade, preco_por_cota):
        self.nome = nome
        self.tipo = tipo
        self.quantidade = quantidade
        self.preco_por_cota = preco_por_cota

    def valor_total(self):
        return self.quantidade * self.preco_por_cota


class ControleDespesas:
    def __init__(self):
        self.despesas = []

    def adicionar_despesas(self, despesa):
        self.despesas.append(despesa)

    def listar_despesas(self):
        if not self.despesas:
            console.print("[red]Nenhuma despesa cadastrada.[/]")
            return

        tabela = Table(title="Despesas Cadastradas", expand=True)

        tabela.add_column("#", justify="center", style="cyan")
        tabela.add_column("Descrição", style="yellow")
        tabela.add_column("Categoria", style="magenta")
        tabela.add_column("Valor (R$)", justify="right", style="green")

        for index, despesa in enumerate(self.despesas, 1):
            tabela.add_row(
                str(index),
                despesa.descricao,
                despesa.categoria,
                f"R$ {despesa.valor:.2f}"
            )

        console.print(tabela)


class ControleInvestimentos:
    def __init__(self):
        self.investimentos = []

    def adicionar_investimento(self, investimento):
        self.investimentos.append(investimento)

    def listar_investimentos(self):
        if not self.investimentos:
            console.print("[red]Nenhum investimento cadastrado.[/]")
            return

        tabela = Table(title="Investimentos", expand=True)

        tabela.add_column("#", justify="center", style="cyan")
        tabela.add_column("Nome", style="yellow")
        tabela.add_column("Tipo", style="magenta")
        tabela.add_column("Cotas", justify="center")
        tabela.add_column("Preço por Cota (R$)", justify="right")
        tabela.add_column("Total (R$)", justify="right", style="green")

        for index, inv in enumerate(self.investimentos, 1):
            tabela.add_row(
                str(index),
                inv.nome,
                inv.tipo,
                str(inv.quantidade),
                f"R$ {inv.preco_por_cota:.2f}",
                f"R$ {inv.valor_total():.2f}"
            )

        console.print(tabela)


def menu_titulo(texto):
    console.print(Panel.fit(f"[bold cyan]{texto}[/]", border_style="bright_blue"))


if __name__ == '__main__':
    controle = ControleDespesas()
    controle_inv = ControleInvestimentos()

    while True:
        menu_titulo("SISTEMA DE CONTROLE FINANCEIRO")

        console.print("[1] Adicionar Despesa", style="yellow")
        console.print("[2] Listar Despesas", style="yellow")
        console.print("[3] Adicionar Investimento", style="green")
        console.print("[4] Listar Investimentos", style="green")
        console.print("[5] Sair", style="red")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            menu_titulo("Adicionar Despesa")
            descricao = input('Descrição: ')
            categoria = input('Categoria: ')
            valor = float(input('Valor: R$ '))
            despesa = Despesa(descricao, categoria, valor)
            controle.adicionar_despesas(despesa)
            console.print("[green]Despesa adicionada com sucesso![/]")

        elif opcao == '2':
            menu_titulo("Lista de Despesas")
            controle.listar_despesas()

        elif opcao == '3':
            menu_titulo("Adicionar Investimento")
            nome = input("Nome do investimento: ")
            tipo = input("Tipo (Ação, Fundo, etc): ")
            quantidade = float(input("Quantidade de cotas: "))
            preco = float(input("Preço por cota: R$ "))
            investimento = Investimento(nome, tipo, quantidade, preco)
            controle_inv.adicionar_investimento(investimento)
            console.print("[green]Investimento adicionado com sucesso![/]")

        elif opcao == '4':
            menu_titulo("Lista de Investimentos")
            controle_inv.listar_investimentos()

        elif opcao == '5':
            console.print("[bold red]Finalizando...[/]")
            break

        else:
            console.print("[bold red]Opção inválida! Tente novamente.[/]")
