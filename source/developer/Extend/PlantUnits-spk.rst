.. _PlantUnitsEx:

*******************************************
PlantUnits Subpackage Structure
*******************************************
   
Main Goal Of this Subpackage
----------------------------

   The main goals of this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/PlantUnits>`_ are:

      * Getting the geometrical parameters and local parameters of each plant unit.
      * Assigning the material and various models and properties of each plant unit to its parameters.
      * Assigning the damage condition and data to related parameters during the analysis for post processing.
	  
	  
_GlobalParameters
-----------------

   In the following tables the existing global parameters and methods in `_GlobalParameters.py <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/PlantUnits/_GlobalParameters.py>`_ of this subpackage has been shown:
   
      .. csv-table:: Global parameters
         :header: "Parameter", "Description"
         :widths: 20, 40
  	     
         V_unit, Parameter for total volume of the plant unit.
         V_subs, Parameter for substance volume that has been stored in the plant unit.
         Pressure, Parameter for internal pressure of the plant unit.
         Temperature, Parameter for internal temprature of the plant unit.
         Horizontal_localPosition, Parameter for local horizontal location of the plant unit.
         Vertical_localPosition, Parameter for local vertical location of the plant unit.
         FragilityTagNumbers, Parameter for the list of the fragilities tag of the plant unit.
         SubstanceTag, Parameter for substance tag of the plant unit.
         SafetyTag, Parameter for safety tag of the plant unit.
         Surface_Roughness, Parameter for surface roughness needed for liquid dispersion calculation around the plant unit.
         Ks_Soil_Thermal_conductivity, Parameter needed for liquid dispersion calculation around the plant unit.
         Alphas_Soil_thermal_diffusivity, Parameter for surface roughness needed for liquid dispersion calculation around the plant unit.
         GroundTemperature, Parameter for Ground Temperature around the plant unit.
         pressure_probit_tag, Parameter for probit tag for overpressure excitations.
         radiation_probit_tag, Parameter for probit tag for radiation excitations.
         DikeTag, Parameter for dike tag of the plant unit.
         LastRadiationDose, Parameter to store the dose of last radiation that the vulnerability has been calculated with it.
         RadiationDifferenceDose, "Parameter to store the radiation difference limit. When the increase of radiation become more that this criteria, the damage of the plant unit again will be checked."
         isdamaged, A boolean parameter that shows the damage condition of the plant unit.
         DamageSource, Parameter for storing the name of the subpackage of the damage source.
         DamageSourceTag, Parameter for storing the damage source tag.
         DamageSourceDose, Parameter for stoing the damage source dose.
         DamageSourceType, Parameter for storing the physical effect type of damage source.
         DamageFragilityTag, Parameter for storing the fragility or probit tag that damage is calculated according to it.
         DamageLevel, Parameter for storing the damage level of the plant unit.
         OutFlowModelTag, Parameter for storing the tag of the OutflowModel object.
         OutFlowModelname, Parameter for storing the outflowModel object name.
         OutFlowModelObject, Parameter for storing the outflowModel object.
         DispersionSpreadModelTag, Parameter for storing the tag of the DispersionSpreadModel object.
         DispersionSpreadModelname, Parameter for storing the DispersionSpreadModel object name.
         DispersionSpreadModelObject, Parameter for storing the DispersionSpreadModel object.
         PhysicalEffectModelTag, Parameter for storing the tag of the PhysicalEffectModel object.
         PhysicalEffectModelname, Parameter for storing the PhysicalEffectModel object name.
         PhysicalEffectObject, Parameter for storing the PhysicalEffectModel object.
		 
      .. csv-table:: Global methods
         :header: "Method", "Arguments", "Description"
         :widths: 10, 10, 40
	     
         boundary_points, "---", This method should return a list of the boundary points of the plant unit to be used in the calculating the damages under physical effects.
         wipeAnalysisGlobal, "---", Shows the global parameters that should be initialize and the beginning of each analysis as described :ref:`here <FrameworkGLBP>`.
		 
		 
		 
Existing modules
----------------
   
   In the following the existing modules for this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/PlantUnits>`_ are described:
   
   .. toctree::
      :maxdepth: 1
   
      PlantUnits-spk/ONGStorage