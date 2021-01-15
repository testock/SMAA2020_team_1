import xml.etree.ElementTree as ET


PATH_text="/home/elliot/SMAA2020/text/"
PAtH_meta="/home/elliot/SMAA2020/meta/"
label=['D','N', 'A', 'P', 'O']
alpha=183033//3
data=open("/home/elliot/SMAA2020/data0.txt","w")
def compare(opinion, line):
    A=False
    for o in opinion:
            if line[:-1]==o.text:
                A=True
    return A

for i in range(1,183033):
    print(i)
    u=i//alpha
    if u!=(i-1)//alpha:
        data.close()
        data=open("/home/elliot/SMAA2020/data"+str(u)+".txt","w")
        
    world=[]
    
    
    try :
        fmeta=ET.parse(PAtH_meta + "meta" + str(i) + ".xml")
    
    
        ftext=open(PATH_text +  str(i) + ".txt" ,"r")
        root = fmeta.getroot()
        root=root[0]
        parties =root.find('parties')
        docketnumber = root.find('docketnumber')
        decisiondate = root.find('decisiondate')
        opinion = root.find('opinion')
        #print(parties.text)
        #print(docketnumber.text)
        #print(decisiondate.text)
        
        
        for line in ftext.readlines():
            if parties !=None and line[:-1]==parties.text : #or line[:-1]==docketnumber.text or line[:-1]==decisiondate.text :
                for c in line:
                    if c==' ':
                        if world!=[]:
                            t=''.join(world) + " I-P\n"
                            data.write(t)
                        world=[]
                    elif c==',':
                        if world!=[]:
                            t=''.join(world) + " I-P\n"
                            data.write(t)
                        data.write(', I-P\n')
                        world=[]
                    elif c=='\n':
                        if line[-2]=='.':
                            world=world[:-1]
                            if world!=[]:
                                t=''.join(world) + " I-P\n"
                                data.write(t)
                            data.write('. O\n')
                            world=[]
                        else:
                            if world!=[]:
                                t=''.join(world) + " I-P\n"
                                data.write(t)
                            world=[]
                    else:
                        world.append(c)
            elif docketnumber!=None and line[:-1]==docketnumber.text : #or line[:-1]==docketnumber.text or line[:-1]==decisiondate.text :
                for c in line:
                    if c==' ':
                        if world!=[]:
                            t=''.join(world) + " I-N\n"
                            data.write(t)
                        world=[]
                    elif c=='\n':
                        if line[-2]=='.':
                            world=world[:-1]
                            if world!=[]:
                                t=''.join(world) + " I-N\n"
                                data.write(t)
                            data.write('. O\n')
                            world=[]
                        elif line[-2]==' ':
                            world=[]
                        else:
                            if world!=[]:
                                t=''.join(world) + " I-N\n"
                                data.write(t)
                            world=[]
                    else:
                        world.append(c)
            elif decisiondate!=None and line[:-1]==decisiondate.text : #or line[:-1]==docketnumber.text or line[:-1]==decisiondate.text :
                for c in line:
                    if c==' ':
                        if world!=[]:
                            t=''.join(world) + " I-D\n"
                            data.write(t)
                        world=[]
                    elif c==',':
                        if world!=[]:
                            t=''.join(world) + " I-D\n"
                            data.write(t)
                        data.write(', I-D\n')
                        world=[]
                    elif c=='\n':
                        if line[-2]=='.':
                            world=world[:-1]
                            if world!=[]:
                                t=''.join(world) + " I-D\n"
                                data.write(t)
                            data.write('. O\n')
                            world=[]
                        elif line[-2]==' ':
                            world=[]
                        else:
                            if world!=[]:
                                t=''.join(world) + " I-D\n"
                                data.write(t)
                            world=[]
                    else:
                        world.append(c)
            elif opinion!=None and compare(opinion, line) :
                for c in line:
                    if c==' ':
                        if world!=[]:
                            t=''.join(world) + " I-A\n"
                            data.write(t)
                        world=[]
                    elif c==',':
                        
                        if world!=[]:
                            t=''.join(world) + " I-A\n"
                            data.write(t)
                        data.write(', I-A\n')
                        world=[]
                    elif c=='\n':
                        if line[-2]=='.':
                            world=world[:-1]
                            if world!=[]:
                                t=''.join(world) + " I-A\n"
                                data.write(t)
                            data.write('. O\n')
                            world=[]
                        elif line[-2]==' ':
                            world=[]
                        else:
                            if world!=[]:
                                t=''.join(world) + " I-A\n"
                                data.write(t)
                            world=[]
                    else:
                        world.append(c)
            else :
                for c in line:
                    if c==' ':
                        if world!=[]:
                            t=''.join(world) + " O\n"
                            data.write(t)
                        world=[]
                    elif c==',':
                        
                        if world!=[]:
                            t=''.join(world) + " O\n"
                            data.write(t)
                        data.write(', O\n')
                        world=[]
                    elif c=='\n':
                        if len(line)>=2 and line[-2]=='.':
                            world=world[:-1]
                            if world!=[]:
                                t=''.join(world) + " O\n"
                                data.write(t)
                            data.write('. O\n')
                            world=[]
                        elif len(line)<2:
                            world=[]
                        elif line[-2]==' ':
                            world=[]
                        else:
                            if world!=[]:
                                t=''.join(world) + " O\n"
                                data.write(t)
                            world=[]
                    else:
                        world.append(c)
        data.write('\n')
    except IOError:
        continue
data.close()
#def findworlds(line):
    #world=[]
    #for c in line:
        #if c==' ':
            #if world!=[]:
                #print(''.join(world))
                    #world=[]
            #else:
                #world.append(c)
    #return world
