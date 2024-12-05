# functions used for converting texture files
# def HeadInit(filename,headline):
#     with open(filename,'w')
#     for 
#   分离西交UXD
import re
class UxdConvert(object):
    def __init__(self,angle,hkl):
        self.outputname='62522001-to1-t_R_'+str(hkl)+'.uxd'
        self.angle=str(angle)
        self.miller=str(hkl)
        self.inputname='62522001-to1-t_R.uxd'
        self.dataset=None
        self.datasetNeo=None
        self.index=0
        
    def outputinit(self):
        # f=open(self.inputname)
        # z=f.read()
        # tick=re.search('\n(; Data for range)',z)
        # dataset=z.split(tick.group(1))
        self.dataget()
        headlines=self.dataset[0]
        # f.close()
        g=open(self.outputname,'a+')
        g.writelines(headlines)
        g.close()
    #; Data for range 3    
    def dataget(self):
        with open(self.inputname,'r') as k:
            dataRaw=k.read()
            tick=re.search('\n; Data for range ',dataRaw)
            self.dataset=dataRaw.split(tick.group(0))
            #self.dataset=dataRaw.split(tick)
# while re.search(('\n; Data for range \d',z))
    def extractDataSet(self):       #angle is the 2theta Angle,hkl is the miller index
        quote='_2THETA = '+self.angle
        # output='T27-anneal-LT-'+miller+'.uxd'
        # with open('T27-anneal-LT-raw.uxd','r+') as f:
        #     z=f.read()
        #     tick=re.search('\n(; Data for range)',z)
        #     dataset=z.split(tick.group(1))
            # print(type())
            # for i in dataset:
        # self.dataset    
        for i in range(0,len(self.dataset)):
            if re.search(quote,self.dataset[i])!=None:
                # self.index+=1
                d=open(self.outputname,'a+')
                d.writelines('; Data for range '+self.dataset[i])
            #     (_2THETA = 48.3)
            # re.serch( ,dataset[i])

    def outputUpdate(self):
        k= open(self.outputname,'r')
        dataRaw=k.readlines()
        dataNeo=[]
        i=0
            # k.close()
        for line in dataRaw:
            if re.search('/n; Data for range ',line) !=None:
                i+=1
                dataNeo.append('; Data for range '+str(i)+'\n')
            else:
                dataNeo.append(line)
        k.close()
        filena=self.outputname+'-1'
        g=open(filena,'w')
        g.writelines(dataNeo)

def UxdSplit(angle,hkl):              
    #Angle as the 2theta Angle in degree, hkl to be 'hkl' crystal phase
    # example: UxdSplit(48.3,'100')
    Ast=UxdConvert(angle,hkl)
    Ast.outputinit()
    Ast.extractDataSet()
    Ast.outputUpdate()
    return



















