.. _HazardEx:

*******************************************
Hazard Subpackage Structure
*******************************************


Main Goal Of this Subpackage
----------------------------

   The main goals of this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/Hazard>`_ are:
   
      * Getting the natural hazard probabilistic data (Magnitude and probability of occurrence each magnitude)
      * Returning magnitude corresponding to random created samples between zero and 1
	  
	  
_GlobalParameters
-----------------

   In the following tables the existing global parameters and methods in `_GlobalParameters.py <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/Hazard/_GlobalParameters.py>`_ of this subpackage has been shown:
   
      .. csv-table:: Global parameters
         :header: "Parameter", "Description"
         :widths: 20, 40
	     
         `SampledMagnitude <https://github.com/OpenSRANE/OpenSRANE/blob/048f3ac7eb2aabb4729bf81f0b29d58ab6bca15d/opensrane/Hazard/_GlobalParameters.py#LL45C14-L45C30>`_, It shows that each class(in the module) should store the sampled magnitude in each analysis in this parameter.
		 
		 
      .. csv-table:: Global methods
         :header: "Method", "Arguments", "Description"
         :widths: 10, 10, 40
	     
		 SampleRandomMagnitude, rnd [1]_, It shows that each class(in the module) should have this method for returning the magnitude corresponding the entered random variable.
	     wipeAnalysisGlobal, "---", Shows the global parameters that should be initialize and the beginning of each analysis as described :ref:`here <FrameworkGLBP>`.
		 
		 
   .. [1] rnd: Is an argument for getting random variable.
		 
Existing modules
----------------
   
   In the following the existing modules for this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/Hazard>`_ are described:
   
   .. toctree::
      :maxdepth: 1
   
      hazard-spk/Earthquake
      hazard-spk/ConstIM
      