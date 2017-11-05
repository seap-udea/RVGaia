###################################################
#EXTERNAL MODULES
###################################################
from util import *

###################################################
#VARIABLES
###################################################
datadir="DB/"

#THIS SCRIPT IS DESIGNED TO BE RUN IN IPYTHON
qip=1
if len(argv)<2:
    qip=0
    argv+=['1']

if argv[1]=='1':
    ######################################################################
    # LEE LA BASE DE DATOS DE RVcatf
    ######################################################################
    print("Reading RVCat...")
    RV=pd.read_csv(datadir+"RVCatf.csv")
    cats=['hip','tycho2_id']
    for cname in cats:
        RV[cname]=RV[cname].fillna('')
        RV[cname]=RV[cname].map(str)
    dfstr=RV.select_dtypes(['object'])
    RV[dfstr.columns]=dfstr.apply(lambda x: x.str.strip())
    RV['hip']=RV['hip'].apply(lambda x:x.replace('.0',''))
    print("Number of RV objects: %d"%len(RV))

def uniqCat(RV):
    RVCat=pd.DataFrame()
    for col in "hip","tycho2_id":
        sel=RV[RV[col]!=''][[col,"eRV"]].sort_values([col,"eRV"])
        print("Number of total entries for %s: %d"%(col,len(sel)))
        index=sel[col].drop_duplicates().index
        uniq=RV.ix[index]
        print("Number of uniq entries for %s: %d"%(col,len(uniq)))
        RVCat=RVCat.append(uniq)

    RVCat.to_csv(datadir+"RVCat.csv",index=False)
    print("Total number of uniq objects:%d"%len(RVCat))
        
if not qip:uniqCat(RV)
