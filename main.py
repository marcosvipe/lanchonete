from tkinter import *
from classes import *
import random
import time
from datetime import date, timedelta

root = Tk()
root.geometry('1350x750+0+0')
root.title('SISTEMA LANCHONETE QUASE TRÊS LANCHES')
root.configure(background='gray')

# FRAMES PRIMÁRIOS
Tops = Frame(root, width=1350, height=100, bd=9, relief='raise')
Tops.pack(side=TOP)

framef1 = Frame(root, width=900, height=650, bd=8, relief='raise')
framef1.pack(side=LEFT)

framef2 = Frame(root, width=440, height=650, bg='black', bd=8, relief='raise')
framef2.pack(side=RIGHT)

# FRAMES SECUNDÁRIOS
frameftb2 = Frame(framef2, width=440, height=450, bd=2, relief='raise')
frameftb2.pack(side=TOP)

framefb2 = Frame(framef2, width=440, height=250, bd=2, relief='raise')
framefb2.pack(side=BOTTOM)

framef1a = Frame(framef1, width=900, height=330, bd=4, relief='raise', bg='DarkSeaGreen3')
framef1a.pack(side=TOP)

framef2a = Frame(framef1, width=900, height=320, bd=2, relief='raise')
framef2a.pack(side=BOTTOM)

frameft1aa = Frame(framef1a, width=450, height=330, bd=2, relief='raise')
frameft1aa.pack(side=LEFT)

frameft1ab = Frame(framef1a, width=450, height=330, bd=2, relief='raise')
frameft1ab.pack(side=RIGHT)

# CRIANDO FRAMES DO RODAPÉ
framef2aa = Frame(framef2a, width=450, height=800, bd=2, relief='raise')
framef2aa.pack(side=LEFT)

framef2ab = Frame(framef2a, width=450, height=800, bd=2, relief='raise')
framef2ab.pack(side=RIGHT)

frameRodape = Frame(framef2a, width=218, height=800, bd=0, relief='raise')
frameRodape.pack(side=BOTTOM)


# FUNÇÃO VERIFICA SE A ENTRADA DE VALOR NO CAMPO É NUMÉRICA
def ValidaInteiro(num):
    if num.isdigit():
        return True
    elif num == '':
        return True
    else:
        return False


# TROCA A COR DE FUNDO DO FRAME DOS FRAMES
Tops.configure(background='gray')
framef1.configure(background='gray')
frameft1aa.configure(background='DarkSeaGreen3')
frameft1ab.configure(background='DarkSeaGreen3')
framef2a.configure(background='Burlywood3')

framef2aa.configure(background='Burlywood3')
framef2ab.configure(background='Burlywood3')
frameRodape.configure(background='Burlywood3')

# INSERINDO O RÓTULO DO CABEÇALHO COM O TÍTULO
lblInfo = Label(Tops, font=('arial', 30, 'bold'), text='SISTEMA LANCHONETE QUASE TRÊS LANCHES', bd=3, width=55)
lblInfo.grid(row=0, column=0)


# CRIANDO OS MÉTODOS DOS BOTÕES

# CRIANDO O CÓDIGO DO BOTÃO SAIR
def iExit():
    root.destroy()
    return


# CRIANDO O CÓDIGO DO BOTÃO LIMPAR
def Limpar():
    Dataordem.set('')
    txtRecibo.delete("1.0", END)
    Taxaservico.set('')
    SubTotal.set('')
    Total.set('')
    NomeCliente.set('')
    ValorPago.set('')

    C_Calabresa.set('0')
    C_Portuguesa.set('0')
    C_Napolitana.set('0')

    C_Xtudo.set('0')
    C_Xbacon.set('0')
    C_Xespecial.set('0')

    C_Coxinha.set('0')
    C_Pastelao.set('0')
    C_Kibe.set('0')

    txtCalabresa.configure(state=DISABLED)
    txtPortuguesa.configure(state=DISABLED)
    txtNapolitana.configure(state=DISABLED)
    txtXtudo.configure(state=DISABLED)
    txtXbacon.configure(state=DISABLED)
    txtXespecial.configure(state=DISABLED)
    txtCoxinha.configure(state=DISABLED)
    txtPastelao.configure(state=DISABLED)
    txtKibe.configure(state=DISABLED)
    cmdRecibo.configure(state=DISABLED)

    var1.set('0')
    var2.set('0')
    var3.set('0')
    var4.set('0')
    var5.set('0')
    var6.set('0')
    var7.set('0')
    var8.set('0')
    var9.set('0')


