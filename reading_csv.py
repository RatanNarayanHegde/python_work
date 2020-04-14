import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = 'sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs =[]
    dates=[]
    low =[]
    for row in reader:
        try:
            dates.append(datetime.strptime(row[0],"%Y-%m-%d"))
            highs.append(int(row[1]))
            low.append(int(row[3]))
        except:
            print("data missing")

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.8)
plt.plot(dates,low,c='blue')
plt.fill_between(dates,highs,low,facecolor='blue',alpha=0.2)

#formatting the plt
plt.title("High Low temperatures of alaska",fontsize=20)
plt.ylabel("Temperature(F)",fontsize=16)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.show()