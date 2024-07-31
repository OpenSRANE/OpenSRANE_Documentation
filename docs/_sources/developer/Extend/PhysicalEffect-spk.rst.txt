.. _PhysicalEffectEx:

*******************************************
PhysicalEffect Subpackage Structure
*******************************************
   
Main Goal Of this Subpackage
----------------------------

   The main goals of this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/PhysicalEffect>`_ are:

      * Calculate the physical effect like heat radiation and overpressure and toxic dose as well in any required point.
      * Calculate the boundary points that have equal dose values.
	  
	  
_GlobalParameters
-----------------

   In the following tables the existing global parameters and methods in `_GlobalParameters.py <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/PhysicalEffect/_GlobalParameters.py>`_ of this subpackage has been shown:
   
      .. csv-table:: Global parameters
         :header: "Parameter", "Description"
         :widths: 20, 40
  	     
         UnitObject, This parameter is to store the object of the plant unit that has damaged and the outflow is calculating for it.

  		 
		 
      .. csv-table:: Global methods
         :header: "Method", "Arguments", "Description"
         :widths: 10, 10, 40
	     
		 Calculate, "---", By calling this method the calculations for outflow will be done and the results will be store in the above global parameters.
         Thermal_Radiation_at_Point, "x,y,z", By calling this method the heat radiation at entered coordinate should be calculated and returned.
         OverPressure_at_Point, "x,y,z", By calling this method the overpressure at entered coordinate should be calculated and returned.
         Toxic_at_Point, "x,y,z", By calling this method the toxic dose at entered coordinate should be calculated and returned.
         RadiationBoundary, "Radiation, Height, PointNumber", By calling this method boudary points with dose equal to Radiation and height equal to Height should be return. The number of points are equal PointNumber that distributed uniformly in the boundary.
         OverPressureBoundary, "OverPressure, Height, PointNumber", By calling this method boudary points with dose equal to OverPressure and height equal to Height should be return. The number of points are equal PointNumber that distributed uniformly in the boundary.
	     wipeAnalysisGlobal, "---", Shows the global parameters that should be initialize and the beginning of each analysis as described :ref:`here <FrameworkGLBP>`.
		 
		 
		 
Existing modules
----------------
   
   In the following the existing modules for this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/PhysicalEffect>`_ are described:
   
   .. toctree::
      :maxdepth: 1
   
      PhysicalEffect-spk/fire_point_source
      PhysicalEffect-spk/SAFE
      PhysicalEffect-spk/Simple_fire_point_source
      PhysicalEffect-spk/VCE_TNT