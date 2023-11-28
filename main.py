
from guizero import App, Text, TextBox, PushButton

from cauculadora import Cal



def desligar():
    app.visible = None



usa = 0
def calcular(tipo,valor):
    global usa

    usa = usa + 1

    cal.set_resposta(int(cauculo.value), tipo)
    var = resp.value + tipo + cauculo.value
    resp.value = var

    cauculo.value = cal.get_resposta()

    print(var)
    print(cal.get_resposta())



def mais():

    valor = int(cauculo.value)
    calcular("+", valor)


def menos():
    valor = int(cauculo.value)
    calcular("-", valor)

def vezes():
    valor = int(cauculo.value)
    calcular("X", valor)


def apagar():
    cal.set_resposta(0, " ")
    resp.value = " "
    cauculo.value = "0"








def numero0():
    if cal.get_uso() == True:
        cauculo.value = "0"
        cal.set_uso(False)
    else:
        cauculo.value = cauculo.value + "0"

def numero1():
    if cal.get_uso() == True:
        cauculo.value = "1"
        cal.set_uso(False)
    else:
        cauculo.value = cauculo.value + "1"

def numero2():
    if cal.get_uso() == True:
        cauculo.value = "2"
        cal.set_uso(False)
    else:
        cauculo.value = cauculo.value + "2"

def numero3():
    if cal.get_uso() == True:
        cauculo.value = "3"
        cal.set_uso(False)
    else:
        cauculo.value = cauculo.value + "3"

def numero4():
    if cal.get_uso() == True:
        cauculo.value = "4"
        cal.set_uso(False)
    else:
        cauculo.value = cauculo.value + "4"

def numero5():
    if cal.get_uso() == True:
        cauculo.value = "5"
        cal.set_uso(False)
    else:
        cauculo.value = cauculo.value + "5"

def numero6():
    if cal.get_uso() == True:
        cauculo.value = "6"
        cal.set_uso(False)
    else:
        cauculo.value = cauculo.value + "6"

def numero7():
    if cal.get_uso() == True:
        cauculo.value = "7"
        cal.set_uso(False)
    else:
        cauculo.value = cauculo.value + "7"

def numero8():
    if cal.get_uso() == True:
        cauculo.value = "8"
        cal.set_uso(False)
    else:
        cauculo.value = cauculo.value + "8"

def numero9():
    if cal.get_uso() == True:
        cauculo.value = "9"
        cal.set_uso(False)
    else:
        cauculo.value = cauculo.value + "9"









cal = Cal()


app = App(title="Calculadora")

cauculo = TextBox(app, width= 50, text="", height= 50)
cauculo.bg = "pink"
cauculo.height = 50
cauculo.text_size = 20

resp = TextBox(app, width= 20, text="00")
resp.bg = "pink"
resp.text_size = 10

desligar = PushButton(app, text = "OFF", command=desligar)
desligar.bg = "#ccff99"
desligar.align = "button"

mais = PushButton(app, text = "+", command=mais)
mais.bg = "#ccff99"
mais.align = "left"

menos = PushButton(app, text = "-", command= menos)
menos.bg = "#ccff99"
menos.align = "left"

vezes = PushButton(app, text = "X", command=vezes)
vezes.bg = "#ccff99"
vezes.align = "left"

apagar = PushButton(app, text = "CC", command=apagar)
apagar.bg = "#ccff99"
apagar.align = "top"





############################################################################################################################################

botao0 = PushButton(app, text="0", command=numero0)
botao0.bg = "#ccff99"
botao0.align = "left"

botao1 = PushButton(app, text="1", command=numero1)
botao1.bg = "#ccff99"
botao1.align = "left"

botao2 = PushButton(app, text="2", command=numero2)
botao2.bg = "#ccff99"
botao2.align = "left"

botao3 = PushButton(app, text="3", command=numero3)
botao3.bg = "#ccff99"
botao3.align = "left"

botao4 = PushButton(app, text="4", command=numero4)
botao4.bg = "#ccff99"
botao4.align = "left"

botao5 = PushButton(app, text="5", command=numero5)
botao5.bg = "#ccff99"
botao5.align = "left"

botao6 = PushButton(app, text="6", command=numero6)
botao6.bg = "#ccff99"
botao6.align = "left"

botao7 = PushButton(app, text="7", command=numero7)
botao7.bg = "#ccff99"
botao7.align = "left"

botao8 = PushButton(app, text="8", command=numero8)
botao8.bg = "#ccff99"
botao8.align = "left"

botao9 = PushButton(app, text="9", command=numero9)
botao9.bg = "#ccff99"
botao9.align = "left"


app.display()

