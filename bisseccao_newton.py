import math
from this import d #biblioteca de matemática em pyhton
import pandas as pd #modulo para análise de dados

#listas
lx = []
lf = []
f_linha = []

#definir uma função
def f(x): 
    return x**2 - 5

#definir a derivada da função x
def df(x):
    h = 0.000001
    return ((f(x+h) - f(x))/h) # definição de derivada : limite quando h -> 0

def m_biseccao(a,b,e):
    # intervalo [a,b]
    # erro e
    #Teorema de Bolzano
    print("\nMétodo de Bisseção\n")

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
    
def m_newton(x0, err, n0):
    # x0 = aproximação inicial
    # err = erro 
    # n0 = número de iterações
    print("\nMétodo de Newton\n")

    i = 0;
    while(math.fabs(f(x0))>err):
        lx.append(x0)
        lf.append(f(x0))
        f_linha.append(df(x0))

        x = x0 - f(x0)/df(x0)
        x0 = x
        i = i + 1
        if(i>=n0):
            print("Raiz não encontrada")
            break 

    if(i<n0):
        print("Raiz %f\nIterações: %f\nf(%f) = %f\n\n"%(x0,i,x0,f(x0)))
        dataF = pd.DataFrame(list(zip(lx,lf,f_linha)), columns = ['x', 'f(x)', 'f_linha(x)'])
        return dataF

#------------------------------------------
#Execução

#Chamando método da bissecção
m_biseccao(2,3,0.1)

#Chamando método de newton
dataFN = m_newton(1,0.00001,100)

print(dataFN)
#dataF = pd.DataFrame(list(zip(lx,lf,f_linha)), columns = ['x', 'f(x)', 'f_linha(x)'])