# CRIANDO CÓDIGO DO BOTÃO TOTAL E BOTÃO RECIBO
def custoItem():
    subtotal = 0
    taxa = 10
    itensCons = geraDic()
    listaItens = list(itensCons.keys())
    for item in listaItens:
        subtotal += item.getprecoVenda() * itensCons[item]
    Sub_total = round(subtotal,2)
    TaxaCons = round(subtotal * (taxa / 100), 2)
    TotalConta = round(subtotal + TaxaCons, 2)
    Taxaservico.set('R$ ' + str(TaxaCons).replace('.',','))
    SubTotal.set('R$ ' + str(Sub_total).replace('.',','))
    Total.set('R$ ' + str(TotalConta).replace('.',','))
    cmdRecibo.configure(state=NORMAL)

def geraDic():
    Item1 = float(C_Calabresa.get())
    Item2 = float(C_Portuguesa.get())
    Item3 = float(C_Napolitana.get())
    Item4 = float(C_Xtudo.get())
    Item5 = float(C_Xbacon.get())
    Item6 = float(C_Xespecial.get())
    Item7 = float(C_Coxinha.get())
    Item8 = float(C_Pastelao.get())
    Item9 = float(C_Kibe.get())

    calabresa = Pizza(30.00, date.today() + timedelta(1), 0.7, 'Calabresa', 'não', 'molhodetomate')
    portuguesa = Pizza(30.00, date.today() + timedelta(1), 0.7, 'Portuguesa', 'sim', 'molhodetomate')
    napolitana = Pizza(30.00, date.today() + timedelta(1), 0.7, 'Napolitana', 'não', 'molhodetomate')

    pao = ['americano', 'italiano', 'australiano']
    xtudo = Lanche(15.00, date.today() + timedelta(1), 0.5, 'Xtudo', pao, 'puredebatata')
    xbacon = Lanche(13.00, date.today() + timedelta(1), 0.5, 'Xbacon', pao, 'puredebatata')
    xespecial = Lanche(13.00, date.today() + timedelta(1), 0.5, 'Xespecial', pao, 'puredebatata')

    coxinha = Salgadinho(3.5, date.today() + timedelta(1), 0.05, 'Coxinha', 'assado', 'mandioca')
    pastelao = Salgadinho(3.5, date.today() + timedelta(1), 0.05, 'Pastelão', 'assado', 'mandioca')
    kibe = Salgadinho(3.5, date.today() + timedelta(1), 0.05, 'Kibe', 'assado', 'mandioca')

    itensCons = dict()

    if Item1 > 0:
        itensCons[calabresa] = Item1

    if Item2 > 0:
        itensCons[portuguesa] = Item2

    if Item3 > 0:
        itensCons[napolitana] = Item3

    if Item4 > 0:
        itensCons[xtudo] = Item4

    if Item5 > 0:
        itensCons[xbacon] = Item5

    if Item6 > 0:
        itensCons[xespecial] = Item6

    if Item7 > 0:
        itensCons[coxinha] = Item7

    if Item8 > 0:
        itensCons[pastelao] = Item8

    if Item9 > 0:
        itensCons[kibe] = Item9

    return itensCons

