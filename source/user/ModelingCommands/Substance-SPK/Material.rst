.. _Material:

Material Command
****************

.. function:: Substance.Material(Tag, name='No name', Density=None, GasDensity=None, Dynamic_Viscousity=None, Molar_Heat_of_Combustion=None, Stoichiometric_Concentration=None,  Vapour_Density=None, Volumetric_Heat_Capacity=None, Molecular_Weight=None, Molar_Volume=None, Boiling_Point=None, Critical_Pressure=None, Critical_Temperature=None, Melting_Point=None, Standard_Enthalpy_of_Formation=None, Vapour_Pressure=None, Molar_Enthalpy_of_Vaporization=None, Specific_Heat_of_Vaporization=None, Molar_Heat_Capacity=None, Specific_Heat_Capacity=None, Specific_Heat_Ratio=None, Autoignition_Temperature=None, Flash_Point=None, Specific_Heat_of_Combustion=None, Lower_Flammability_Limit=None, Upper_Flammability_Limit=None, Bioconcentration_Factor=None, Liquid_Partial_Pressure_in_Atmosphere=None,)


   This command is used for defining the substances.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  name, str, Name of Material. 
	  Density, float, A Property of material.
	  GasDensity, float, A Property of material. 
	  Dynamic_Viscousity, float, A Property of material. 
	  Molar_Heat_of_Combustion, float, A Property of material. 
	  Stoichiometric_Concentration, float, A Property of material. 
	  Vapour_Density, float, A Property of material. 
	  Volumetric_Heat_Capacity, float, A Property of material. 
	  Molecular_Weight, float, A Property of material. 
	  Standard_Enthalpy_of_Formation, float, A Property of material. 
	  Vapour_Pressure, float, A Property of material. 
	  Molar_Enthalpy_of_Vaporization, float, A Property of material. 
	  Specific_Heat_of_Vaporization, float, A Property of material. 
	  Molar_Heat_Capacity, float, A Property of material. 
	  Specific_Heat_Capacity, float, A Property of material. 
	  Specific_Heat_Ratio, float, A Property of material. 
	  Autoignition_Temperature, float, A Property of material. 
	  Flash_Point, float, A Property of material. 
	  Specific_Heat_of_Combustion, float, A Property of material. 
	  Lower_Flammability_Limit, float, A Property of material. 
	  Upper_Flammability_Limit, float, A Property of material. 
	  Bioconcentration_Factor, float, A Property of material. 
	  Liquid_Partial_Pressure_in_Atmosphere, float, A Property of material. 

	  

   .. note::
   
      Attention that there is no need to define all properties for a material. Some properties also are for gases and some other are only for liquid. Depending on the outflow, dispersion, fire or explosion models that are selected for the material (in modeling procedure), the software create warning in the case of lack of material required properties.

   .. admonition:: Example:
   
      Create some imaginary materials:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.Substance.Material(Tag=1,name='None',Density=250, Specific_Heat_of_Combustion=45.334*10**6)
        
        opr.Substance.Material(2,name='Imaginary Material', Density=123,Vapour_Density=125, Specific_Heat_of_Combustion=45.334*10**6,)		


Code Developed by: |bsz|