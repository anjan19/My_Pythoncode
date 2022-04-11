import base64
import os
import requests
import datetime
import zipfile
import pandas as pd
import pandas_gbq

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)
    
    home_path = os.environ['HOME']
    if pubsub_message == 'TRIGGER_DATALOAD':
      project = 'anjan1909-346410'
      now = datetime.datetime.now()

      if len(str(now.day))==1:
        m_day='0'+str(now.day)
      else:
        m_day=str(now.day)
    
      if len(str(now.month))==1:
        m_mn='0'+str(now.month)
      else:
        m_mn=str(now.month)    
  
      fn='MTO_'+m_day+m_mn+str(now.year)+'.DAT'
      fn2=m_day+now.strftime("%b").upper()+str(now.year)
      url='https://www1.nseindia.com/archives/equities/mto/'+fn
      #print(url)

      def web_download(url,ospath,file):
        response = requests.get(url)
        with open(os.path.join(ospath,file),'wb') as f:
          f.write(response.content)
          f.close()

      def file_remove(file):
        if os.path.exists(file):
          os.remove(file)
          print(": File removed")  
        else:
          print("The file does not exist")

      file_remove(home_path + "/*.csv")
#file_remove("/home/anjangcp7861/swdp.csv")

      web_download(url,home_path,"swtd.csv")

      url='https://www1.nseindia.com/content/historical/EQUITIES/'+str(now.year)+'/'+now.strftime("%b").upper()+'/cm'+fn2+'bhav.csv.zip'
#print(url)

      web_download(url,home_path,"swdp.csv")
    
      zip_ref = zipfile.ZipFile(home_path + '/swdp.csv', 'r')
      zip_ref.extractall(home_path)
      zip_ref.close()

      os.replace(home_path + "/cm"+m_day+now.strftime("%b").upper()+str(now.year)+"bhav.csv",home_path + "/swdp.csv")

      df_d = pd.read_csv(home_path + '/swtd.csv',skiprows = 4)
      df_d.columns=['REC_TYPE','SR_NO','SYMBOL','SCR_TYPE','TRD_QTY','DLVRY_QTY','DLVRY_TO_TRD_PERC']
      df_h = pd.read_csv(home_path+ '/swdp.csv')
      df_join = pd.merge(df_h, df_d, how='inner', on = 'SYMBOL')
      df_res = df_join[['SYMBOL','TIMESTAMP','PREVCLOSE','OPEN','HIGH','LOW','CLOSE','TOTTRDQTY','DLVRY_QTY','DLVRY_TO_TRD_PERC']]

      pandas_gbq.to_gbq(df_res,
              'stock_data.company_daywise_ohlc', 
               project,
               chunksize=1000, 
               if_exists='append'
            )
    else:
      print('No event triggered')  
