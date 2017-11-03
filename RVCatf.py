###################################################
#EXTERNAL MODULES
###################################################
from util import *

###################################################
#VARIABLES
###################################################
srcdir="RV/"
datadir="./"

###################################################
#INITIAL DATA
###################################################
data=dict()
match=dict()
RVcat=pd.DataFrame()

###################################################
#READ CATALOGUES
###################################################
#MALDONADO2010
name="Maldonado2010.tsv"
print("Building catalogue %s..."%name)
comments=list(range(82))+[83,84]
data[name]=pd.read_csv(srcdir+name,sep=";",skiprows=comments)
cats=['HIP']
for cname in cats:
    data[name][cname]=data[name][cname].fillna('')
    data[name][cname]=data[name][cname].map(str)
dfstr=data[name].select_dtypes(['object'])
data[name][dfstr.columns]=dfstr.apply(lambda x: x.str.strip())
print("Number of objects in %s:"%name,len(data[name]))
for cat in cats:
    cond=data[name][cat]!=''
    print("Number of objects in catalogue %s:"%cat,len(data[name][cat][cond]))
#STORING RESULTS
df=pd.DataFrame()
if not 'TYC2' in data[name].columns:df["TYC2"]=''
else:df["TYC2"]=data[name]["TYC2"]
if not 'HIP' in data[name].columns:df["HIP"]=''
else:df["HIP"]=data[name]["HIP"].apply(lambda x:x.replace('.0',''))
COORDS=dict(RAJ2000="_RAJ2000",DECJ2000="_DEJ2000")
for C in COORDS.keys():df[C]=data[name][COORDS[C]]
df["RV"]=data[name]["RV"]
df["eRV"]=data[name]["e_RV"]
df["CAT"]=name
#ZERO ERRORS
cond=df.RV==''
df=df.drop(df.index[cond])
df.RV=df.RV.map(float)
df.eRV[df.eRV=='']=0.0
df.eRV=df.eRV.map(float)
med=df.eRV[df.eRV>0].median()
print("Median error:",med)
print("Number of entries with zero error:",len(df.eRV[df.eRV==0]))
df.eRV[df.eRV==0]=med
#RESULTING SIZE
print("Filtered catalogue:",len(df))
#FILLNA
RVcat=RVcat.append(df.fillna(''))

#WEB1995
#III/213/catalog
name="Web1995-HIP.csv"
print("Building catalogue %s..."%name)
data[name]=pd.read_csv(srcdir+name)
cats=['HIP']
for cname in cats:
    data[name][cname]=data[name][cname].fillna('')
    data[name][cname]=data[name][cname].map(str)
dfstr=data[name].select_dtypes(['object'])
data[name][dfstr.columns]=dfstr.apply(lambda x: x.str.strip())
print("Number of objects in %s:"%name,len(data[name]))
for cat in cats:
    cond=data[name][cat]!=''
    print("Number of objects in catalogue %s:"%cat,len(data[name][cat][cond]))
#STORING RESULTS
df=pd.DataFrame()
if not 'TYC2' in data[name].columns:df["TYC2"]=''
else:df["TYC2"]=data[name]["TYC2"]
if not 'HIP' in data[name].columns:df["HIP"]=''
else:df["HIP"]=data[name]["HIP"].apply(lambda x:x.replace('.0',''))
COORDS=dict(RAJ2000="_RAJ2000",DECJ2000="_DEJ2000")
for C in COORDS.keys():df[C]=data[name][COORDS[C]]
df["RV"]=data[name]["RV"].map(str)
df["eRV"]=data[name]["e_RV"].map(str)
df["CAT"]=name
#ZERO ERRORS
cond=df.RV==''
df=df.drop(df.index[cond])
df.RV=df.RV.map(float)
df.eRV[df.eRV=='']=0.0
df.eRV=df.eRV.map(float)
med=df.eRV[df.eRV>0].median()
print("Median error:",med)
print("Number of entries with zero error:",len(df.eRV[df.eRV==0]))
df.eRV[df.eRV==0]=med
#RESULTING SIZE
print("Filtered catalogue:",len(df))
#FILLNA
RVcat=RVcat.append(df.fillna(''))

