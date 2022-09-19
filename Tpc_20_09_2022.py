import sys
a = int(input('Primul numar:'))
b = int(input('Al doilea numar:'))

#A. Suma numerelor
def suma(x, y):
    s = a + b
    return s
print("A. Suma numerelor", suma(a, b))

#B. Produsul numerelor
def produs(x, y):
    p = a * b
    return p
print("B. Produsul numerelor", produs(a, b))

#C. Media aritmetica
def med_aritmetica(x, y):
    m = (x+y)/2
    return m
print("C. Media aritmetica", med_aritmetica(a, b))

#D. Cel mai mare divizor comun
def cmmdc(x, y):
    i = 1
    while (i<=x) and (i<=y):
        if (x%i==0) and (y%i==0):
            div_com = i
        i = i+1
    return div_com
print("D. Cel mai mare divizor comun", cmmdc(a, b))

#E. Cel mai mic multiplu comun
def cmmmc(x, y):
    return int((x/cmmdc(x, y))*y)
print("E. Cel mai mic multiplu comun", cmmmc(a, b))

#F. Numarul minim
def minim(x, y):
    if x<y:
        return x
    else: return y
print("F. Numarul minim", minim(a, b))

#G. Numarul maxim
def maxim(x, y):
    if x>y:
        return x
    else: return y
print("F. Numarul maxim", maxim(a, b))

#H. Suma numerelor citite in timpul programului
def suma_locala():
    a = int(input("Dati primul nr:"))
    b = int(input("Dati al doilea nr:"))
    c = a + b
    return c
print("H. Suma numerelor citite in timpul programului", suma_locala())

#I. Produsul numerelor citite in timpul programului
def produsul_local():
    k = int(input("Dati primul termen:"))
    l = int(input("Dati al doilea termen:"))
    c = k * l
    return c
print("I. Produsul numerelor citite in timpul programului", produsul_local())

#J. Toti divizorii
def toti_divizorii(x, y):
    divizori1 = []
    divizori2 = []
    for i in range(1, x+1):
        if x%i==0:
            divizori1.append(i)
    for i in range(1, y+1):
        if y%i==0:
            divizori2.append(i)
    return divizori1, divizori2
print("J. Toti divizorii", toti_divizorii(a, b))

#K. Cinci multipli comuni
def multipli_comuni(x, y):
    mul_com1 = []
    mul_com2 = []
    for i in range(1,21):
        m = i*x
        mul_com1.append(int(m))
    for i in range(1,21):
        n = i*y
        mul_com2.append(int(n))
    mul_com = list(set(mul_com1+mul_com2))
    mul_com = mul_com[0:5]
    return mul_com
print("K. Cinci multipli comuni", multipli_comuni(a, b))

#L. Cifrele care se contin in ambele numere
def cifre(x, y):
    l1 = set(map(int, str(x)))
    l2 = set(map(int, str(y)))
    l = l1.intersection(l2)
    return l
print("L. Cifrele care se contin in ambele numere", cifre(a, b))

#M. Cifrele care sunt in primul numar, dar nu sunt in al doilea
def cifre_nr(x, y):
    l1 = list(map(int, str(x)))
    l2 = list(map(int, str(y)))
    for i in range(len(l1)+1):
        if i in l2:
            l1.remove(i)
    return l1
print("M. Cifrele care sunt in primul numar, dar nu sunt in al doilea", cifre_nr(a, b))

#N. Numere prietene
def prietene(x, y):
    divizori1 = []
    divizori2 = []
    for i in range(1, x+1):
        if x%i==0:
            divizori1.append(i)
    for i in range(1, y+1):
        if y%i==0:
            divizori2.append(i)
    if len(divizori1)==len(divizori2):
        n = "PRIETENE"
    return n
print("N. Numere prietene", prietene(a, b))