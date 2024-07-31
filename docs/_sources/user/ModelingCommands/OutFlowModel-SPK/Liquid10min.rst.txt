.. _Liquid10min:

Liquid10min Command
*******************

.. function:: OutFlowModel.Liquid10min(Tag)
   
   Very simple model that calculate the outflow of whole capacity of liquid in 10 minutes with a constant rate.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.


   .. admonition:: Example:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.OutFlowModel.Liquid10min(Tag=1)

Code Developed by: |bsz|