#WEB1995-TYC2
#III/213/catalog
name="Web1995-TYC2.csv"
print("Building catalogue %s..."%name)
data[name]=pd.read_csv(srcdir+name)
cats=['TYC2','HIP']
for cname in cats:
    data[name][cname]=data[name][cname].fillna('')
    data[name][cname]=data[name][cname].map(str)
dfstr=data[name].select_dtypes(['object'])
data[name][dfstr.columns]=dfstr.apply(lambda x: x.str.strip())
print("Number of objects in %s:"%name,len(data[name]))
for cat in cats:
    cond=data[name][cat]!=''
    print("Number of objects in catalogue %s:"%cat,len(data[name][cat][cond]))
#STORING RESULTS
df=pd.DataFrame()
if not 'TYC2' in data[name].columns:df["TYC2"]=''
else:df["TYC2"]=data[name]["TYC2"]
if not 'HIP' in data[name].columns:df["HIP"]=''
else:df["HIP"]=data[name]["HIP"].apply(lambda x:x.replace('.0',''))
COORDS=dict(RAJ2000="_RAJ2000",DECJ2000="_DEJ2000")
for C in COORDS.keys():df[C]=data[name][COORDS[C]]
df["RV"]=data[name]["RV"].map(str)
df["eRV"]=data[name]["e_RV"].map(str)
df["CAT"]=name
#ZERO ERRORS
cond=df.RV==''
df=df.drop(df.index[cond])
df.RV=df.RV.map(float)
df.eRV[df.eRV=='']=0.0
df.eRV=df.eRV.map(float)
med=df.eRV[df.eRV>0].median()
print("Median error:",med)
print("Number of entries with zero error:",len(df.eRV[df.eRV==0]))
df.eRV[df.eRV==0]=med
#RESULTING SIZE
print("Filtered catalogue:",len(df))
#FILLNA
RVcat=RVcat.append(df.fillna(''))

#GCS2011
#J/A+A/530/A138/catalog
name="GCS2011.tsv"
print("Building catalogue %s..."%name)
comments=list(range(174))+[175,176]
data[name]=pd.read_csv(srcdir+name,sep="|",skiprows=comments)
cats=['HIP']
for cname in cats:
    data[name][cname]=data[name][cname].fillna('')
    data[name][cname]=data[name][cname].map(str)
dfstr=data[name].select_dtypes(['object'])
data[name][dfstr.columns]=dfstr.apply(lambda x: x.str.strip())
print("Number of objects in %s:"%name,len(data[name]))
for cat in cats:
    cond=data[name][cat]!=''
    print("Number of objects in catalogue %s:"%cat,len(data[name][cat][cond]))
#STORING RESULTS
df=pd.DataFrame()
if not 'TYC2' in data[name].columns:df["TYC2"]=''
else:df["TYC2"]=data[name]["TYC2"]
if not 'HIP' in data[name].columns:df["HIP"]=''
else:df["HIP"]=data[name]["HIP"].apply(lambda x:x.replace('.0',''))
COORDS=dict(RAJ2000="_RAJ2000",DECJ2000="_DEJ2000")
for C in COORDS.keys():df[C]=data[name][COORDS[C]]
df["RV"]=data[name]["RV"].map(str)
df["eRV"]=data[name]["e_RV"].map(str)
df["CAT"]=name
#ZERO ERRORS
cond=df.RV==''
df=df.drop(df.index[cond])
df.RV=df.RV.map(float)
df.eRV[df.eRV=='']=0.0
df.eRV=df.eRV.map(float)
med=df.eRV[df.eRV>0].median()
print("Median error:",med)
print("Number of entries with zero error:",len(df.eRV[df.eRV==0]))
df.eRV[df.eRV==0]=med
#RESULTING SIZE
print("Filtered catalogue:",len(df))
#FILLNA
RVcat=RVcat.append(df.fillna(''))

#RAVE-DR5
#III/279/rave_dr5
name="RAVE-DR5.tsv"
print("Building catalogue %s..."%name)
comments=list(range(78))+[79,80]
data[name]=pd.read_csv(srcdir+name,sep=";",skiprows=comments)
cats=['TYCHO2']
for cname in cats:
    data[name][cname]=data[name][cname].fillna('')
    data[name][cname]=data[name][cname].map(str)
