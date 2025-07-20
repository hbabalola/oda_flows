# oda_flows ### ODA Flows to Pakistan Analysis

## Project Overview

This project analyses Official Development Assistance (ODA) flows to Pakistan from 2002 to 2023 using OECD DAC data on donor disbursements. This workflow includes data loading, cleaning, categorisation, aggregation, and interactive visualisations using Plotly.

## Credits ##
- The DAC was acquired thanks to the API development by 'jm-rivera' in the 'ONEcampaign/oda_reader' public repository.
- Project jointly done by collaborators: 'hbabalola' and 'Uzie9'

## Steps Carried Out

1. **Data Loading**
    - Load data from API using the 'oecd_dac_loading_data.py' file and write the output into CSV file.
    - Loaded ODA data from `crs_data.csv` into a pandas DataFrame.

2. **Initial Exploration**
    - Inspected data structure and missing values using pandas and `missingno`. 
    - Confirmed cluster of mission values were not in fields that we were using within the analysis.
    - Missing values are largely due to the OECD DAC markers, which are assigned according to the project's cross-cutting focus.

3. **Donor Categorisation**
    - Defined lists for donor groups (G7, BRICS, Foundations, UN Agencies, World Bank, Other Countries, etc.).
    - Created a function to assign each donor to a mutually exclusive group.

  4. **Data Aggregation**
    - Grouped data by year and donor group, calculated total ODA values, and converted amounts from millions to billions.

5. **Visualisation**
    - Generated interactive bar charts showing ODA flows by year and donor group.
    - Created sector-wise bar charts with dropdown filters for sector and year.
    - Plotted a line chart to show ODA trends over time.
    - Built treemap visualisations to display ODA distribution by donor group and country.

## Tools Used

- **Python**: Data manipulation and analysis.
- **Pandas**: DataFrame operations.
- **Missingno**: Visualising missing data.
- **Plotly**: Interactive charts and visualisations.
- **Dash**: (Imported for potential dashboard development).

## Key Outcomes

- Categorised donors for clearer analysis.
- Visualised ODA flows over time, by donor group, and by sector.
- Enabled interactive exploration of ODA data for Pakistan.
