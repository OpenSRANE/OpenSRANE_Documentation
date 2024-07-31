.. _OpenSRANE1:

***********************************************************************************************
OpenSRANE, a flexible and extensible platform for quantitative risk assessment of NaTech events 
***********************************************************************************************

DOI: `10.22115/SCCE.2023.407882.1685 <https://doi.org/10.22115/scce.2023.407882.1685>`_

In this page the model file of above article and other related files with their description are presented. 


OpenSRANE Model's file
**********************

The model's file can be downloaded from :download:`here <files/OPR1Model.py>`. Both of recorder types has been considered in the model to record the results. Name of object_recorder file is "Recorder" and name of ordinary recorders files are "RecorderA-H". 15 processors considred as parallel analysis cores. 


Postprocessing files
********************
   
By finishing the analysis, the postprocessing of the results was done in jupyter notebook. the following files are the postprocess's jupyter notebook for both type of recorders.

   + ObjectRecorder postprocessing jupyter notebook file: :download:`Download from here <files/OPR1PostProcess(ObjsRecorder).ipynb>`.
   + OrdinaryRecorder postprocessing jupyter notebook file: :download:`Download from here <files/OPR1PostProcess(Recorder).ipynb>`.
	
Both of the above files do same processes and their difference is just in their recordes.

Zero level handy verification
*****************************

To check the results, an independent calculations was done in Excel. To record the results, a macro was written and using the provided button it will be activate. The simulations will be done according the define Simulation Number (cell A4). After finishing the simulations, by entering the zero level scenario name in cells T2 or T3, the probability of the enetered scenario can be seen. 8 tanks modeled with tags 1 to 8 and to enter the zero level scenario name they should be mentioned in order. For example the zero level scenario that tanks 1 and 3 and 6 was damaged is 136 (631 or 613 or 316 are not correct because the order has not been obsereved).

   + The provided excel file can be downloaded from :download:`here <files/OPR1DMLVL0Check.xlsm>`.

	  

By: |bsz|