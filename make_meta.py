"""
Description:
The goal of the script is to make the metadata file from the xml file

Author : ROGIE Elliot



"""


import xml.etree.ElementTree as ET

nbrdate=0
nbrnumber=0
nbropi=0
nbrpart=0
cdate=''
cnumber=''
copi=''
cpart=''

PATH_data="/home/elliot/SMAA2020/xml/"
PATH_meta="/home/elliot/SMAA2020/meta/"

for i in range(1,183033):
    cdate=''
    cnumber=''
    copi=''
    cpart=''
    
    tree = ET.parse(PATH_data  + str(i) + '.xml')
    root = tree.getroot()


    meta= ET.Element('meta', {'id_text': str(i)})

    case = ET.SubElement(meta, 'casebody', root.attrib)


    #print(root.tag)
    #print(root.attrib)
    #print('\n\n')
    #print(root.attrib)
    parties =root.find('{http://nrs.harvard.edu/urn-3:HLS.Libr.US_Case_Law.Schema.Case_Body:v1}parties')
    docketnumber = root.find('{http://nrs.harvard.edu/urn-3:HLS.Libr.US_Case_Law.Schema.Case_Body:v1}docketnumber')
    decisiondate = root.find('{http://nrs.harvard.edu/urn-3:HLS.Libr.US_Case_Law.Schema.Case_Body:v1}decisiondate')
    opinion = root.find('{http://nrs.harvard.edu/urn-3:HLS.Libr.US_Case_Law.Schema.Case_Body:v1}opinion')
    do=True
    if parties==None or docketnumber==None or opinion==None or parties==None :
        do=False
    
    #print(parties.tag)
    #print(parties.text)
    #print('\n\n')
    if do==True :
        print(i)
        part = ET.SubElement(case, 'parties')
        if parties!=None:
            t=ET.tostring(parties, method='text').decode("utf-8")
            t=t.replace('\\n  ', '')
            part.text=t
            nbrpart=nbrpart+1
            cpart='p'


        #print(docketnumber.tag)
        #print(docketnumber.text)
        #print('\n\n')
        dock = ET.SubElement(case, 'docketnumber')
        if docketnumber!=None:
            t=ET.tostring(docketnumber, method='text').decode("utf-8")
            t=t.replace('\\n  ', '')
            dock.text=t
            nbrnumber=nbrnumber+1
            cnumber='n'



        #print(decisiondate.tag)
        #print(decisiondate.text)
        #print('\n\n')
        date =ET.SubElement(case, 'decisiondate')
        if decisiondate!=None:
            t=ET.tostring(decisiondate, method='text').decode("utf-8")
            t=t.replace('\\n  ', '')
            date.text=t
            nbrdate=nbrdate+1
            cdate='d'


        #print(opinion.tag)
        #print(opinion.attrib)

        if opinion!=None:
            opin = ET.SubElement(case, 'opinion', opinion.attrib)
            nbropi=nbropi+1
            copi='o'
            for o in opinion:
                if o.tag=='{http://nrs.harvard.edu/urn-3:HLS.Libr.US_Case_Law.Schema.Case_Body:v1}author':
                    #print(o.text)
                    aut= ET.SubElement(opin, 'author')
                    aut.text=o.text
        else:
            opin = ET.SubElement(case, 'opinion')
            aut= ET.SubElement(opin, 'author')







        out=open(PATH_meta + 'meta' + str(i) + '.xml', 'w')
        out.write(str(ET.tostring(meta)))
        out.close()
        out=open(PATH_meta + 'meta' + str(i) + '.xml', 'r')
        for line in out.readlines():
            out2=open(PATH_meta + 'meta' + str(i) + '.xml', 'w')
            line=line[2:-1]
            out2.write(line)
            out2.close()
        out.close()
    

print('nbrdate : '+str(nbrdate) +'   nbrnumber :' + str(nbrnumber) + '    nbropi : '+ str(nbropi));
