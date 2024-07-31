.. _GasUnitHole:

GasUnitHole Command
********************************************************

.. function:: OutFlowModel.GasUnitHole(tag,Hole_Diameter=0.01, Total_t=20, Cd=1, Gas_Constant=8.31446261815324)
   
   This command models gas outflow from a hole using the following flowchart from [Ref.1]_. 

   .. figure:: figures/GasHoleAlgorithm.png
      :align: center
      :figclass: align-center
      
      GasUnitHole command flowchart
	
   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  "Hole_Diameter", float, Diameter of the hole that gas is releasing from.
	  "Total_t", float, Total duration of outflow
	  Cd, float, Explained in [Ref.1]_.
	  Gas_Constant, float, Gas Constant


   .. admonition:: Example:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.OutFlowModel.GasUnitHole(2, Hole_Diameter=0.02, Total_t=40, Cd=0.62, Gas_Constant=8.31446261815324,)

.. [Ref.1] `J. Casal, Evaluation of the Effects and Consequences of Major Accidents in Industrial Plants, vol. 8. 2018.`

Code Developed by: |bsz|