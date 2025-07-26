===========
Usage
===========

.. code-block:: python

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



Some features of the module
=============================

The ``get_cb_var_fields`` method allows us to obtain information about the cost variable

.. code-block:: python

    cb.get_cb_var_fields(cb_var_name = "cb:trns:air_pollution:X:diesel")

.. code-block:: text

    CostFactor(
            output_variable_name = cb:trns:air_pollution:X:diesel,
            difference_variable = energy_consumption_trns_public_diesel|energy_consumption_trns_road_heavy_freight_diesel|energy_consumption_trns_road_heavy_regional_diesel|energy_consumption_trns_road_light_diesel,
            multiplier = -8471713.0,
            multiplier_unit = $/PJ,
            annual_change = 1.0,
            output_display_name = Transport air pollution (diesel),
            sum = False,
            natural_multiplier_units = $0.31/l diesel      ,
            display_notes = We use the IMFÃs fossil fuel subsidies database (2021) to estimate the avoided air pollution costs of fossil fuels used for road transport, averaged across LAC.,
            internal_notes = none,
            cb_function = cb_apply_cost_factors,
            cb_var_group = trns_air_pollution_cost_factors) 


The method ``get_all_cost_factor_variables`` retrieve all the cost variables by querying the TXTable table

.. code-block:: python

    cb.get_all_cost_factor_variables()


The method ``get_all_cost_factor_variables`` retrieve all the cost variables by querying the CostFactor table

.. code-block:: python

    cb.get_cost_factors()

The method ``get_technical_costs`` retrieve all the transformation cost by querying the TransformationCost table 

.. code-block:: python

    cb.get_technical_costs()

The method ``update_cost_factor_register`` allow us update a specific register of the ``CostFactor`` and ``TransformationCost`` tables.

For example, we can to update the multiplier and annual_change fields from the ``cb:trns:air_pollution:X:diesel`` variable.

Lets see the default fields of the ``cb:trns:air_pollution:X:diesel`` variable

.. code-block:: python
    cb.get_cb_var_fields(cb_var_name = "cb:trns:air_pollution:X:diesel")

.. code-block:: text 

    CostFactor(
		output_variable_name = cb:trns:air_pollution:X:diesel,
		difference_variable = energy_consumption_trns_public_diesel|energy_consumption_trns_road_heavy_freight_diesel|energy_consumption_trns_road_heavy_regional_diesel|energy_consumption_trns_road_light_diesel,
		multiplier = -8471713.0,
		multiplier_unit = $/PJ,
		annual_change = 1.0,
		output_display_name = Transport air pollution (diesel),
		sum = False,
		natural_multiplier_units = $0.31/l diesel      ,
		display_notes = We use the IMFÃs fossil fuel subsidies database (2021) to estimate the avoided air pollution costs of fossil fuels used for road transport, averaged across LAC.,
		internal_notes = none,
		cb_function = cb_apply_cost_factors,
		cb_var_group = trns_air_pollution_cost_factors) 

We will update the multiplier from -8471713.0 to -6471713.0 and the annual_change from 1.0 to 1.2.

.. code-block:: python

    cb.update_cost_factor_register(cb_var_name = "cb:trns:air_pollution:X:diesel", 
                                   cb_var_fields = {"multiplier" : -6471713.0, "annual_change" : 1.2})

Verify the update

.. code-block:: python

    cb.get_cb_var_fields(cb_var_name = "cb:trns:air_pollution:X:diesel")

.. code-block:: text 

    CostFactor(
		output_variable_name = cb:trns:air_pollution:X:diesel,
		difference_variable = energy_consumption_trns_public_diesel|energy_consumption_trns_road_heavy_freight_diesel|energy_consumption_trns_road_heavy_regional_diesel|energy_consumption_trns_road_light_diesel,
		multiplier = -6471713.0,
		multiplier_unit = $/PJ,
		annual_change = 1.2,
		output_display_name = Transport air pollution (diesel),
		sum = False,
		natural_multiplier_units = $0.31/l diesel      ,
		display_notes = We use the IMFÃs fossil fuel subsidies database (2021) to estimate the avoided air pollution costs of fossil fuels used for road transport, averaged across LAC.,
		internal_notes = none,
		cb_function = cb_apply_cost_factors,
		cb_var_group = trns_air_pollution_cost_factors) 

The method ``update_all_cost_factors_table`` receive a dataframe and update the ``CostFactor`` Table. 
For example, if we want to reduce all the cost factor multipliers on 50%, we will do the next

.. code-block:: python 

    cost_factor_table["multiplier"] *= 0.5
    cb.update_all_cost_factors_table(cost_factor_table)

The method ``update_all_technical_costs_table`` receive a dataframe and update the ``TransformationCost`` Table
For example, if we want to reduce all the cost factor multipliers on 50%, we will do the next

.. code-block:: python

    transformation_cost_table["multiplier"] *= 0.5
    cb.update_all_technical_costs_table(transformation_cost_table)

We can save the current configuration of the cost tables in an excel file:

.. code-block:: python
    
    UPDATED_CB_DEFAULT_DEFINITION_FILE_PATH = os.path.join(CB_DEFAULT_DEFINITION_PATH, "updated_cb_config_params_croatia_tornado.xlsx")

    cb.export_db_to_excel(UPDATED_CB_DEFAULT_DEFINITION_FILE_PATH)


Once the excel file is saved, we can load it and update the program's database.

The program does not need to load this excel file for its execution. We use the load_cb_parameters method to show a functionality of the program

.. code-block:: python 
    
    cb.load_cb_parameters(CB_DEFAULT_DEFINITION_FILE_PATH)


Compute Costs and Benefits individually
========================================

The ``compute_cost_benefit_from_variable`` method computes the costs or benefits of a cost variable for any of the strategies. 

This method defaults to the base strategy defined when instantiating the ``CostBenefits`` class. 

We can modify the comparison strategy by adding the new baseline strategy to the ``strategy_code_base`` argument, for example:

.. code-block:: python
    
    cb.compute_cost_benefit_from_variable(cb_var_name = 'cb:trns:technical_cost:efficiency:non_electric', 
                                      strategy_code_tx = 'PFLO:NZ')

The method ``compute_system_cost_for_strategy`` calculates all system costs for a specific strategy

.. code-block:: python

    cb.compute_system_cost_for_strategy(strategy_code_tx = 'PFLO:NZ')

The method ``compute_technical_cost_for_strategy`` calculates all technical costs for a specific strategy

.. code-block:: python
    
    cb.compute_technical_cost_for_strategy(strategy_code_tx = 'PFLO:NZ')

The ``compute_system_cost_for_all_strategies`` method compute all system cost for all strategies

.. code-block:: python
    
    results_system = cb.compute_system_cost_for_all_strategies()

The ``compute_technical_cost_for_all_strategies`` method compute all technical cost for all strategies

.. code-block:: python
    
    results_tx = cb.compute_technical_cost_for_all_strategies()