dfstr=data[name].select_dtypes(['object'])
data[name][dfstr.columns]=dfstr.apply(lambda x: x.str.strip())
print("Number of objects in %s:"%name,len(data[name]))
for cat in cats:
    cond=data[name][cat]!=''
    print("Number of objects in catalogue %s:"%cat,len(data[name][cat][cond]))
#STORING RESULTS
df=pd.DataFrame()
if not 'TYC2' in data[name].columns:df["TYC2"]=''
else:df["TYC2"]=data[name]["TYC2"]
if not 'HIP' in data[name].columns:df["HIP"]=''
else:df["HIP"]=data[name]["HIP"].apply(lambda x:x.replace('.0',''))
COORDS=dict(RAJ2000="RAJ2000",DECJ2000="DEJ2000")
for C in COORDS.keys():df[C]=data[name][COORDS[C]]
df["RV"]=data[name]["HRV"].map(str)
df["eRV"]=data[name]["e_HRV"].map(str)
df["CAT"]=name
#ZERO ERRORS
cond=df.RV==''
df=df.drop(df.index[cond])
df.RV=df.RV.map(float)
df.eRV[df.eRV=='']=0.0
df.eRV=df.eRV.map(float)
med=df.eRV[df.eRV>0].median()
print("Median error:",med)
print("Number of entries with zero error:",len(df.eRV[df.eRV==0]))
df.eRV[df.eRV==0]=med
#RESULTING SIZE
print("Filtered catalogue:",len(df))
#FILLNA
RVcat=RVcat.append(df.fillna(''))

#PULKOVO
#III/252/table8
name="Pulkovo.tsv"
print("Building catalogue %s..."%name)
comments=list(range(61))+[62,63]
data[name]=pd.read_csv(srcdir+name,sep=";",skiprows=comments)
cats=['HIP']
for cname in cats:
    data[name][cname]=data[name][cname].fillna('')
    data[name][cname]=data[name][cname].map(str)
dfstr=data[name].select_dtypes(['object'])
data[name][dfstr.columns]=dfstr.apply(lambda x: x.str.strip())
print("Number of objects in %s:"%name,len(data[name]))
for cat in cats:
    cond=data[name][cat]!=''
    print("Number of objects in catalogue %s:"%cat,len(data[name][cat][cond]))
#STORING RESULTS
df=pd.DataFrame()
if not 'TYC2' in data[name].columns:df["TYC2"]=''
else:df["TYC2"]=data[name]["TYC2"]
if not 'HIP' in data[name].columns:df["HIP"]=''
else:df["HIP"]=data[name]["HIP"].apply(lambda x:x.replace('.0',''))
COORDS=dict(RAJ2000="_RA",DECJ2000="_DE")
for C in COORDS.keys():df[C]=data[name][COORDS[C]]
df["RV"]=data[name]["RV"].map(str)
df["eRV"]=data[name]["eRV"].map(str)
df["CAT"]=name
#ZERO ERRORS
cond=df.RV==''
df=df.drop(df.index[cond])
df.RV=df.RV.map(float)
df.eRV[df.eRV=='']=0.0
df.eRV=df.eRV.map(float)
med=df.eRV[df.eRV>0].median()
print("Median error:",med)
print("Number of entries with zero error:",len(df.eRV[df.eRV==0]))
df.eRV[df.eRV==0]=med
#RESULTING SIZE
print("Filtered catalogue:",len(df))
#FILLNA
RVcat=RVcat.append(df.fillna(''))

#FAMAEY2005
#J/A+A/430/165/tablea1
name="Famaey2005.tsv"
print("Building catalogue %s..."%name)
comments=list(range(118))+[119,120]
data[name]=pd.read_csv(srcdir+name,sep=";",skiprows=comments)
cats=['HIP']
for cname in cats:
    data[name][cname]=data[name][cname].fillna('')
    data[name][cname]=data[name][cname].map(str)
