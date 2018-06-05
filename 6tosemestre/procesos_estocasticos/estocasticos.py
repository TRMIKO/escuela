import numpy as np
def mExp(m,n):
    tmp=m
    for i in range(n-1):
        tmp=tmp@m
    return tmp

def recu(x,y,t,m):
    if t==1:
        return m[x][y]
    res=[]
    sum=0

    for i in range(1,t+1):
        sum=0
        #print("iteracion de ------------------- i {}".format(i))
        #print("longitud {}".format(len(res)))
        for j in range(len(res)):
            sum=sum+(res[j]*mExp(m,len(res)-j)[y][y])
        res.append(mExp(m,i)[x][y]-sum)
    return res
    # print("P{}(T{}={})=".format(x,y,t))
    # print("P^{}({},{}) -".format(t,x,y))
    # for i in range(1,t+1):
    #     print("P{}(T{}={})*P^{}({},{})".format(x,y,i,t-i,y,y))
    #print("p{}(t{}={})=p^{}({},{})".format(x,y,t,t,x,y))
while True:
    print("dame la dimesion de la matriz por ejemplo 2x2")
    while True:
        try:
            r,c=input().split("x")
            break
        except Exception as e:
            print("debes poner ponerlo en la forma mxn")

    mat=np.array([]).reshape(0,int(c))
    print("dame el renglon, por ejemplo 1 2 3 4")
    for i in range(int(r)):
        print("renglon {}".format(i))
        while True:
            try:
                ren=np.array([input().split(" ")]).astype(float)
                print(ren)
                break
            except Exception as e:
                print("oye tranquilo chico , tienes que separarlo por espacios")
        mat=np.vstack((mat,ren))
    # mat = np.array([[.4,.2,.2,.2],
    #                 [.1,.8,.1,.0],
    #                 [0,0,.5,.5],
    #                 [.7,0,.3,0]])

    print(mat)
    print("dame estado inicial")
    x=int(input())
    print("dame y estado final")
    y=int(input())
    print("dame el numero de pasos")
    t=int(input())
    print("el resultado es ")
    print(recu(x,y,t,mat))
    print("desea seguir? s/n")
    if input() == "n":
        break
#print(mExp(mat,3))
