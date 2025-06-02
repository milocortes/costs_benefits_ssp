import pandas as pd 
import os 

FP_CBF = "cb_factors/cost_factors.xlsx"

cb_factors = pd.ExcelFile(FP_CBF)  

for sheet_name in cb_factors.sheet_names:
    # Load sheet
    cb_table = pd.read_excel(FP_CBF, sheet_name = sheet_name)

    # Define csv output path
    CSV_FP = os.path.join("docs", "cost_factors", f"{sheet_name}.csv")

    cb_table.to_csv(CSV_FP, index = False)

