.. _PbLOC:

Pb_LOC Command
**************

.. function:: Connectors.Pb_LOC( tag, ProbitTag, OutFlowModelTagList, LOCProbabilityList=None,)



   Same definition of :ref:`DS_LOC <DSLOC>` but for connecting each probit model to its corresponding physical effects.


   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  ProbitTag, int, The defined probit model tag that user wants to define its corresponding physical effect models.
	  OutFlowModelTagList, list of int, List of outflow models that can happen after happening defined probit tag.
	  LOCProbabilityList, list of float, List of the outflow models probabilities that program select a loss of containment (LOC) model according them. 


	  

   .. note::
   
      If user do not enter LOCProbabilityList or enter None, the program will consider a uniform distribution for the defined models. If summation of the defined probabilities does not be equal to unity, program will normal the according their weights to be equal unity.

   .. admonition:: Example:
   
      Create some imaginary materials:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.Connectors.Pb_LOC(tag=13, ProbitTag=5,  OutFlowModelTagList=[1,2,3,4,5],  LOCProbabilityList=[1,1,1,1,1])



Code Developed by: |bsz|