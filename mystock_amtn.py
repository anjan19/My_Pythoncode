
import os
import requests
import datetime
import zipfile

now = datetime.datetime.now()

if len(str(now.day))==1:
    m_day='0'+str(now.day)
else:
    m_day=str(now.day)
    
fn='MTO_'+m_day+m_mn+str(now.year)+'.DAT'
fn2=m_day+now.strftime("%b").upper()+str(now.year)
url='https://www.nseindia.com/archives/equities/mto/'+fn

def web_download(url,ospath,file):
    response = requests.get(url)
    with open(os.path.join(ospath,file),'wb') as f:
      f.write(response.content)
      f.close()
        
web_download(url,"/home/anjanvlsi8432/anjan/nse","swtd.csv")

url='https://www.nseindia.com/content/historical/EQUITIES/'+str(now.year)+'/'+now.strftime("%b").upper()+'/cm'+fn2+'bhav.csv.zip'

web_download(url,"/home/anjanvlsi8432/anjan/nse","swdp.csv")
    
zip_ref = zipfile.ZipFile('/home/anjanvlsi8432/anjan/nse/swdp.csv', 'r')
zip_ref.extractall('/home/anjanvlsi8432/anjan/nse')
zip_ref.close()

if os.path.exists("/home/anjanvlsi8432/anjan/nse/swdp.csv"):
  os.remove("/home/anjanvlsi8432/anjan/nse/swdp.csv")
  print("File removed")  
else:
  print("The file does not exist")  