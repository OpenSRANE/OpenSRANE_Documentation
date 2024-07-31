.. _Safe:

SAFE Command
------------

.. function:: PhysicalEffect.SAFE(tag)



   As obvious from its name, this command is used in case no physical effect even if hazardous material released in environment. 


   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.

   .. admonition:: Example:
   
      Create some imaginary materials:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.PhysicalEffect.SAFE(1)


Code Developed by: |bsz|