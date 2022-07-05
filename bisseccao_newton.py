import math
from this import d #biblioteca de matemática em pyhton
import pandas as pd #modulo para análise de dados

#listas
lx = []
lf = []
f_linha = []
px = [2,-5,-1,3]
p0x = []
p1x = []
p2x = []
p3x = []

def fp0x():
  p0x = px.copy()
  p0x.reverse()
  return p0x
  
def fp2x():
  indice = 0
  indice2 = len(px) - 1
  p2x = fp0x()
  for i in px:
    p2x[indice] = p2x[indice] * math.pow(-1, indice2)
    indice = indice + 1
    indice2 = indice2 - 1
  indice = 0
  if(p2x[0] < 0):
    for i2 in p2x:
      p2x[indice] = p2x[indice] * (-1)
      indice = indice + 1
  return p2x

def fp1x():
  indice = 0
  p1x = px.copy()
  if(p1x[0] < 0):
    for i in p1x:
      p1x[indice] = p1x[indice] * (-1)
      indice = indice + 1
  return p1x

def fp3x():
  indice = 0
  p3x = fp1x()
  for i in px:
      p3x[indice] = p3x[indice] * math.pow(-1, indice)
      indice = indice + 1
  if(p3x[0] < 0):
    indice = 0
    for i in p3x:
      p3x[indice] = p3x[indice] * (-1)
      indice = indice + 1
  return p3x

def calc_k(px):
  indice = len(px) - 1
  k = 0
  for i in px:
    if(px[indice] < 0):
        k = indice
        break
    indice = indice - 1
  return k

def calc_B(px):
  B = 0
  indice = 0
  for i in px:
    if(px[indice] < 0):
      if(px[indice]*(-1) > B):
        B = math.fabs(px[indice])
    indice = indice + 1
  return B

print(calc_k(fp0x()))
def l(px):
  size = len(px) - 1
  return 1 + math.pow(calc_B(px)/px[size], 1/(size-calc_k(px)))

l0 = l(fp0x())
l1 = l(fp1x())
l2 = l(fp2x())
l3 = l(fp3x())

intervalo1 = [1/l1, l0]
intervalo2 = [-l2, -1/l3]
print(intervalo1)
print(intervalo2)

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
m_biseccao(2,3,0.00001)

#Chamando método de newton
dataFN = m_newton(1,0.00001,100)

print(dataFN)
#dataF = pd.DataFrame(list(zip(lx,lf,f_linha)), columns = ['x', 'f(x)', 'f_linha(x)'])
