import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np

def graphRawFX():
    date, bid, ask = np.loadtxt('data/GBPUSD1d.txt',
            unpack=True,
            delimiter=',',
            converters={0: mdates.strpdate2num('%Y%m%d%H%M%S')}
            )
    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40, 40), (0, 0), rowspan=40, colspan=40)
    ax1.plot(date, bid)
    ax1.plot(date, ask)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    plt.grid(True)
    plt.show()

graphRawFX()
