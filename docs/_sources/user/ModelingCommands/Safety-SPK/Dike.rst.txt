.. _Dike:

Dike Command
------------

.. function:: Safety.Dike(tag, Height=None, Area=None)



   This command is used to define dike objects. By assigning this object to plant units, the outflow area will be limited to the area of defined and assigned dikes.  


   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  Height, float, Hight of the dike.
	  Area, float, Area is surrounded by the dike.

   .. admonition:: Example:
   
      Create some imaginary materials:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.Safety.Dike(4,2,50**2)


Code Developed by: |bsz|