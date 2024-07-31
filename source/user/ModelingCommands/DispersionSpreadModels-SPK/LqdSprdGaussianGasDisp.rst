.. _LqdSprdGaussianGasDisp:

LqdSprdGaussianGasDisp Command
******************************

.. function:: DispersionSpreadModels.LqdSprdGaussianGasDisp( tag, MatTags, OutFlowModelTags, MinDisThickness=0.01, Surface_Roughnesslist=[], Surface_RoughnessThickness=[], Vaporization_Delta_t=10, TotalDuration=1800,     GasConstant=8.31446261815324, GasDispersionXSegments=10, GasDisperstionErrorPercent=1,)


   This command is for modeling the spread of the liquids and then calculate its gas dispersion in the environment. So, it is appropriate for liquids that their gas dispersions are important to be considered. 


   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  MatTags, list of int, List of defined materials that user wants to consider this module for them as their behavior.
	  OutFlowModelTags, list of int, List of outflow models that this model can happen after happening them.
	  MinDisThickness, list of float, "Minimum thickness of the liquid until it has not reached to the dike wall (if dike has been defined before). If user do not define any value for this parameter, it will be considered equal to 0.01 m."
	  Surface_Roughnesslist, list of float, List of existing surfaces roughness’s.
	  Surface_RoughnessThickness, list of float, list of Thickness values corresponding to each Roughnesslist value.
      Vaporization_Delta_t, float, steps time distance for vaporization calculations.
      TotalDuration, float, total time of vaporization. 
      GasDispersionXSegments, int, number of segments that are considered to calculate the dispersion and also dispersed mass of gas.
      GasDisperstionErrorPercent, float, Error percentage for numerical calculations.


   .. admonition:: Example:
   
      Create some imaginary materials:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.DispersionSpreadModels.LqdSprdGaussianGasDisp(tag=4,MatTags=[3,4],OutFlowModelTags=[1,2,3,4],MinDisThickness=0.005,Vaporization_Delta_t=10, TotalDuration=1800,GasConstant=8.31446261815324,GasDispersionXSegments=10,GasDisperstionErrorPercent=1,)



Code Developed by: |bsz|