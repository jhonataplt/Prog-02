# Dados dois numeros M e N, imprima o máximo divisor comum entre M e N.

import ex_04

def menor(m,n):
    if m < n:
        return m
    else:
        return n

def mdc(m,n):
    menorNum = menor(m,n)
    while menorNum >= 1:
        if ex_04.divisor(menorNum,m) and ex_04.divisor(menorNum,n):
            print(menorNum)
            return
        menorNum -= 1