dfstr=data[name].select_dtypes(['object'])
data[name][dfstr.columns]=dfstr.apply(lambda x: x.str.strip())
print("Number of objects in %s:"%name,len(data[name]))
for cat in cats:
    cond=data[name][cat]!=''
    print("Number of objects in catalogue %s:"%cat,len(data[name][cat][cond]))
#STORING RESULTS
df=pd.DataFrame()
if not 'TYC2' in data[name].columns:df["TYC2"]=''
else:df["TYC2"]=data[name]["TYC2"]
if not 'HIP' in data[name].columns:df["HIP"]=''
else:df["HIP"]=data[name]["HIP"].apply(lambda x:x.replace('.0',''))
COORDS=dict(RAJ2000="_RAJ2000",DECJ2000="_DEJ2000")
for C in COORDS.keys():df[C]=data[name][COORDS[C]]
df["RV"]=data[name]["RV"].map(str)
df["eRV"]=data[name]["e_RV"].map(str)
df["CAT"]=name
#ZERO ERRORS
cond=df.RV==''
df=df.drop(df.index[cond])
df.RV=df.RV.map(float)
df.eRV[df.eRV=='']=0.0
df.eRV=df.eRV.map(float)
med=df.eRV[df.eRV>0].median()
print("Median error:",med)
print("Number of entries with zero error:",len(df.eRV[df.eRV==0]))
df.eRV[df.eRV==0]=med
#RESULTING SIZE
print("Filtered catalogue:",len(df))
#FILLNA
RVcat=RVcat.append(df.fillna(''))

#BB2000
#III/213/catalogue
name="BB2000.csv"
print("Building catalogue %s..."%name)
data[name]=pd.read_csv(srcdir+name)
cats=['TYC2','HIP']
for cname in cats:
    data[name][cname]=data[name][cname].fillna('')
    data[name][cname]=data[name][cname].map(str)
dfstr=data[name].select_dtypes(['object'])
data[name][dfstr.columns]=dfstr.apply(lambda x: x.str.strip())
print("Number of objects in %s:"%name,len(data[name]))
for cat in cats:
    cond=data[name][cat]!=''
    print("Number of objects in catalogue %s:"%cat,len(data[name][cat][cond]))
#STORING RESULTS
df=pd.DataFrame()
if not 'TYC2' in data[name].columns:df["TYC2"]=''
else:df["TYC2"]=data[name]["TYC2"]
if not 'HIP' in data[name].columns:df["HIP"]=''
else:df["HIP"]=data[name]["HIP"].apply(lambda x:x.replace('.0',''))
COORDS=dict(RAJ2000="_RAJ2000",DECJ2000="_DEJ2000")
for C in COORDS.keys():df[C]=data[name][COORDS[C]]
df["RV"]=data[name]["RV"].map(str)
df["eRV"]=data[name]["e_RV"].map(str)
df["CAT"]=name
#ZERO ERRORS
cond=df.RV==''
df=df.drop(df.index[cond])
df.RV=df.RV.map(float)
df.eRV[df.eRV=='']=0.0
df.eRV=df.eRV.map(float)
med=df.eRV[df.eRV>0].median()
print("Median error:",med)
print("Number of entries with zero error:",len(df.eRV[df.eRV==0]))
df.eRV[df.eRV==0]=med
#RESULTING SIZE
print("Filtered catalogue:",len(df))
#FILLNA
RVcat=RVcat.append(df.fillna(''))

#MALARODA2012
#III/249/catalog
name="Malaroda2012.csv"
print("Building catalogue %s..."%name)
data[name]=pd.read_csv(srcdir+name)
cats=['TYC2','HIP']
for cname in cats:
    data[name][cname]=data[name][cname].fillna('')
    data[name][cname]=data[name][cname].map(str)
dfstr=data[name].select_dtypes(['object'])
data[name][dfstr.columns]=dfstr.apply(lambda x: x.str.strip())
print("Number of objects in %s:"%name,len(data[name]))
for cat in cats:
    cond=data[name][cat]!=''
    print("Number of objects in catalogue %s:"%cat,len(data[name][cat][cond]))
