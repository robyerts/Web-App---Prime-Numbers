from myproject import app
from flask import render_template

import math
def checkPrime(x):
    len=(int)(math.floor(math.sqrt(x))+1)
    for i in range(2,len):
        if x%i==0:
            return False
    return True

def firstNprimes(n):
    primes=[]
    for i in range(0,n):
        primes.append(-1)
    if n==0 or n==1:
        return 0
    elif n==2:
        return 1

    primes[0]=0
    primes[1]=0
    primes[2]=1
    for i in range(3,n):
        if primes[i]==-1:
            if checkPrime(i)==False:
                primes[i]=0
            else:
                primes[i]=1
                j=2
                while i*j<n:
                    primes[i*j]=0
                    j=j+1
    return primes;


primeNrIndexes=firstNprimes(1000)

def recomputePrimes(n):
    global primeNrIndexes
    startNumber=len(primeNrIndexes)
    for i in range(startNumber,n):
        primeNrIndexes.append(-1)
    for i in range(3,n):
        if primeNrIndexes[i]==-1:
            if checkPrime(i)==False:
                primeNrIndexes[i]=0
            else:
                primeNrIndexes[i]=1
                j=2
                while i*j<n:
                    primeNrIndexes[i*j]=0
                    j=j+1
        elif primeNrIndexes[i]==1:
           j= (int)(startNumber/i)+1
           while i*j<n:
               primeNrIndexes[i*j]=0
               j=j+1


@app.route('/')
@app.route('/index')
def index():
    res=[]
    for i in range(0,1000):
        res.append(i)
    return render_template('indexTemp.html',res=res)
        

@app.route('/<int:var>')
def checkNrPrime(var):
    ok=0
    if var>=len(primeNrIndexes):
        recomputePrimes(var+1)
    if primeNrIndexes[var]==1:
        ok=1
    
    return render_template('number.html',number=var,ok=ok)


@app.route('/<startNumber>/<endNumber>')
def index1000plus(startNumber,endNumber):
    try:
        startNumber = int(float(startNumber))
        endNumber = int(float(endNumber))
    except ValueError :
        return render_template('invalid.html')
    if endNumber<startNumber or startNumber<0 :
        return render_template('invalid.html')
    if endNumber-startNumber>1000:
        endNumber=startNumber+1000   ######pot face redirect catre un alt link ?
    if endNumber >=len(primeNrIndexes):
        recomputePrimes(endNumber)
    res=[]
    if startNumber==endNumber:
        res.append(startNumber)
    for i in range(startNumber,endNumber):
        res.append(i)
    return render_template('indexTemp.html',res=res)
        

    
    
