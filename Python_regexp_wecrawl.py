
# coding: utf-8

# In[7]:


x=('a','b','c')
for i in x:
    print(i)


# In[16]:


x=(1,'anjan')


# In[24]:


def myfun():
    return 1,2,3
myfun()


# In[25]:


a=[1,2,3]
ret=[t*2 for t in a]
print(ret)


# In[13]:


import re
h=open('wc.txt')
for l in h:
    l=l.strip()
    if re.search('python',l):
        print(l)


# In[77]:


import re
s='My 2 favourate numbers are 19 and 21'
lst=re.findall('[0-9]+',s)
print(lst)


# In[96]:


import re
re.findall(' ..','a this is aa to match aaa waw aaaa')
re.findall('@.+ ','a this is aa to @match aaa waw aaaa')
re.findall('\\+','a this+ is aa to @match aaa waw aaaa')
re.findall('^this','this is aa to @match aaa waw aaaa')
re.findall('...a$','this is aa to @match aaa waw aaaa')
re.findall('.\s.','this is aa to @match aaa waw aaaa')
re.findall('s +','this    is aa to @match aaa waw aaaa')
re.findall('a\S','thisa    is aa to @match aaa waw aaaa')
re.findall('thi?','this is aa to @match aaa waw aaaa')
re.findall('[wa]a','this is aa to @match aaa waw aaaa')
re.findall('th[ai][st]','this is aa to get that @match aaa')
re.findall('th[ai][st]','this is aa to get that @match aaa')
re.findall('[aeiou]','this is aa to get that @match aaa')
re.findall('[aeiou][^aeiou]','this is aa to get @match aaa')
re.findall('[a-i]','this is aa to get that @match aaa')
re.findall('[0-9]+\\.[0-9]+','1.x this is a decimal nr 21.54')
re.findall('[^0-9a-z.]','1.x this is a decimal nr 21.54')
re.findall('\S+@\S+','These are email ids anjanvlsi@gmail.com and edfdfe@yahoomail.com ok')


# In[103]:


x=3
y=2
print('{} * {} = {}'.format(x,y,x*y))


# In[5]:


import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('www.pyinf.com',80))
mysock.send(b'GET http://www.pyfinf.com/code/romeo.txt HTTP/1.\n\n')
while True:
    data=mysock.recv(512)
    if (len(data) < 1):
        break
    print(data)   
mysock.close()    


# In[7]:


from urllib import *
fhand=request.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
    print(line.strip())


# In[9]:


from urllib import *
fhand=request.urlopen('http://www.py4inf.com/code/romeo.txt')
wcd=dict()
for line in fhand:
    words=line.split()
    for word in words:
        wcd[word]=wcd.get(word,0)+1
print(wcd)    


# In[13]:


from urllib import *
from bs4 import BeautifulSoup
# 'https://en.wikipedia.org/wiki/Web_scraping'
url=input('Enter URL- ')
html=request.urlopen(url).read()
soup=BeautifulSoup(html)
tags=soup('a')
for i in tags:
    print(i.get('href',None))

