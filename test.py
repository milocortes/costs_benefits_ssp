from costs_benefits_ssp.cb_calculate import CostBenefits
import pandas as pd 
import os 


##---- Definimos directorios

DIR_PATH = "/home/milo/Documents/egtp/sisepuede/CB/ejecuciones_paquete_cb/mexico"

build_path = lambda PATH  : os.path.abspath(os.path.join(*PATH))

### Directorio de salidas de SSP
SSP_RESULTS_PATH = build_path([DIR_PATH,"ssp_salidas"])

### Directorio de configuración de tablas de costos
CB_DEFAULT_DEFINITION_PATH = build_path([DIR_PATH, "cb_factores_costo"])

### Directorio de salidas del módulo de costos y beneficios
OUTPUT_CB_PATH = build_path([DIR_PATH, "cb_resultados"])

### Directorio de datos requeridos paragenerar el archivo tornado_plot_data_QA_QC.csv
QA_PATH = build_path([DIR_PATH, "edgar_cw"])

## Cargamos los datos
ssp_data = pd.read_csv(os.path.join(SSP_RESULTS_PATH, "mexico.csv"))
att_primary = pd.read_csv(os.path.join(SSP_RESULTS_PATH, "ATTRIBUTE_PRIMARY.csv"))
att_strategy = pd.read_csv(os.path.join(SSP_RESULTS_PATH, "ATTRIBUTE_STRATEGY.csv"))

#ssp_data = ssp_data.drop(columns = ["totalvalue_enfu_fuel_consumed_inen_fuel_hydrogen", "totalvalue_enfu_fuel_consumed_inen_fuel_furnace_gas"])

# Definimos la estrategia baseline
strategy_code_base = "BASE"

## Instanciamos un objeto de la clase CostBenefits 
cb = cb_calculate.CostBenefits(ssp_data, att_primary, att_strategy, strategy_code_base)


## El método export_db_to_excel guarda la configuración inicial de las tablas de costos a un archivo excel. 
### Cada pestaña representa una tabla en la base de datos del programa de costos y beneficios.
CB_DEFAULT_DEFINITION_FILE_PATH = os.path.join(CB_DEFAULT_DEFINITION_PATH, "cb_config_params_mexico.xlsx")

#cb.export_db_to_excel(CB_DEFAULT_DEFINITION_FILE_PATH)
cb.load_cb_parameters(CB_DEFAULT_DEFINITION_FILE_PATH)

#------ System Costs
## Calculamos los system costs para todas las estrategias
results_system = cb.compute_system_cost_for_all_strategies()

#-------Technical Costs
## Calculamos los technical costs para todas las estrategias
results_tx = cb.compute_technical_cost_for_all_strategies()

# Combina resultados
results_all = pd.concat([results_system, results_tx], ignore_index = True)

#-------------POST PROCESS SIMULATION RESULTS---------------
# Post process interactions among strategies that affect the same variables
results_all_pp = cb.cb_process_interactions(results_all)