#STORING RESULTS
df=pd.DataFrame()
if not 'TYC2' in data[name].columns:df["TYC2"]=''
else:df["TYC2"]=data[name]["TYC2"]
if not 'HIP' in data[name].columns:df["HIP"]=''
else:df["HIP"]=data[name]["HIP"].apply(lambda x:x.replace('.0',''))
COORDS=dict(RAJ2000="_RAJ2000",DECJ2000="_DEJ2000")
for C in COORDS.keys():df[C]=data[name][COORDS[C]]
df["RV"]=data[name]["RV"].map(str)
df["eRV"]=1.0;df["eRV"]=df["eRV"].map(str) #TYPICAL VALUE FOR OTHER CATALOGUES
df["CAT"]=name
#ZERO ERRORS
cond=df.RV==''
df=df.drop(df.index[cond])
df.RV=df.RV.map(float)
df.eRV[df.eRV=='']=0.0
df.eRV=df.eRV.map(float)
med=df.eRV[df.eRV>0].median()
print("Median error:",med)
print("Number of entries with zero error:",len(df.eRV[df.eRV==0]))
df.eRV[df.eRV==0]=med
#RESULTING SIZE
print("Filtered catalogue:",len(df))
#FILLNA
RVcat=RVcat.append(df.fillna(''))

#GALAH I
#J/MNRAS/465/3203/catal
name="Galah.tsv"
print("Building catalogue %s..."%name)
comments=list(range(54))+[55,56]
data[name]=pd.read_csv(srcdir+name,sep=";",skiprows=comments)
cats=['TYC2']
for cname in cats:
    data[name][cname]=data[name][cname].fillna('')
    data[name][cname]=data[name][cname].map(str)
dfstr=data[name].select_dtypes(['object'])
data[name][dfstr.columns]=dfstr.apply(lambda x: x.str.strip())
print("Number of objects in %s:"%name,len(data[name]))
for cat in cats:
    cond=data[name][cat]!=''
    print("Number of objects in catalogue %s:"%cat,len(data[name][cat][cond]))
#STORING RESULTS
df=pd.DataFrame()
if not 'TYC2' in data[name].columns:df["TYC2"]=''
else:df["TYC2"]=data[name]["TYC2"]
if not 'HIP' in data[name].columns:df["HIP"]=''
else:df["HIP"]=data[name]["HIP"].apply(lambda x:x.replace('.0',''))
COORDS=dict(RAJ2000="RAJ2000",DECJ2000="DEJ2000")
for C in COORDS.keys():df[C]=data[name][COORDS[C]]
df["RV"]=data[name]["RV"].map(str)
df["eRV"]=0.6;df["eRV"]=df["eRV"].map(str) #Martell et al. (2017)
df["CAT"]=name
#ZERO ERRORS
cond=df.RV==''
df=df.drop(df.index[cond])
df.RV=df.RV.map(float)
df.eRV[df.eRV=='']=0.0
df.eRV=df.eRV.map(float)
med=df.eRV[df.eRV>0].median()
print("Median error:",med)
print("Number of entries with zero error:",len(df.eRV[df.eRV==0]))
df.eRV[df.eRV==0]=med
#RESULTING SIZE
print("Filtered catalogue:",len(df))
#FILLNA
RVcat=RVcat.append(df.fillna(''))

###################################################
#COMPILING FULL TABLE
###################################################
print("Compiling final catalogue...")
RVcat=RVcat.rename(columns={'TYC2':'tycho2_id','HIP':'hip'})
RVcat.to_csv(datadir+"RVcatf_raw.csv",index=False)
print("Compiling final catalogue...")
RVcatf=RVcat.reset_index(drop=True)
print("Number of unfiltered entries:",len(RVcatf))
print("Catalogues included:",np.unique(RVcat.CAT.values))
RVcatf.is_copy=False
cond=RVcatf.RV==''
RVcatf=RVcatf.drop(RVcatf.index[cond])
RVcatf.RV=RVcatf.RV.map(float)
cond=RVcatf.eRV==''
RVcatf=RVcatf.drop(RVcatf.index[cond])
RVcatf.eRV=RVcatf.eRV.map(float)
print("Number of filtered entries:",len(RVcatf))
RVcatf.to_csv(datadir+"RVcatf.csv",index=False)