def geraRecibo():
    itensCons = geraDic()
    Item10 = str(NomeCliente.get())
    Item11 = str(ValorPago.get()).replace(',','.')

    pedido1 = Pedido('', 10, itensCons)
    fatura = pedido1.mostraFatura(10, itensCons)

    txtRecibo.delete("1.0", END)
    x = random.randint(10747, 500298)
    randomRef = str(x)
    Recibo_Ref.set("CUPOM" + randomRef)
    txtRecibo.insert(END, 'CUPOM Ref:\t\t\t\t' + Recibo_Ref.get() + '\nData:' + Data1.get() + '\t\t\t\tHora:' +
                     Time1.get() + '\n')
    txtRecibo.insert(END, 'Cliente: ' + Item10 + '\n')
    txtRecibo.insert(END, '-------------------------------------------------------------------------------' + '\n')
    txtRecibo.insert(END, 'Ítem: \t\t\t' + 'Quant: \t\t' + 'Valor:' + '\n')
    txtRecibo.insert(END, '-------------------------------------------------------------------------------' + '\n')
    listaItens = list(itensCons.keys())
    for item in listaItens:
        txtRecibo.insert(END, item.getrecheio() + '\t\t\t' +  str(itensCons[item]) + '\t\t' +
                         str(itensCons[item]*item.getprecoVenda()).replace('.',',') + '\n')

    txtRecibo.insert(END, '-------------------------------------------------------------------------------' + '\n')
    txtRecibo.insert(END, 'Sub-Total: \t\t\t R$ ' + str(round(fatura['SubTotal'], 2)).replace('.',',') +'\n')
    txtRecibo.insert(END, 'Taxa: \t\t\t R$ ' + str(round(fatura['TaxaCons'], 2)).replace('.',',') + '\n')
    txtRecibo.insert(END, 'Total: \t\t\t R$ ' + str(round(fatura['TotalConta'], 2)).replace('.',',') + '\n')
    txtRecibo.insert(END, 'Valor Pago: \t\t\t R$ '+ str(round(float(Item11), 2)).replace('.',',') + '\n')
    txtRecibo.insert(END, 'Troco: \t\t\t R$ ' + str(round(float(Item11) - fatura['TotalConta'],2)).replace('.',',') + '\n')
    txtRecibo.insert(END, '-------------------------------------------------------------------------------' + '\n')
    txtRecibo.insert(END, '\t Lanchonete Quase Três Lanches' + '\n')
    txtRecibo.insert(END, '-------------------------------------------------------------------------------' + '\n')


# CRIANDO OS MÉTODOS PARA OS RADIO BUTTONS
def chkCalabresa():
    if (var1.get() == 1):
        txtCalabresa.configure(state=NORMAL)
        C_Calabresa.set('')
    elif (var1.get() == 0):
        txtCalabresa.configure(state=DISABLED)
        C_Calabresa.set('0')

def chkPortuguesa():
    if (var2.get() == 1):
        txtPortuguesa.configure(state=NORMAL)
        C_Portuguesa.set('')
    elif (var2.get() == 0):
        txtPortuguesa.configure(state=DISABLED)
        C_Portuguesa.set('0')

def chkNapolitana():
    if (var3.get() == 1):
        txtNapolitana.configure(state=NORMAL)
        C_Napolitana.set('')
    elif (var3.get() == 0):
        txtNapolitana.configure(state=DISABLED)
        C_Napolitana.set('0')

def chkXtudo():
    if (var4.get() == 1):
        txtXtudo.configure(state=NORMAL)
        C_Xtudo.set('')
    elif (var4.get() == 0):
        txtXtudo.configure(state=DISABLED)
        C_Xtudo.set('0')

def chkXbacon():
    if (var5.get() == 1):
        txtXbacon.configure(state=NORMAL)
        C_Xbacon.set('')
    elif (var5.get() == 0):
        txtXbacon.configure(state=DISABLED)
        C_Xbacon.set('0')

def chkXespecial():
    if (var6.get() == 1):
        txtXespecial.configure(state=NORMAL)
        C_Xespecial.set('')
    elif (var6.get() == 0):
        txtXespecial.configure(state=DISABLED)
        C_Xespecial.set('0')

def chkCoxinha():
    if (var7.get() == 1):
        txtCoxinha.configure(state=NORMAL)
        C_Coxinha.set('')
    elif (var7.get() == 0):
        txtCoxinha.configure(state=DISABLED)
        C_Coxinha.set('0')

def chkPastelao():
    if (var8.get() == 1):
        txtPastelao.configure(state=NORMAL)
        C_Pastelao.set('')
    elif (var8.get() == 0):
        txtPastelao.configure(state=DISABLED)
        C_Pastelao.set('0')

