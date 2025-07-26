# Costs Benefits Analysis (CBA) 

The Costs and Benefits module belongs to the SISEPUEDE (sImulation of sEctoral Pathways and Uncertainty Exploration for dEcarbonization) decarbonization toolbox.

The module evaluate the Costs and Benefits of bottom-up transformations (decarbonization options) using estimates found in the literature of their costs and benefits.

This includes technical costs or benefits that actors generally experience within a sector and also generally are internal to markets, such as the cost to the agricultural sector of capturing biogas from livestock, the cost of increasing energy efficiency in industry, or the cost of investments in the electricity sector for new capacity to keep up with growing demand. We also include non-technical costs or benefits that are paramount to aligning decarbonization with development goals, such as health benefits of avoided automobile crashes and air pollution, the value of conserving biodiversity, or the time saved thanks to less congestion.

The next table presents a summary of the costs and benefits of transformations across different sectors. Appendices A-G from the report (The Benefits and Costs of Reaching Net Zero Emissions in Latin America and the Caribbean
)[https://publications.iadb.org/en/benefits-and-costs-reaching-net-zero-emissions-latin-america-and-caribbean] provide additional detail on each of these performance metrics, costs, and benefits.

+---------------------------------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Sector                                      | Technical Costs and Benefits                                                               | Non-Technical Costs and benefits                                                        |
+=============================================+============================================================================================+=========================================================================================+
| Agriculture, forests, and other land use    | - Investment cost of transformations                                                       | - Nitrate leaching and runoff from fertilizer                                           |
|                                             | - Value of agricultural inputs, such as fuel and fertilizer                                | - Soil health benefits of conservation agriculture                                      |
|                                             | - Value of agricultural outputs (crops and livestock produced)                             | - Ecosystem services of forests                                                         |
|                                             | - Technical cost of reforestation                                                          | - Human health and productivity of better diets                                         |
|                                             |                                                                                            | - Household grocery costs from improved                                                 |
+---------------------------------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Industry                                    | - Investment cost of transformations                                                       | - Air quality changes from industrial energy and production                             |
|                                             | - Maintenance savings of transformations, e.g., from lower maintenance of heat pumps       |                                                                                         |
|                                             | - Value of industrial inputs, such as fuel                                                 |                                                                                         |
|                                             | - Value of industrial outputs                                                              |                                                                                         |
+---------------------------------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Buildings                                   | - Investment cost of transformations                                                       | - We did not assess non-technical benefits and costs in buildings such as indoor air    |
|                                             | - Maintenance savings of transformations, e.g., from lower maintenance of heat pumps       |                                                                                         |
|                                             | - Value of building inputs, such as fuel                                                   |                                                                                         |
+---------------------------------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Transport                                   | - Investment cost of transformations                                                       | - Health impacts of changing air quality                                                |
|                                             | - System cost of transportation service provisioning                                       | - Health and productivity impacts of avoided crashes                                    |
|                                             | - Maintenance savings, e.g., from lower maintenance of electric vehicles                   | - Productivity impacts from congestion                                                  |
|                                             | - Value of transport inputs, such as fuel                                                  |                                                                                         |
+---------------------------------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Energy production                           | - Capital and operating expenditures of electricity production                             | - Health benefit of avoided air pollution                                               |
|                                             | - Cost of fuels used to produce electricity and other fuel production                      |                                                                                         |
|                                             | - Investment cost of other transformations                                                 |                                                                                         |
+---------------------------------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Waste                                       | - Technical costs of transformations                                                       | - Health impacts of universal safe sanitation                                           |
|                                             | - Value of energy recovery                                                                 | - Health and environmental impacts of ending open dumping                               |
|                                             |                                                                                            | - Water quality impacts of wastewater treatment                                         |
+---------------------------------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+



## CBA Installation

The CBA module can be installed from PyPi:

```
pip install costs-benefits-ssp
```

## Usage

```python
# Load packages
from costs_benefits_ssp.cb_calculate import CostBenefits
import pandas as pd
import os

# Define paths
SSP_RESULTS_PATH = "https://raw.githubusercontent.com/milocortes/costs_benefits_ssp/refs/heads/main/test_data"

# Load data
ssp_data = pd.read_csv(os.path.join(SSP_RESULTS_PATH, "sisepuede_results_sisepuede_run_2025-02-11T11;37;41.739098_WIDE_INPUTS_OUTPUTS.csv"))
att_primary = pd.read_csv(os.path.join(SSP_RESULTS_PATH, "ATTRIBUTE_PRIMARY.csv"))
att_strategy = pd.read_csv(os.path.join(SSP_RESULTS_PATH, "ATTRIBUTE_STRATEGY.csv"))
strategy_code_base = "BASE"

# Instantiate CostBenefits object
cb = CostBenefits(ssp_data, att_primary, att_strategy, strategy_code_base)

# The export_db_to_excel method saves the initial configuration of the cost tables to an excel file.
# Each sheet represents a table in the cost and benefit program database.
# If the Excel file name is not given, the file will be saved with the default name cb_config_params.xlsx on the current python session.

CB_DEFAULT_DEFINITION_PATH = os.getcwd()
CB_DEFAULT_DEFINITION_FILE_PATH = os.path.join(CB_DEFAULT_DEFINITION_PATH, "cb_config_params.xlsx")

cb.export_db_to_excel(CB_DEFAULT_DEFINITION_FILE_PATH)

# Once that the excel file has been updated, we can reload it in order to update the cost factors database
cb.load_cb_parameters(CB_DEFAULT_DEFINITION_FILE_PATH)

# Compute System Costs
results_system = cb.compute_system_cost_for_all_strategies()

# Compute Technical Costs
results_tx = cb.compute_technical_cost_for_all_strategies()

# Combine results
results_all = pd.concat([results_system, results_tx], ignore_index = True)

#-------------POST PROCESS SIMULATION RESULTS---------------
# Post process interactions among strategies that affect the same variables
results_all_pp = cb.cb_process_interactions(results_all)

# SHIFT any stray costs incurred from 2015 to 2025 to 2025 and 2035
results_all_pp_shifted = cb.cb_shift_costs(results_all_pp)

# Save the results
results_all_pp_shifted.to_csv("cba_resultados.csv", index = False)

```