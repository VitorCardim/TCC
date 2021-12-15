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
df_gb.plot(kind = 'bar')
df_gb.plot.pie(figsize=(10,10))
