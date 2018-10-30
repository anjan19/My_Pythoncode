import numpy as np
import csv
import matplotlib.pyplot as plt
from matplotlib import dates,ticker
import matplotlib as mpl
from matplotlib import colors as mcolors
from matplotlib.collections import LineCollection, PolyCollection
from matplotlib.lines import TICKLEFT, TICKRIGHT, Line2D
from matplotlib.patches import Rectangle
from matplotlib.transforms import Affine2D
#import mpl_finance as mplf

def candlestick_ohlc(ax, quotes, width=0.2, colorup='k', colordown='r',
                     alpha=1.0):
   
    return _candlestick(ax, quotes, width=width, colorup=colorup,
                        colordown=colordown,
                        alpha=alpha, ochl=False)

def _candlestick(ax, quotes, width=0.2, colorup='k', colordown='r',
                 alpha=1.0, ochl=True):
   
    OFFSET = width / 2.0

    lines = []
    patches = []
    for q in quotes:
        if ochl:
            t, open, close, high, low = q[:5]
        else:
            t, open, high, low, close = q[:5]

        if close >= open:
            color = colorup
            lower = open
            height = close - open
        else:
            color = colordown
            lower = close
            height = open - close

        vline = Line2D(
            xdata=(t, t), ydata=(low, high),
            color=color,
            linewidth=0.5,
            antialiased=True,
        )

        rect = Rectangle(
            xy=(t - OFFSET, lower),
            width=width,
            height=height,
            facecolor=color,
            edgecolor=color,
        )
        rect.set_alpha(alpha)

        lines.append(vline)
        patches.append(rect)
        ax.add_line(vline)
        ax.add_patch(rect)
    ax.autoscale_view()

    return lines, patches

mpl.style.use('default')
fname='price.csv'
date_data=[]
open_data=[]
high_data=[]
low_data=[]
close_data=[]
trade=[]

with open(fname,'r') as csvfile:
    data=csv.reader(csvfile, delimiter=',')
    for line in data:
        date_data.append(line[0])
        open_data.append(line[3])
        high_data.append(line[4])
        low_data.append(line[5])
        close_data.append(line[7])
        trade.append(line[8])
        
open_val=np.array(open_data[0:],dtype=np.float64)
high_val=np.array(high_data[0:],dtype=np.float64)
low_val=np.array(low_data[0:],dtype=np.float64)
close_val=np.array(close_data[0:],dtype=np.float64)
trade_val=np.array(trade[0:],dtype=np.float64)

data_dates=[]
for date in date_data:
    new_date=dates.datestr2num(date)
    data_dates.append(new_date)

i=0
ohlc_data=[]
while i<len(data_dates):
    stats_1_day=data_dates[i],open_val[i],high_val[i],low_val[i],close_val[i]
    ohlc_data.append(stats_1_day)
    i+=1
dayFormatter=dates.DateFormatter('%d-%b-%y')
fig,ax1=plt.subplots()
candlestick_ohlc(ax1,ohlc_data,width=0.5,colorup='green',colordown='red',alpha=0.8)
#plt.plot(data_dates,open_val)
ax1.xaxis.set_major_formatter(dayFormatter) # Format the date
ax1.xaxis.set_major_locator(ticker.MaxNLocator(10)) #specify the number of ticks on x axis
plt.xticks(rotation=40)
plt.grid()
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Price Action for the the stock \nfor specified time')
plt.tight_layout()
plt.show()
    