def chkKibe():
    if (var9.get() == 1):
        txtKibe.configure(state=NORMAL)
        C_Kibe.set('')
    elif (var9.get() == 0):
        txtKibe.configure(state=DISABLED)
        C_Kibe.set('0')


# DECLARANDO AS PRIMEIRAS VARIÁVEIS
C_Calabresa = StringVar()
C_Portuguesa = StringVar()
C_Napolitana = StringVar()
C_Xtudo = StringVar()
C_Xbacon = StringVar()
C_Xespecial = StringVar()
C_Coxinha = StringVar()
C_Pastelao = StringVar()
C_Kibe = StringVar()
Time1 = StringVar()
Data1 = StringVar()

Data1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()


# SETANDO AS VARIÁVEIS
C_Calabresa.set('0')
C_Portuguesa.set('0')
C_Napolitana.set('0')
C_Xtudo.set('0')
C_Xbacon.set('0')
C_Xespecial.set('0')
C_Coxinha.set('0')
C_Pastelao.set('0')
C_Kibe.set('0')

var1.set('0')
var2.set('0')
var3.set('0')
var4.set('0')
var5.set('0')
var6.set('0')
var7.set('0')
var8.set('0')
var9.set('0')


# VARIÁVEIS DO RODAPÉ
Dataordem = StringVar()
Recibo = StringVar()
SubTotal = StringVar()
Total = StringVar()
NomeCliente = StringVar()
ValorPago = StringVar()
Totalsalgadinhos = StringVar()
Taxaservico = StringVar()
Recibo_Ref = StringVar()


# CRIANDO OS RADIO BUTTONS PARA AS PIZZAS
Calabresa = Checkbutton(frameft1aa, text='Calabresa \t', bg='DarkSeaGreen3', variable=var1, onvalue=1, offvalue=0,
                        width=20,
                        font=('arial', 18, 'bold'), command=chkCalabresa).grid(row=2, sticky=W)

Portuguesa = Checkbutton(frameft1aa, text='Portuguesa \t', bg='DarkSeaGreen3', variable=var2, onvalue=1, offvalue=0,
                         width=20,
                         font=('arial', 18, 'bold'), command=chkPortuguesa).grid(row=3, sticky=W)

Napolitana = Checkbutton(frameft1aa, text='Napolitana \t', bg='DarkSeaGreen3', variable=var3, onvalue=1, offvalue=0,
                         width=20,
                         font=('arial', 18, 'bold'), command=chkNapolitana).grid(row=4, sticky=W)


# CRIANDO OS RADIO BUTTONS PARA OS LANCHES
xtudo = Checkbutton(frameft1ab, text='X-Tudo \t', bg='DarkSeaGreen3', variable=var4, onvalue=1, offvalue=0, width=14,
                    font=('arial', 18, 'bold'), command=chkXtudo).grid(row=1, sticky=W)

Xbacon = Checkbutton(frameft1ab, text='X-Bacon \t', bg='DarkSeaGreen3', variable=var5, onvalue=1, offvalue=0, width=21,
                     font=('arial', 18, 'bold'), command=chkXbacon).grid(row=2, sticky=W)

Xespecial = Checkbutton(frameft1ab, text='X-Especial \t', bg='DarkSeaGreen3', variable=var6, onvalue=1, offvalue=0,
                        width=21,
                        font=('arial', 18, 'bold'), command=chkXespecial).grid(row=3, sticky=W)


# CRIANDO OS RADIO BUTTONS PARA OS SALGADINHOS
Coxinha = Checkbutton(frameft1ab, text='Coxinha \t', bg='DarkSeaGreen3', variable=var7, onvalue=1, offvalue=0, width=14,
                      font=('arial', 18, 'bold'), command=chkCoxinha).grid(row=6, sticky=W)

Pastelao = Checkbutton(frameft1ab, text='Pastelão \t', bg='DarkSeaGreen3', variable=var8, onvalue=1, offvalue=0,
                       width=21,
                       font=('arial', 18, 'bold'), command=chkPastelao).grid(row=7, sticky=W)

