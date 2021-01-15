"""
Description:
The goal of the script is to make the text file from the xml file

Author : ROGIE Elliot



"""
import xml.etree.ElementTree as ET

PATH_data="/home/elliot/SMAA2020/xml/"
PATH_text="/home/elliot/SMAA2020/text/"
for i in range(1,183033):
    print(i)
    xml = open(PATH_data  + str(i)+ ".xml")
    text = open(PATH_text + str(i)+ ".txt", 'w')
    writing=True
    for line in xml.readlines():
        for caract in line:
            if (caract=='<'):
                writing=False
            elif (caract=='>'):
                writing=True
            elif writing :
                text.write(caract)
    xml.close()
    text.close()

for i in range(1,183033):
    print(i)
    text = open(PATH_text + str(i)+ ".txt", 'r')
    for line in text.readlines():
        text2 = open(PATH_text + str(i)+ ".txt", 'w')
        line=line.replace('\\n  ', '\n')
        line=line.replace('  ', '')
        text2.write(line)
    text2.close()
    text.close()
        #for y in range(len(line)-3):
            #if line[y]=='\\' and line[y+1]=='n' and line[y+2]==' ' and line[y]==' ':

            
    xml.close()
    text.close()
