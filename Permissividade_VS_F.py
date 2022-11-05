import math
import matplotlib.pyplot as plt
import numpy as np

f = (10 ** 9)
er = (4.4)
c = (3 * 10 ** 8)
h = (1.54 * 10 ** -3)
u = (1.26 * 10 ** -6)
e = (8.85 * 10 ** -12)
l = ()
w = ()
deltal = ()
vo = ()
fr = ()
lista_fr = []
lista_er = []


def calcula_w(f, u, e, er):
    w = (1 / (2 * f * math.sqrt(u * e))) * math.sqrt(2 / (er + 1))
    return w


w_calculado = calcula_w(f, u, e, er)


def calcula_deltal(w, h, er):
    deltal = 0.412 * h * ((er + 0.3) * ((w / h) + 0.264)) / ((er - 0.258) * ((w / h) + 0.8))
    return deltal


deltal_calculado = calcula_deltal(w_calculado, h, er)


def calcula_l(f, er, u, e, deltal):
    l = (1 / (2 * f * math.sqrt(er) * math.sqrt(u * e))) - (2 * deltal)
    return l


l_calculado = calcula_l(f, er, u, e, deltal_calculado)


def calcula_vo(w, f, er):
    vo = w * 2 * f / math.sqrt(2 / (er + 1))
    return vo


vo_calculado = calcula_vo(w_calculado, f, er)


def calcula_fr(vo, l, er):
    fr = vo / (2 * l * math.sqrt(er))
    return fr


fr_calculado = calcula_fr(vo_calculado, l_calculado, er)

for er in np.arange(1, 12, 0.5):
    fr_calculado = calcula_fr(vo_calculado, l_calculado, er)
    lista_fr.append(fr_calculado)
    lista_er.append(er)

plt.figure(figsize=(6, 4))
plt.plot(lista_fr, lista_er)
plt.xlabel('Frequência de Ressonância (GHz)')
plt.ylabel('Permissividade Relativa')
plt.grid(True)
plt.savefig('Gráfico_fr_versus_er.png')
plt.show()