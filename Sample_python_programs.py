# Sample function1
def ordnum(a,b):
    if a >  b:
        return [a,b]
    else:
        return [b,a]

# Sample function2, Lambda function
def mymap(a,f):
    r=[]
    for i in a:
        v=f(i)
        r.append(v)
    return r

mymap([2,3,6,7],lambda x: x*3)

# Lambda example 2
f=lambda x,y:print('we are x and y',str(x)+str(y))
f(1,2)

# Dictionary and accessing keys and values

an=dict()
an['anjan']=34
an['sree']=25
an['home']='Chengicherla'
print(an)
d2={'shamp': 23,'brush':26,'surf':56}
print(d2)

print(an.keys())
print(an.values())

lst=['anjan','ravi','anjan','sree','anjan','sree','sam']
names=dict()
for name in lst:
   # if name not in lst:
    #    names[name] = 1
   # else:
   #     names[name]=names[name] + 1
    names[name]=names.get(name,0)+1
print(names)
for i in names:
    print(i,names[i])
for key,val in names.items():
    print(key,val)

# File opening, reading

wcline=open('wc.txt')
wcount=dict()
line=wcline.read()
wlist=line.split()
#print(wlist)
for word in wlist:
    wcount[word]=wcount.get(word,0)+1    
bigwrd=None
bigval=None
for key,val in wcount.items():
    if bigval is None or val > bigval:
        bigwrd=key
        bigval=val
print(bigwrd,bigval)

# Tuple 
t=('a','b','c')
print(t)

for i in t:
    print(i)

(a,b)=(99,100)
print(b)

#Function on tuple
def order(x,y):
    if x > y:
        return (x,y)
    else:
        return (y,x)
(a,b)=order(2,1)
print(a,b)

# Program to count word occurance 
file=input('Enter the file name: ')
words={}
lst=[]
fh=open(file)
for line in fh:
    wlist=line.split()
    for word in wlist:
        words[word]=words.get(word,0)+1
#print(words)
for k,v in words.items():
    lst.append((v,k))
lst.sort(reverse=True)
#print(lst)
for v,k in lst[:10]:
    print(k,v)

