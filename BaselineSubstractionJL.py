import re

def Head_get(filename):    #file Head
    inputname=filename
    with open(inputname,'r') as k:
        dataRaw=k.read()
        dataset=dataRaw.split('; Data for range ')
    return dataset[0]
# inputname='02-AT_JL.uxd' 

#Function that obtain all data
def dataget(filename):
    inputname=filename
    with open(inputname,'r') as k:
        dataRaw=k.read()
        dataset=dataRaw.split('; Data for range ')
    return dataset
        # tick=re.search('(\n;  Data for Range number) ',dataRaw)
        # tick=re.search('(\n; Data for range) ',dataRaw)
        # self.dataset=dataRaw.split(tick.group(1))

def HeadClean(filename):
    head_Raw=Head_get(filename)
    head_Neo=head_Raw.replace('<100><100BL><100BR>\n<002><002BL><002BR>\n<101><101BL><101BR>\n<102><102BL><102BR>\n<110><110BL><110BR>\n','')
    return head_Neo

# Function to get the end number
def datapick(para):
    strTemp=para.split('\t')
    for i in range(1,5):
        id=-1*(i)
        try:
            picked=strTemp[id]
            NumOfPicked=float(picked)
            break
        except ValueError:
            i=i+1
    # NumOfPicked=strTemp
    return NumOfPicked 

#Function that generate the baseline value, call in iteration loop of n
def baselineDefine(LeftNum,RightNum,stepNum,n):
    discre=float(RightNum-LeftNum)
    incre=discre/stepNum
    baseValue=LeftNum+n*incre
    return baseValue
    

#Function that do Baseline Substraction 
def BackSubstract(ind):
    # ind=1
    dataRaw=g[ind].split('\n')
    init=dataRaw.index('; 2THETA	Cnt2_D1\t')
    for i in range(init+1,len(dataRaw)):
        try:
            IntensRaw=dataRaw[i].split('\t')
            # print(IntensRaw[1],type(IntensRaw[1]))
            IntensNeo=float(IntensRaw[1])-baselineDefine(Start,End,len(dataRaw)-init,i-init)  #baseline Substraction
            if IntensNeo<0:
                IntensNeo=0
            IntensRaw[1]=str(IntensNeo)   #复原
            IntensUpdate="\t".join(IntensRaw)  #还原成一行
            dataRaw[i]=IntensUpdate
        except:
            continue
        # print(init)
    dataRaw[0]='; Data for range '+dataRaw[0]
    return dataRaw

# def fileUpdate(filename):
#     with open(filename,) as k:
#         k.close
      
#     return

def updateFile(data):
    outputname='T12-RT-1.uxd'
    strr='\n'.join(data)
    with open(outputname,'a+') as j:
        j.writelines(strr)
        j.close
    return
  
    
def NeoFileInit(infilename,outfilename):
    strrHead=HeadClean(infilename)
    with open(outfilename,'a+') as k:
        k.writelines(strrHead)
    return

inputname='1-RT-2.uxd'
outputname='T12-RT-1.uxd' 
NeoFileInit(inputname,outputname)
g=dataget(inputname)
# print(len(g))
for l in range(1,len(g)-2,3):
    Start=datapick(g[l+1])
    End=datapick(g[l+2])
    dataNeo=BackSubstract(l)
    updateFile(dataNeo)

# print(type(data))


class BacelineSub(object):
    def __init__(self,infile,outfile):
        self.inputname=infile
        self.outputname=outfile

    def Head_get(self):    #file Head
        self.dataget
        self.head_Raw=self.dataset[0]

    def HeadClean(self):
    # head_Raw=Head_get(filename)
        self.head_Neo=self.head_Raw.replace('<100><100BL><100BR>\n<002><002BL><002BR>\n<101><101BL><101BR>\n<102><102BL><102BR>\n<110><110BL><110BR>\n','')
    # return head_Neo

        
        # return dataset[0] 

    def dataget(self):
        with open(self.inputname,'r') as k:
            dataRaw=k.read()
            self.dataset=dataRaw.split('; Data for range ')
        


        

    

 