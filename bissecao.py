import math

#definir um intervalo [a,n] e um erro e
a = 2
b = 3
e = 0.01

#definir uma função
def f(x): 
    return x**2 - 5

#Teorema de Bolzano
#-Verificar se existe raiz nesse intervalo

if(f(a)*f(b)) < 0:
    #enquanto o módulo de b-a / 2 for maior do que o erro, executa o laço 
    while(math.fabs(b-a)/2 > e):
        xi = (a+b)/2
        if(f(xi))==0:
            print("Raiz da função: ", xi)
            break #sai do loop
        else:
            if(f(a)*f(xi)<0):
                b = xi
            else:
                a = xi
    print("Raiz = ", xi)
else:
    print("Não existe raiz neste intervalo!")
