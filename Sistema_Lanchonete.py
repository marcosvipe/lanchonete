#Sistema de Controle de Lanches
#Lanchonete Quase Três Lanches

# -----------------------        CLASSES        -----------------------
# Classe Pai
class Cardapio:
    __slots__ = ['_precoVenda', '_dataValidade', '_peso', '_recheio']
    #inicializador da classe cliente
    def __init__(self, precoVenda, dataValidade, peso, recheio):
        self._precoVenda = precoVenda
        self._dataValidade = dataValidade
        self._peso = peso
        self._recheio = recheio

    def getprecoVenda(self):
        return self._precoVenda

    def setprecoVenda(self, precoVenda):
        self._precoVenda = precoVenda

    def getdataValidade(self):
        return self._dataValidade

    def setdataValidade(self, dataValidade):
        self._dataValidade = dataValidade

    def getpeso(self):
        return self._peso

    def setpeso(self, peso):
        self._peso = peso

    def getrecheio(self):
        return self._recheio

    def setrecheio(self, recheio):
        self._recheio = recheio

# Classes Filhas
class Pizza(Cardapio):
    __slots__ = ['_bordasRecheadas', '_molho']
    #inicializador da classe cliente
    def __init__(self, precoVenda, dataValidade, peso, recheio, bordasRecheadas, molho):
        super().__init__(precoVenda, dataValidade, peso, recheio)
        self._bordasRecheadas = bordasRecheadas
        self._molho = molho

    def getbordasRecheadas(self):
        return self._bordasRecheadas

    def setbordasRecheadas(self, bordasRecheadas):
        self._bordasRecheadas = bordasRecheadas

    def getmolho(self):
        return self._molho

    def setmolho(self, molho):
        self._molho = molho


class Lanche(Cardapio):
    __slots__ = ['_tipoPao', '_molhos']
    #inicializador da classe cliente
    def __init__(self, precoVenda, dataValidade, peso, recheio, tipoPao, molhos):
        super().__init__(precoVenda, dataValidade, peso, recheio)
        self._tipoPao = tipoPao
        self._molhos = molhos

    def gettipoPao(self):
        return self._tipoPao

    def settipoPao(self, tipoPao):
        self._tipoPao = tipoPao

    def getmolhos(self):
        return self._molhos

    def setmolhos(self, molhos):
        self._molhos = molhos


class Salgadinho(Cardapio):
    __slots__ = ['_tipo', '_massa']
    #inicializador da classe cliente
    def __init__(self, precoVenda, dataValidade, peso, recheio, tipo, massa):
        super().__init__(precoVenda, dataValidade, peso, recheio)
        self._tipo = tipo
        self._massa = massa

    def gettipo(self):
        return self._tipo

    def settipo(self, tipo):
        self._tipo = tipo

    def getmassa(self):
        return self._massa

    def settipo(self, massa):
        self._massa = massa


class Pedido:
    __slots__ = ['_nomeCliente', '_taxaServico', '_itens']
    # inicializador da classe cliente
    def __init__(self, nomeCliente, taxaServico, itens):
        self._nomeCliente = nomeCliente
        self._taxaServico = taxaServico
        self._itens = itens

    def getnomeCliente(self):
        return self._nomeCliente

    def setnomeCliente(self, nomeCliente):
        self._nomeCliente = nomeCliente

    def gettaxaServico(self):
        return self._taxaServico

    def settaxaServico(self, taxaServico):
        self._taxaServico = taxaServico

    def getitens(self):
        return self._itens

    def setitens(self, itens):
        self._itens = itens

# Método de Cálculo da Fatura
    def mostraFatura(self, taxa, it):
        Total = 0
        listaItens = list(it.keys())
        for item in listaItens:
            Total += item.getprecoVenda() * it[item]

        TaxaCons = Total * (taxa/100)
        TotalConta = Total + TaxaCons

        calculaConta = dict()
        calculaConta['TaxaCons'] = TaxaCons
        calculaConta['TotalConta'] = TotalConta
        calculaConta['SubTotal'] = Total
        return calculaConta
