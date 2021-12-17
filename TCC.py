import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

xml_data = open('C:\\Users\\vitor.cardim.menezes\\Downloads\\grade_history.xml', 'r').read()  
root = ET.XML(xml_data)  # Parse XML
data = []
cols = ["action","oldid","source","loggeduser","itemid","userid","rawgrade","rawgrademax","rawgrademin","rawscaleid","usermodified","finalgrade","hidden","locked","locktime","exported","overridden","excluded","feedback","feedbackformat","information","informationformat","timemodified"]
for i, child in enumerate(root):
    data.append([subchild.text for subchild in child])

df = pd.DataFrame(data)
df.columns = cols
df['finalgrade'] = pd.to_numeric(df['finalgrade'], errors='coerce')
df.loc[(df.finalgrade > 0), 'finalgrade'] = round(df.finalgrade)
df = df.dropna()
df_gb = df.groupby(['finalgrade']).size()

plt.figure(1)
df_gb.plot();

plt.figure(2)
df.boxplot();


plt.figure(3)
df_gb.plot.barh()

plt.figure(4)
df_gb.plot(kind = 'bar')

plt.figure(5)
df_gb.plot.pie(figsize=(10,10))

plt.figure(6)
df_gb.plot.pie(labels=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],colors=["r", "g", "b", "c", "r", "g", "b", "c", "r", "g", "b"],autopct="%.2f",fontsize=20, figsize=(10, 10),);
