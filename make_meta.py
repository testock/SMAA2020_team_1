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

PATH_data="/home/elliot/ill_xml_20200604/data/data_1000/"
PATH_meta="/home/elliot/ill_xml_20200604/data/data_1000/meta/"

for i in range(1,1000):
    print(i)
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

    #print(parties.tag)
    #print(parties.text)
    #print('\n\n')
    part = ET.SubElement(case, 'parties')
    if docketnumber!=None:
        part.text=parties.text
        nbrpart=nbrpart+1
    

    #print(docketnumber.tag)
    #print(docketnumber.text)
    #print('\n\n')
    dock = ET.SubElement(case, 'docketnumber')
    if docketnumber!=None:
        dock.text=docketnumber.text
        nbrnumber=nbrnumber+1
        
        

    #print(decisiondate.tag)
    #print(decisiondate.text)
    #print('\n\n')
    date =ET.SubElement(case, 'decisiondate')
    if decisiondate!=None:
        date.text=decisiondate.text
        nbrdate=nbrdate+1


    #print(opinion.tag)
    #print(opinion.attrib)
    
    if opinion!=None:
        opin = ET.SubElement(case, 'opinion', opinion.attrib)
        nbropi=nbropi+1
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
    
print('nbrdate : '+str(nbrdate) +'   nbrnumber :' + str(nbrnumber) + '    nbropi : '+ str(nbropi));
