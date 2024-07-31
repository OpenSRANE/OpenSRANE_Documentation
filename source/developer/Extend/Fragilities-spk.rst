.. _FragilitiesEx:

*******************************************
Fragilities Subpackage Structure
*******************************************

Main Goal Of this Subpackage
----------------------------

   The main goals of this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/Fragilities>`_ are:

      * Getting the Fragilities and Probits data from the user (Get the probability of fragile, collapse, vulnerability or any type of damage under a magnitude value of external excitation).
      * Returning probability value corresponding to entered damage magnitude.
	  
	  
_GlobalParameters
-----------------

   In the following tables the existing global parameters and methods in `_GlobalParameters.py <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/Fragilities/_GlobalParameters.py>`_ of this subpackage has been shown:
   
      .. csv-table:: Global parameters
         :header: "Parameter", "Description"
         :widths: 20, 40
  	     
         "---", "---"
  		 
		 
      .. csv-table:: Global methods
         :header: "Method", "Arguments", "Description"
         :widths: 10, 10, 40
	     
		 GetProbability, RandomVariable [1]_, It returns the probability value of fragility or probit corresponding to entered RandomVariable.
	     wipeAnalysisGlobal, "---", Shows the global parameters that should be initialize and the beginning of each analysis as described :ref:`here <FrameworkGLBP>`.
		 
		 
   .. [1] RandomVariable: Is the magnitude of damage source.
		 
Existing modules
----------------
   
   In the following the existing modules for this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/Fragilities>`_ are described:
   
   .. toctree::
      :maxdepth: 1
   
      Fragilities-spk/Fragility
      Fragilities-spk/Probit