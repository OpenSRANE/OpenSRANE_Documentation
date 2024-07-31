.. _OutFlowModelEx:

*******************************************
OutFlowModel Subpackage Structure
*******************************************
   
Main Goal Of this Subpackage
----------------------------

   The main goals of this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/OutFlowModel>`_ are:

      * Creating the desired outflow model and get the outflow model parameters from the user.
      * Calculating the outflow and store results in the global parameters to use in other required objects.
	  
	  
_GlobalParameters
-----------------

   In the following tables the existing global parameters and methods in `_GlobalParameters.py <https://github.com/OpenSRANE/OpenSRANE/blob/main/opensrane/OutFlowModel/_GlobalParameters.py>`_ of this subpackage has been shown:
   
      .. csv-table:: Global parameters
         :header: "Parameter", "Description"
         :widths: 20, 40
  	     
         t_release, This parameter is for storing and returning the time step values of the substance outflow.
         MassLiquidReleaseRate, This parameter is for storing and returning the mass outflow rate of the substance in liquid mode in each time step.
         dMassLiquid_release, This parameter is for storing and returning the mass outflow of the substance in liquid mode in each time step.
         TotalMassLiquid_Release, This parameter is for storing and returning the total mass outflow of the substance in liquid mode in each time step.
         MassGasReleaseRate, This parameter is for storing and returning the mass outflow rate of the substance in gas mode in each time step.
         dMassGas_release, This parameter is for storing and returning the mass outflow of the substance in gas mode in each time step.
         TotalMassGas_Release, This parameter is for storing and returning the total mass outflow of the substance in gas mode in each time step.
         UnitObject, This parameter is to store the object of the plant unit that has damaged and the outflow is calculating for it.

  		 
		 
      .. csv-table:: Global methods
         :header: "Method", "Arguments", "Description"
         :widths: 10, 10, 40
	     
		 Calculate, "---", By calling this method the calculations for outflow will be done and the results will be store in the above global parameters.
	     wipeAnalysisGlobal, "---", Shows the global parameters that should be initialize and the beginning of each analysis as described :ref:`here <FrameworkGLBP>`.
		 
		 
		 
Existing modules
----------------
   
   In the following the existing modules for this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/OutFlowModel>`_ are described:
   
   .. toctree::
      :maxdepth: 1
   
      OutFlowModel-spk/GasUnitHole
      OutFlowModel-spk/SimultaniousGas
      OutFlowModel-spk/SimultaniousLiquid
      OutFlowModel-spk/TankHole