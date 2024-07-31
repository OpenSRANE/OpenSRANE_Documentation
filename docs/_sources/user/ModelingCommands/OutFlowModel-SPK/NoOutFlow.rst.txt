.. _NoOutFlow:

NoOutFlow Command
*****************

.. function:: OutFlowModel.NoOutFlow(Tag)
   
   This model consider 0 for amount of outflow mass and rate and other results for cases that there is no outflow.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.


   .. admonition:: Example:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.OutFlowModel.NoOutFlow(Tag=1)

Code Developed by: |bsz|