import math #biblioteca de matemática em pyhton

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

    i = 1;
    while(math.fabs(f(x0))>err):
        x = x0 - f(x0)/df(x0)
        x0 = x
        i = i + 1
        if(i>=n0):
            print("Raiz não encontrada")
            break 

    if(i<n0):
        print("Raiz %f\nIterações: %f\nf(%f) = %f\n\n"%(x0,i,x0,f(x0)))

#------------------------------------------
#Execução

#Chamando método da bissecção
m_biseccao(2,3,0.00001)

#Chamando método de newton
m_newton(1,0.00001,100)
