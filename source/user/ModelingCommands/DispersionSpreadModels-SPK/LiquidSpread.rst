.. _LiquidSpread:

LiquidSpread Command
********************

.. function:: DispersionSpreadModels.LiquidSpread(tag, MatTags, OutFlowModelTags, MinDisThickness=0.01, Surface_Roughnesslist=[0.0001, 0.0002], Surface_RoughnessThickness=[0.005, 0.01],)



   As it is obvious from the name of the command this model is used for the liquid dispersion of the liquid substances. It is obvious that user should consider this model for a liquid substance.


   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  MatTags, list of int, List of defined materials that user wants to consider this module for them as their behavior.
	  OutFlowModelTags, list of int, List of outflow models that this model can happen after happening them.
	  MinDisThickness, list of float, "Minimum thickness of the liquid until it has not reached to the dike wall (if dike has been defined before). If user do not define any value for this parameter, it will be considered equal to 0.01 m."
	  Surface_Roughnesslist, list of float, List of existing surfaces roughness’s.
	  Surface_RoughnessThickness, list of float, list of Thickness values corresponding to each Roughnesslist value.



   .. admonition:: Example:
   
      Create some imaginary materials:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.DispersionSpreadModels.LiquidSpread(Tag=1, MatTags=[1,2], OutFlowModelTags=[1,2,3,4],MinDisThickness=0.005,)



Code Developed by: |bsz|