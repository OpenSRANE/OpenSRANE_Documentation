.. _TankHoleSeries:

TankHoleSeries Commands
***********************

4 models that start with TankHole (TankHole, TankHoleInitRate, TankHoleDuration, TankHoleFixStep) models **Liquids** outflow from a hole in the body of the tank with small changes to each other. TankHole models the outflow until the outflow volume become equal to the Tank containment volume, TankHoleInitRate is same TankHole model with outflow rate equal to the initial rate, TankHoleDuration is same Tankhole model but its calculations will be stop when the release duration become equal to defined duration and TankHoleFixStep is same TankHole but with limited steps of calculations. Models are according [Ref.1]_. 

.. function:: OutFlowModel.TankHole(Tag, Hole_Diameter=0.01, Hole_Height_FromBot=0, delta_t=0.1, Cd=1,)

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  "Hole_Diameter", float, Diameter of the hole that liquid release.
	  "Hole_Height_FromBot", float, the height of the hole from the ground.
	  "delta_t", float, Calculation steps time interval.
	  Cd, float, Discharge coefficient ≤1.

   .. admonition:: Example:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.OutFlowModel.TankHole(Tag, Hole_Diameter=0.05, Hole_Height_FromBot=0, delta_t=500, Cd=1)


.. function:: OutFlowModel.TankHoleInitRate(Tag, Hole_Diameter=0.01, Hole_Height_FromBot=0, delta_t=0.1, Cd=1,)
   
   In this model the initial rate of outflow will be consider constant.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      -, -, Parameters are same as before.

   .. admonition:: Example:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.OutFlowModel.TankHoleInitRate(2, Hole_Diameter=0.01, Hole_Height_FromBot=1, delta_t=500, Cd=0.62)


.. function:: OutFlowModel.TankHoleDuration(Tag, Hole_Diameter=0.01, Hole_Height_FromBot=0, delta_t=0.1, Cd=1, Duration=100)

    In this model the duration of outflow is limited to defined Duration.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
	  Duration, float, Total duration of outflow
      -, -, Other parameters are same as before.	  

   .. admonition:: Example:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.OutFlowModel.TankHoleDuration(3, Hole_Diameter=0.5, Hole_Height_FromBot=0.5, delta_t=500, Cd=0.62,Duration=3000)


.. function:: OutFlowModel.TankHoleFixStep(Tag, Hole_Diameter=0.01, Hole_Height_FromBot=0, delta_t=0.1, Cd=1, StepNumber=30)

    In this model the calculations steps are limited to the defined StepNumber.		
	
   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
	  StepNumber, int, The number or calculations steps.
      -, -, Other parameters are same as before.	  

   .. admonition:: Example:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.OutFlowModel.TankHoleFixStep(4, Hole_Diameter=0.5, Hole_Height_FromBot=0.5, delta_t=500, Cd=0.62,StepNumber=30)
		

.. [Ref.1] `J. Casal, Evaluation of the Effects and Consequences of Major Accidents in Industrial Plants, vol. 8. 2018.`

Code Developed by: |bsz|