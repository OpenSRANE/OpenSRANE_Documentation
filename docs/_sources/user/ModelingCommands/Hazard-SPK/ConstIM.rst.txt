.. _constim:

ConstIM Command
******************

.. function:: Hazard.ConstIM(Tag,DefType,IM=0)
   
   Using this command a defined Intensity Measure (IM) will be consider as the simulated IM in all Simulations. 

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  DefType, str, Specifies the type of the earthquake magnitude. Currently it has no effect on the program process and the input is only as a string.
	  IM, float, Value of Intensity Measure (IM) that will be consider as the simulated IM in all simulations.

   .. note::
      
	  If user used this command without assigning any value to IM, then 0 will be consider for it!

   .. admonition:: Example:
   
      The following demonstrates the use of the ConstIM command.
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        #Create Hazard Object with Tag=1 and a constant IM equal to 0.99 is considered for it.
        opr.Hazard.ConstIM(1,'PGA',IM=0.99) 


Code Developed by: |bsz|