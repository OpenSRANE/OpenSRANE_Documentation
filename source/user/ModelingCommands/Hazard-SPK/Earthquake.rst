.. _hazquake:

Earthquake Command
******************

.. function:: Hazard.Earthquake(Tag,DefType,Magnitude,Probabilities)
   
   Obviously this command is used for defining earthquake hazard. 

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  DefType, str, Specifies the type of the earthquake magnitude. Currently it has no effect on the program process and the input is only as a string.
	  Magnitude, list of float, list of the magnitude values.
	  Probabilities, list of float, list of the probability values corresponding to the magnitude values.

   .. note::
      
	  Values less than the first value will be consider as zero.

   .. admonition:: Example:
   
      The following demonstrates the use of the Earthquake command.
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        #Generate a Seismic Hazard Object
        PGA=[x/2 for x in range(41) ]
        Prob=[(40-x)**(1/3)/40**(1/3) for x in range(41)]
		
        #Create Hazard Object with Tag=1 that is 0th Object
        opr.Hazard.Earthquake(1,'PGA',PGA,Prob) 


Code Developed by: |bsz|