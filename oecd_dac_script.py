#Installing packages
#pip install oda-reader - downloading package 
import pandas as pd
from oda_reader import download_crs
from oda_reader import get_available_filters

crs_filters = get_available_filters(source="crs")
print(crs_filters)

#
crs_data =  download_crs(
    start_year=2000,
    end_year=2024,
    pre_process=True,
    filters={"recipient": "PAK"},
)

crs_data.info()

