import pandas as pd

data = pd.read_csv('xiyouji.csv')
for i in data.index:
    htmlname = data['title'][i].replace('\r\n',"").replace("\u3000"," ")
    f = open(htmlname+".html",'w',encoding='utf-8')
    f.write(data['title'][i])
    f.write(data['Content'][i])
    f.close