Kibe = Checkbutton(frameft1ab, text='Kibe \t', bg='DarkSeaGreen3', variable=var9, onvalue=1, offvalue=0, width=14,
                   font=('arial', 18, 'bold'), command=chkKibe).grid(row=8, sticky=W)


# CRIANDO OS CAMPOS DE PIZZAS
reg = root.register(ValidaInteiro)
txtCalabresa = Entry(frameft1aa, font=('arial', 16, 'bold'), bg='cyan', bd=1, width=11, justify='left',
                     textvariable=C_Calabresa, state=DISABLED)
txtCalabresa.config(validate="key", validatecommand=(reg, '%P'))
txtCalabresa.grid(row=2, column=1)

txtPortuguesa = Entry(frameft1aa, font=('arial', 16, 'bold'), bg='cyan', bd=1, width=11, justify='left',
                      textvariable=C_Portuguesa, state=DISABLED)
txtPortuguesa.config(validate="key", validatecommand=(reg, '%P'))
txtPortuguesa.grid(row=3, column=1)

txtNapolitana = Entry(frameft1aa, font=('arial', 16, 'bold'), bg='cyan', bd=1, width=11, justify='left',
                      textvariable=C_Napolitana, state=DISABLED)
txtNapolitana.config(validate="key", validatecommand=(reg, '%P'))
txtNapolitana.grid(row=4, column=1)


# CRIANDO OS CAMPOS DE LANCHES
txtXtudo = Entry(frameft1ab, font=('arial', 16, 'bold'), bg='cyan', bd=1, width=11, justify='left',
                 textvariable=C_Xtudo, state=DISABLED)
txtXtudo.config(validate="key", validatecommand=(reg, '%P'))
txtXtudo.grid(row=1, column=1)

txtXbacon = Entry(frameft1ab, font=('arial', 16, 'bold'), bg='cyan', bd=1, width=11, justify='left',
                  textvariable=C_Xbacon, state=DISABLED)
txtXbacon.config(validate="key", validatecommand=(reg, '%P'))
txtXbacon.grid(row=2, column=1)

txtXespecial = Entry(frameft1ab, font=('arial', 16, 'bold'), bg='cyan', bd=1, width=11, justify='left',
                     textvariable=C_Xespecial, state=DISABLED)
txtXespecial.config(validate="key", validatecommand=(reg, '%P'))
txtXespecial.grid(row=3, column=1)


# CRIANDO OS CAMPOS DE SALGADINHOS
txtCoxinha = Entry(frameft1ab, font=('arial', 16, 'bold'), bg='cyan', bd=1, width=11, justify='left',
                   textvariable=C_Coxinha, state=DISABLED)
txtCoxinha.config(validate="key", validatecommand=(reg, '%P'))
txtCoxinha.grid(row=6, column=1)

txtPastelao = Entry(frameft1ab, font=('arial', 16, 'bold'), bg='cyan', bd=1, width=11, justify='left',
                    textvariable=C_Pastelao, state=DISABLED)
txtPastelao.config(validate="key", validatecommand=(reg, '%P'))
txtPastelao.grid(row=7, column=1)

txtKibe = Entry(frameft1ab, font=('arial', 16, 'bold'), bg='cyan', bd=1, width=11, justify='left', textvariable=C_Kibe,
                state=DISABLED)
txtKibe.config(validate="key", validatecommand=(reg, '%P'))
txtKibe.grid(row=8, column=1)


# CAMPO DO RECIBO
lblRecibo = Label(frameftb2, font=('arial', 12, 'bold'), text='Recibo do Cliente:', bd=2, anchor='w')
lblRecibo.grid(row=0, column=0, sticky=W)
txtRecibo = Text(frameftb2, width=55, height=36, bg='lemonchiffon', bd=8, font=('arial', 10))
txtRecibo.grid(row=1, column=0)


# CAMPOS DOS BOTÕES
cmdTotal = Button(framefb2, padx=16, pady=1, bg='black', bd=4, fg='green', font=('arial', 12, 'bold'), width=4,
                  text='Total', command=custoItem)
cmdTotal.grid(row=0, column=0)

