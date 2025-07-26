.. Costs Benefits Analysis documentation master file, created by
   sphinx-quickstart on Sat May 31 11:19:17 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Costs Benefits Analysis (CBA) Documentation
=====================================

The Costs and Benefits module belongs to the SISEPUEDE (sImulation of sEctoral Pathways and Uncertainty Exploration for dEcarbonization) decarbonization toolbox. 

The module evaluate the Costs and Benefits of bottom-up transformations (decarbonization options) using estimates found in the literature of their costs and benefits. 

This includes technical costs or benefits that actors generally experience within a sector and also generally are internal to markets, such as the cost to the agricultural sector of capturing biogas from livestock, the cost of increasing energy efficiency in industry, or the cost of investments in the electricity sector for new capacity to keep up with growing demand. We also include non-technical costs or benefits that are paramount to aligning decarbonization with development goals, such as health benefits of avoided automobile crashes and air pollution, the value of conserving biodiversity, or the time saved thanks to less congestion.

The next table presents a summary of the costs and benefits of transformations across different sectors. Appendices A-G provide additional detail on each of these performance metrics, costs,
and benefits.


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


Contents
--------
.. toc example struct from https://github.com/readthedocs/sphinx_rtd_theme/blob/c9b1bde560d8ee31400e4e4f92f2e8d7a42265ce/docs/index.rst
.. https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html

.. toctree::
   :caption: Getting Started
   :hidden:

   getting_started/installation
   getting_started/quick_start

.. toctree::
   :caption: Cost Factors Description
   :hidden:

   ssp_sectors/agriculture.rst
   ssp_sectors/building.rst
   ssp_sectors/energy_production.rst
   ssp_sectors/forest_land_use.rst
   ssp_sectors/industry.rst
   ssp_sectors/transport.rst
   ssp_sectors/waste.rst

.. toctree::
   :caption: Defining Strategies
   :hidden:
