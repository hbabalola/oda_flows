#Installing packages
#pip install oda_reader
import pandas as pd
import plotly as pll
from oda_reader import download_crs
from oda_reader import get_available_filters
from oda_reader import bulk_download_multisystem

#setting working directory
import os
print(os.getcwd())
#os.chdir('C:/Users/helen/Documents/ds_projects/2_oda_flows')

crs_filters = get_available_filters(source="crs")
print(crs_filters)

#loading data in bulk and writing as CSV
crs_data =  download_crs(
    start_year=2000,
    end_year=2024,
    pre_process=True,
    filters={"recipient": "PAK", "flow_type": "D"}, #filtering for disbursements to Pak (excludes commitments)
)
crs_data.to_csv('crs_data.csv', index=False)

crs_data = pd.DataFrame(crs_data)
crs_data.info()



