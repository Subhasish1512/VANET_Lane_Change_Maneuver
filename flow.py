from xml.etree import ElementTree as ET
import sys
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
et=ET.parse(sys.argv[1])
val=[]
car_id =[]
time = []
ti = 0

for t in et.findall("timestep"):
	if float(t.get("time"))% 1==0:
		#time.append(t.get("time")
		for vh in t.findall("vehicle"):
			if vh.get("id") == "car4":
				val.append(float(vh.get("speed")))
				car_id.append("car4")
				time.append(ti)
			elif vh.get("id") == "car3":
				val.append(float(vh.get("speed")))
				car_id.append("car3")
				time.append(ti)
			elif vh.get("id") == "car2":
				val.append(float(vh.get("speed")))
				car_id.append("car2")
				time.append(ti)
		ti += 1
data = pd.DataFrame({"Speed": val, "Car ID": car_id, "Time": time})
plt.rcParams.update({'font.size': 20})
plt.figure(figsize=(25,20), dpi=500)
sns.lineplot(hue="Car ID", x="Time", y="Speed", data=data, palette="husl", linewidth=4)
plt.title("Speed vs Time", fontsize=35)
plt.xlabel("Time", fontsize=30)
plt.ylabel("Speed", fontsize=30)
plt.legend(fontsize = 20)
plt.savefig("speed.png")