cmdRecibo = Button(framefb2, padx=16, pady=1, bg='black', bd=4, fg='white', font=('arial', 12, 'bold'), width=4,
                   text='Recibo', command=geraRecibo, state=DISABLED)
cmdRecibo.grid(row=0, column=1)

cmdLimpar = Button(framefb2, padx=16, pady=1, bg='black', bd=4, fg='yellow', font=('arial', 12, 'bold'), width=4,
                   text='Limpar', command=Limpar)
cmdLimpar.grid(row=0, column=2)

cmdSair = Button(framefb2, padx=16, pady=1, bg='black', bd=4, fg='red', font=('arial', 12, 'bold'), width=5,
                 text='Sair', command=iExit)
cmdSair.grid(row=0, column=3)


# CRIANDO OS CAMPOS DO RODAPÉ FRAME DA ESQUERDA

lblNomeCliente = Label(framef2aa, font=('arial', 12, 'bold'), bg='Burlywood3', text='Nome do Cliente:', bd=2)
lblNomeCliente.grid(row=0, column=0, sticky=W)
txtNomeCliente = Entry(framef2aa, font=('arial', 16, 'bold'), bd=1, justify='left', textvariable=NomeCliente)
txtNomeCliente.grid(row=0, column=1)

lblValorPago = Label(framef2aa, font=('arial', 12, 'bold'), bg='Burlywood3', text='Valor Pago:', bd=2)
lblValorPago.grid(row=1, column=0, sticky=W)
txtValorPago = Entry(framef2aa, font=('arial', 16, 'bold'), bd=1, justify='left', textvariable=ValorPago)
txtValorPago.grid(row=1, column=1)

lblCustosalgadinhos = Label(framef2aa, font=('arial', 12, 'bold'), bg='Burlywood3', text='', bd=2)
lblCustosalgadinhos.grid(row=2, column=0, sticky=W)


# CRIANDO OS CAMPOS DO RODAPÉ FRAME DA DIREITA
lblTaxaservico = Label(framef2ab, font=('arial', 12, 'bold'), bg='Burlywood3', text='Taxa Serviços:', bd=2)
lblTaxaservico.grid(row=0, column=0, sticky=W)
txtTaxaservico = Entry(framef2ab, font=('arial', 16, 'bold'), bd=1, justify='left', textvariable=Taxaservico,
                       state=DISABLED)
txtTaxaservico.grid(row=0, column=1)

lblSubtotal = Label(framef2ab, font=('arial', 12, 'bold'), bg='Burlywood3', text='Sub-Total:', bd=2)
lblSubtotal.grid(row=1, column=0, sticky=W)
txtSubtotal = Entry(framef2ab, font=('arial', 16, 'bold'), bd=1, justify='left', textvariable=SubTotal, state=DISABLED)
txtSubtotal.grid(row=1, column=1)

lblTotal = Label(framef2ab, font=('arial', 12, 'bold'), bg='Burlywood3', text='Total:', bd=2)
lblTotal.grid(row=2, column=0, sticky=W)
txtTotal = Entry(framef2ab, font=('arial', 16, 'bold'), bd=1, justify='left', textvariable=Total, state=DISABLED)
txtTotal.grid(row=2, column=1)

lblPizzas = Label(frameft1aa, font=('arial', 12, 'bold'), bg='DarkSeaGreen3', text='Pizzas:', bd=2)
lblPizzas.grid(row=1, column=0, sticky=W)
lblespacoframe = Label(frameft1aa, font=('arial', 18, 'bold'), bg='DarkSeaGreen3', text='', bd=2, height=5)
lblespacoframe.grid(row=5, column=0, sticky=W)

lblLanches = Label(frameft1ab, font=('arial', 12, 'bold'), bg='DarkSeaGreen3', text='Lanches:', bd=2)
lblLanches.grid(row=0, column=0, sticky=W)

lblSalgadinhos = Label(frameft1ab, font=('arial', 12, 'bold'), bg='DarkSeaGreen3', text='Salgadinhos:', bd=2)
lblSalgadinhos.grid(row=5, column=0, sticky=W)

root.mainloop()
