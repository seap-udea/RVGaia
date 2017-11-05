Catalogue of Radial Velocities of GAIA Stars
============================================
Jorge I. Zuluaga and Oscar Sanchez

This catalogue compile radial velocities for as much objects in the
GAIA astrometric catalogue (TGAS) as possible.

TGAS Catalogue
==============

VizieR Reference: I/337/tgas
Citation: Gaia Collaboration (2016)
ADSABS: 

Gaia's full astrometric catalogue (TGAS DR1, 2057050) is stored in 15
binary files with the name:
       
       TgasSource_000-000-00N.csv.gz

where N=1,2,3,...,15.

Radial velocity sources
=======================

At least 5 different catalogue has been used to construct the radial
velocities following the direct suggestion by Bailer-Jones (2017):
	   
	   Catalog		VizieR			ADS

	   Maldonado2010 	J/A+A/521/A12/table1	
	   Webb1995		III/213/catalog
	   GCS2011		J/A+A/530/A138/catalog
	   RAVE-DR5		III/279/rave_dr5
	   Pulkovo		III/252/table8
	   Famaey2005		J/A+A/430/165/tablea1	
	   BB2000 		III/213/catalogue
	   Malaroda2012		III/249/catalog
	   Galah I  		J/MNRAS/465/3203/catal

Extracting Radial Velocities
============================

The first step to create the compiled catalog we need to generate the
full set of radial velocities.  We call this set *RVcatf*.

The script to generate *RVCatf* is `RVCatf.py`.

Once ran the script generate two tables:

- `RVCatf_raw.csv`: this table contains all the information about the
  stars for which RV data is available in the compiled catalogues.
  Data in this table is not purged to remove objects with no RV or
  error in RV (eRV).

- `RVCatf.csv`: the same as before but dropping null RV and eRV.

Both files contains the same columns:

- `tycho2_id`: Tycho2 id.
- `hip`: Hipparchos id.
- `RAJ2000`, `DEJ2000`: J2000 position.
- `RV`: Radial velocity (km/s)
- `eRV`: Error in radial velocity (km/s)
- `CAT`: Name of the catalog from where the information was extracted.

Removing repeated entries
=========================

Once the full catalogue has been compiled, repeated entries must be
removed.  This is achieved by running the script `RVCat.py`

The script produces the table `RVCat.csv``containing the non repeated
entries of our compiled catalog.

Gaia RV Catalog
===============

Once we have compiled the RV information for as much stars as possible
we need to merge it with the Gaia catalog.

For this process we need to run the script `RVGaia.py`.

This script create the final `RVGaia.csv` catalog.

The columns in the catalog are the same as that for TGAS (see
http://gaiaportal.asdc.asi.it/doc/PDF/Tgas_Columns.pdf for reference)
but with new columns coming from the RV catalogs: RAJ2000, DEJ2000,
RV, eRV, CAT.

