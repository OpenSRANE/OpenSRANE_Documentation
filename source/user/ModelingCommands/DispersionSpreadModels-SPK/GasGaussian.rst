.. _GasGaussian:

GasGaussian Command
-------------------

.. function:: DispersionSpreadModels.GasGaussian(tag, MatTags, OutFlowModelTags, OutFlowHeight=1, GasConstant=8.31446261815324, GasDispersionXSegments=10, GasDisperstionErrorPercent=1)



   This model is used for gas dispersions and its formulation is but with gaussian algorithm according [Ref.1]_. It is assumed that the outflow happen from a point and the point height is considered as the height of the outflow point location. The gas concentration will be considered according gas outflow values, so if the outflow model does not consider any outflow values so, this module, do not calculate any dispersion because of no gas outflow.


   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  MatTags, list of int, List of defined materials that user wants to consider this module for them as their behavior.
	  OutFlowModelTags, list of int, List of outflow models that can can cause this type of dispersion.
	  OutFlowHeight, float, Hight that gas is outflowing.
	  GasConstant, float, List of existing surfaces roughness`s.
	  GasDispersionXSegments, int, number of segments that are considered to calculate the dispersion and also dispersed mass of gas.
      GasDisperstionErrorPercent, float, Error percentage for numerical calculations.



   .. admonition:: Example:
   
      Create some imaginary materials:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.DispersionSpreadModels.GasGaussian(tag=1,MatTags=[1], OutFlowModelTags=[1,2,3,4])


.. [Ref.1] `J. Casal, Evaluation of the Effects and Consequences of Major Accidents in Industrial Plants section 7.4, vol. 8. 2018.`


Code Developed by: |bsz|