.. _DSLOC:

DS_LOC Command
**************

.. function:: Connectors.DS_LOC( tag, FragilityTag, OutFlowModelTagList, LOCProbabilityList=None,)


   This command connects a fragility model (Damage state) to its corresponding outflow models and user for each damage state or fragility defines a list of probable outflow models with their corresponding probability and if during the analysis a damage under a fragility happens, then code uses the fragility's outflow models to calculate the following out flow. Such approach has been used to connect probit functions to outflow models and also to connect outflow models to physical events that will be described in the following.


   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  FragilityTag, int, The defined fragility tag that user wants to define its corresponding outflow models. 
	  OutFlowModelTagList, list of int, List of outflow models that can happen after happening defined fragility tag.
	  LOCProbabilityList, list of float, List of the outflow models probabilities that program select a loss of containment (LOC) model according them. 


	  

   .. note::
   
      If user do not enter LOCProbabilityList or enter None, the program will consider a uniform distribution for the defined models. If summation of the defined probabilities does not be equal to unity, program will normal the according their weights to be equal unity.

   .. admonition:: Example:
   
      Create some imaginary materials:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.Connectors.DS_LOC(1,FragilityTag=1,OutFlowModelTagList=[1,2,3,8],LOCProbabilityList=[4,3,2,1])

        opr.Connectors.DS_LOC(2,FragilityTag=2,OutFlowModelTagList=[6,7],LOCProbabilityList=[1,1])



Code Developed by: |bsz|