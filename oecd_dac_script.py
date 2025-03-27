#Installing packages
#pip install oda-reader - downloading package 
import pandas as pd
import plotly as ply
from oda_reader import download_crs
from oda_reader import get_available_filters
from oda_reader import bulk_download_multisystem

crs_filters = get_available_filters(source="crs")
print(crs_filters)

#
#crs_data =  download_crs(
#    start_year=2000,
#    donor_name="World Bank",
 #   end_year=2024,
  #  pre_process=True,
   # filters={"recipient": "PAK"},
#)

crs_data = pd.DataFrame(crs_data)
crs_data.info()
crs_data_uk = crs_data[crs_data['donor_name'] == 'United Kingdom']

crs_data_uk.info()

crs_donornames = crs_data['donor_name'].unique()



