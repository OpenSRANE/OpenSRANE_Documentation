.. _DispersionSpreadModelsEx:

*******************************************
DispersionSpreadModels Subpackage Structure
*******************************************
   
Main Goal Of this Subpackage
----------------------------

   The main goals of this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/DispersionSpreadModels>`_ are:

      * Creating the desired Dispersion or Spread model and get the mentioned model parameters from the user.
      * Calculating the dispersion or spread of the substance into the environment and store results in the global parameters to use in other required objects.
	  
	  
_GlobalParameters
-----------------

   In the following tables the existing global parameters and methods in `_GlobalParameters.py <https://github.com/OpenSRANE/OpenSRANE/blob/main/opensrane/DispersionSpreadModels/_GlobalParameters.py>`_ of this subpackage has been shown:
   
      .. csv-table:: Global parameters
         :header: "Parameter", "Description"
         :widths: 20, 40

         MatTags, List of the tag of materials that the model can be implemented for.
         OutFlowModelTags, List of the outflow models that the model can be implemented for.
         t_disp, This parameter is for storing and returning the time step values of the substance dispersion.
         LiquidRadious, This parameter is for storing and returning the dispersed liquid radious at each time step.
         LiquidCenter, This parameter is for storing and returning the dispersed liquid center coordinate at each time step.
         LiquidThickness, This parameter is for storing and returning the dispersed liquid thickness at each time step.
         t_dispLiquidVaporization, This parameter is for storing and returning the time step values of the liquid vaporization.
         LiquidVaporizationMassRate, This parameter is for storing and returning the vaporization mass rate of dispersed liquid at each time step.
         LiquidVaporizationMass, This parameter is for storing and returning the total vaporized mass of dispersed liquid at each time step.
         GasExplosiveMass, This parameter returns the explosive mass of the dispersed gas at each time step.
         GasExplosiveCenterX, This parameter returns the x coordinate of explosive mass center of the dispersed gas at each time step.
         GasExplosiveCenterY, This parameter returns the y coordinate of explosive mass center of the dispersed gas at each time step.
         GasExplosiveCenterZ, This parameter returns the z coordinate of explosive mass center of the dispersed gas at each time step.
         UnitObject, This parameter is to store the object of the plant unit that has damaged and the outflow is calculating for it.
         WindDirection, This parameter stores the sampled wind direction from winddata objects for required calculations.

		 
      .. csv-table:: Global methods
         :header: "Method", "Arguments", "Description"
         :widths: 10, 10, 40
	     
		 Calculate, "---", By calling this method the calculations for outflow will be done and the results will be store in the above global parameters.
         GasConcentration, "x,y,z", This method returns the gas concentration at entered coordinate.
         GiveBoundary, C, This method returns the boundary points that have concentration equal to entered C.
	     wipeAnalysisGlobal, "---", Shows the global parameters that should be initialize and the beginning of each analysis as described :ref:`here <FrameworkGLBP>`.
		 
		 
		 
Existing modules
----------------
   
   In the following the existing modules for this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/DispersionSpreadModels>`_ are described:
   
   .. toctree::
      :maxdepth: 1
   
      DispersionSpreadModels-spk/BritterMcQuaid
      DispersionSpreadModels-spk/GasGaussian
      DispersionSpreadModels-spk/LiquidSpread
      DispersionSpreadModels-spk/LqdSprdGaussianGasDisp