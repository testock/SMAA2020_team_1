"""
Description:
The goal of the script is to transform the jsonl file into xml files (one file for each lines)

Author : ROGIE Elliot
"""

PATH_data="/home/elliot/ill_xml_20200604/data/data_1000/"

f = open("datasample1000.xml")
out=open("datasample.xml")
f1=f.readlines()
doc = False
i=1
for x in f1:
    out.close()
    pre=x[0]
    doc = False
    for y in x:
        if (pre=='<' and y=='c'):
            doc=True
            out = open(PATH_data +  str(i) + ".xml" ,"w")
            
            out.write("<?xml version='1.0' encoding='utf-8'?> \\n")
            
            out.write(pre + y)
            pre=""
        elif (doc==False):
            pre=y
        else:
            if doc == True:
                if (y!='}'):
                    
                    out.write(y)
        
    i=i+1
    print(i)
f.close()

for y in range(1,i):
    ini = open(PATH_data +  str(y) + ".xml")
    for u in ini.readlines():
        out = open(PATH_data +  str(y) + ".xml" ,"w")
        txt=u.replace('\\"', '"')
        txt=txt.replace(' \\n', '')
        txt=txt.replace('\\n"', '')
        out.write(txt)
        out.close()
        
    ini.close()
    print(y)
