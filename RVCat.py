###################################################
#EXTERNAL MODULES
###################################################
from util import *

###################################################
#VARIABLES
###################################################
datadir="./RVGaia/"

###################################################
#READ RVCatf
###################################################
RVcatf=pd.read_csv(datadir+"RVcatf.csv")
RVcatf=RVcatf.fillna('')

###################################################
#REMOVE DUPLICATE ENTRIES
###################################################
ids=""
k=0
indexes=[]

tini=mytimer()
ti=mytimer()
Nfreq=1000
Ntot=1e100 #100*Nfreq
for TYC2,HIP in zip(RVcatf.TYC2.values,RVcatf.HIP.values):
    if (k%Nfreq)==0:
        te=mytimer()
        print("Entry %d (time = %.3e)..."%(k,te-ti))
        ti=mytimer()

    if TYC2!='':
        rep=RVcatf[RVcatf.TYC2==TYC2].sort_values('eRV')
        if(len(rep)>1):indexes+=list(rep.index[1:])
    elif HIP!='':
        rep=RVcatf[RVcatf.HIP==HIP].sort_values('eRV')
        if(len(rep)>1):indexes+=list(rep.index[1:])

    k+=1
    if k>Ntot:break

RVcatf=RVcatf.drop(indexes)
tend=mytimer()
print("Total time = %.3e"%(tend-tini))

###################################################
#SAVE TABLE
###################################################
RVcatf.to_csv(datadir+"RVCat.csv",index=False)
print("Catalogue after removing repeated entries:",len(RVcatf))

