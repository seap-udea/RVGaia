###################################################
#EXTERNAL MODULES
###################################################
from util import *

###################################################
#VARIABLES
###################################################
datadir="./"

######################################################################
# READ TGAS
######################################################################
for i in range(16):
    file1 = "TgasSource_000-000-0"
    file2 = ".csv.gz"
    file = file1 + str(i).zfill(2)+ file2
    filename = datadir + "/TGAS/" + file
    if i == 0:
        print("Reading", file)
        TGAS = pd.read_csv(filename) #, usecols=cols)
    else:
        print("Reading", file)
        DRx = pd.read_csv(filename) #, usecols=cols)
        TGAS = TGAS.append(DRx)

TGAS = pd.DataFrame(TGAS)

######################################################################
# FIX THE TGAS DATABASE
######################################################################
cats=['hip','tycho2_id']
for cname in cats:
    TGAS[cname]=TGAS[cname].fillna('')
    TGAS[cname]=TGAS[cname].map(str)
dfstr=TGAS.select_dtypes(['object'])
TGAS[dfstr.columns]=dfstr.apply(lambda x: x.str.strip())
TGAS['hip']=TGAS['hip'].apply(lambda x:x.replace('.0',''))

######################################################################
# LEE LA BASE DE DATOS DE RVcat
######################################################################
RV=pd.read_csv(datadir+"RVGaia/RVCat.csv")
cats=['hip','tycho2_id']
for cname in cats:
    RV[cname]=RV[cname].fillna('')
    RV[cname]=RV[cname].map(str)
dfstr=RV.select_dtypes(['object'])
RV[dfstr.columns]=dfstr.apply(lambda x: x.str.strip())
RV['hip']=RV['hip'].apply(lambda x:x.replace('.0',''))
print("Number of RV objects:",len(RV))

######################################################################
#POPULATE RVgaia
######################################################################
RVgaia=pd.DataFrame()
RVcolumns=["RAJ2000","DEJ2000","CAT","RV","eRV"]
columns=TGAS.columns.tolist()+RVcolumns

Nfreq=1000
Ntot=1e100*Nfreq
ti=mytimer()
k=0
for tycho2_id,hip in zip(RV.tycho2_id.values,RV.hip.values):
    print(tycho2_id,hip)
    if (k%Nfreq)==0:
        te=mytimer()
        print("Entry %d (time = %.3e)..."%(k,te-ti))
        ti=mytimer()
    row=RV.iloc[k]
    match=pd.DataFrame()
    if tycho2_id!='':match=TGAS[TGAS.tycho2_id==tycho2_id]
    if hip!='':
        if len(match)==0:match=TGAS[TGAS.hip==hip]
    if len(match)>0:
        print "Match!"
        found=match.iloc[0]
        nrow=pd.concat([found,row[RVcolumns]])
        RVgaia=RVgaia.append(nrow,ignore_index=True)
    k+=1
    if k>Ntot:break

######################################################################
#PREPARE AND SAVE
######################################################################
RVgaia=RVgaia[columns]
RVgaia.to_csv(datadir+"RVGaia/RVGaia.csv",index=False)
print("Number of Gaia stars with radial velocities:",len(RVgaia))
