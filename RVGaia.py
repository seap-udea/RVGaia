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
RV=pd.read_csv(datadir+"RVGaia/RVCat.csv",skiprows=1)
RV=RV.drop(RV.columns[[0]],axis=1)
cats=['hip','tycho2_id']
for cname in cats:
    RV[cname]=RV[cname].fillna('')
    RV[cname]=RV[cname].map(str)
dfstr=RV.select_dtypes(['object'])
RV[dfstr.columns]=dfstr.apply(lambda x: x.str.strip())
RV['hip']=RV['tycho2_id'].apply(lambda x:x.replace('.0',''))
print("Number of RV objects:",len(RV))

######################################################################
#POPULATE RVgaia
######################################################################
RVgaia=pd.DataFrame()
columns=GAIA.columns.tolist()+["RV","eRV"]

Nfreq=10
Ntot=10*Nfreq
ti=mytimer()
k=0
for TYC2,HIP in zip(RV.TYC2.values,RV.HIP.values):
    if (k%Nfreq)==0:
        te=mytimer()
        print("Entry %d (time = %.3e)..."%(k,te-ti))
        ti=mytimer()
    row=RV.iloc[k]
    match=pd.DataFrame()
    if TYC2!='':match=GAIA[GAIA.tycho2_id==TYC2]
    if HIP!='':
        if len(match)==0:match=GAIA[GAIA.hip==HIP]
    if len(match)>0:
        found=match.iloc[0]
        nrow=pd.concat([found,row[['RV','eRV']]])
        RVgaia=RVgaia.append(nrow,ignore_index=True)
    k+=1
    if k>Ntot:break

######################################################################
#PREPARE AND SAVE
######################################################################
RVgaia=RVgaia[columns]
RVgaia.to_csv(datadir+"RVGaia/RVGaia.csv",index=False)
print("Number of Gaia stars with radial velocities:",len(RVgaia))
