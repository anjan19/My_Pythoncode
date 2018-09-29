#Program for word count
with open('C:/Python34/fruits.txt') as fh:
    lst=list()
    lst=fh.read().split()
    print(lst)
    dct=dict()
    for word in lst:
        
        if word in dct: 
            dct[word]=dct[word]+1
        else:
            dct[word]=1
    for k,v in dct.items():
        print(k,':',v)
        
    
