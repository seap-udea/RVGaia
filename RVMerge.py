###################################################
#EXTERNAL MODULES
###################################################
from util import *

###################################################
#VARIABLES
###################################################
datadir="./"

#THIS SCRIPT IS DESIGNED TO BE RUN IN IPYTHON
qip=1
if len(argv)<2:
    qip=0
    argv+=['1']

if argv[1]=='1':
    ######################################################################
    # READ TGAS
    ######################################################################
    print("Reading TGAS...")
    for i in range(16):
        file1 = "TgasSource_000-000-0"
        file2 = ".csv.gz"
        file = file1 + str(i).zfill(2)+ file2
        filename = datadir + "/TGAS/" + file
        if i == 0:
            TGAS = pd.read_csv(filename)
        else:
            DRx = pd.read_csv(filename)
            TGAS = TGAS.append(DRx)
    TGAS = pd.DataFrame(TGAS)
    print("Number of TGAS objects: %d"%len(TGAS))

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
    print("Reading RVCat...")
    RV=pd.read_csv(datadir+"RVGaia/RVCat.csv")
    cats=['hip','tycho2_id']
    for cname in cats:
        RV[cname]=RV[cname].fillna('')
        RV[cname]=RV[cname].map(str)
    dfstr=RV.select_dtypes(['object'])
    RV[dfstr.columns]=dfstr.apply(lambda x: x.str.strip())
    RV['hip']=RV['hip'].apply(lambda x:x.replace('.0',''))
    print("Number of RV objects: %d"%len(RV))

def runMerge(TGAS,RV):

    ######################################################################
    # PERFORM A MERGE
    ######################################################################
    #MERGING GAIA AND RV DATABASE
    cols=["tycho2_id","hip"]
    RVGaia=pd.DataFrame()
    for col in cols[::1],cols[::-1]:
        print("Merging by %s..."%col[0])
        result=pd.merge(left=TGAS[TGAS[col[0]]!=''],
                        right=RV[RV[col[0]]!=''],
                        on=col[0])
        result=result.drop("%s_y"%col[1],1)
        result=result.rename(columns={"%s_x"%col[1]:col[1]})
        print("Number of matchings for %s: %d"%(col[0],len(result)))
        RVGaia=RVGaia.append(result)

    RVGaia=RVGaia.fillna('NULL')
    RVGaia.to_csv(datadir+"RVGaia/RVGaia.csv",index=False)
    print("Number of matches: %d"%len(RVGaia))

if not qip:runMerge(TGAS,RV)

