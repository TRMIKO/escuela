from IPython.core.display import display, HTML


def sumVer(arr):
    res=[]
    for i in range(0,len(arr[0])):
        res.append(0)
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            res[j]=res[j]+arr[i][j]
    return res

def sumHor(arr):
    res=[]
    for i in range(0,len(arr)):
        res.append(0)
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            res[i]=res[i]+arr[i][j]
    return res

def trat(arr2,tot,t):
    cont=0
    total=0
    for i in range(0,len(arr2)):
        cont+=((arr2[i]*arr2[i])/tot)
    for i in range(0,len(arr2)):
        total+=arr2[i]
    return cont-((total*total)/t)

def bloque(arr2,tot,t):
    cont=0
    total=0
    for i in range(0,len(arr2)):
        cont+=(arr2[i]*arr2[i])/tot
    for i in range(0,len(arr2)):
        total+=arr2[i]
    pre=(cont)
    res=((total*total)/t)
    display(HTML("""
       <h4>bloque</h4>
         {}-{}
        
    """.format(pre,res)))
    return cont-((total*total)/t)

def total(arr,arr2,n,k):
    cont=0
    total=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            cont+=(arr[i][j]*arr[i][j])
    for i in range(0,len(arr2)):
        total+=arr2[i]
    pre=(cont)
    res=((total*total)/(n*k))
    display(HTML("""
       <h4>total</h4>
        <ul>
            <li>pre={}</li>
            <li>res={}</li>
            
        </ul>
        
    """.format(pre,res)))
    return cont-((total*total)/(n*k))
def testCuad(arr):
    cont=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            cont+=(arr[i][j]*arr[i][j])
    return cont
def total1d(arr):
    cont=0
    for i in range(0,len(arr)):
        cont=arr[i]
    return cont
def totalDatos(arr):
    cont=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            cont+=1
    return cont

def anovaBloques(tabla):
    ver=sumVer(tabla)
    hor=sumHor(tabla)
    k=len(tabla[0])
    n=len(tabla)
    totalDat=totalDatos(tabla)
    #total=total1d(ver)
    tratamiento=trat(ver,n,totalDat)
    bloq=bloque(hor,k,totalDat)
    tot=total(tabla,ver,n,k)
    error=tot-bloq-tratamiento
    scmtr=tratamiento/(k-1)
    scmb=bloq/(n-1)
    smce=(error)/((n-1)*(k-1))
    #trat(tabla,ver,)
    display(HTML("""
        <ul>
            <li>k={}</li>
            <li>n={}</li>
            <li>total={}</li>
        </ul>
        
    """.format(k,n,totalDat)))
    display(HTML("""
     <ul>
            <li>vertical={}</li>
            <li>horizontal={}</li>
    </ul>
        """.format(ver,hor)))
    
    display(HTML("""
    <table>
  <thead>
    <tr>
      <td>Fuente de variacion</td>
      <td>G.L</td>
      <td>S.C</td>
      <td>S.C.M</td>
      <td>F</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>TRATAMIENTO</td>
      <td>{}</td>
      <td>{}</td>
      <td>{}</td>
      <td>{}</td>
    </tr>
    <tr>
      <td>BLOQUES</td>
      <td>{}</td>
      <td>{}</td>
      <td>{}</td>
      <td>{}</td>
    </tr>
    <tr>
      <td>ERROR</td>
      <td>{}</td>
      <td>{}</td>
      <td>{}</td>
      <td></td>
    </tr>
    <tr>
      <td>TOTAL</td>
      <td>{}</td>
      <td>{}</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

    """.format(k-1,tratamiento,scmtr,scmtr/smce,n-1,bloq,scmb,scmb/smce,(k-1)*(n-1),error,smce,totalDat-1,tot) ))