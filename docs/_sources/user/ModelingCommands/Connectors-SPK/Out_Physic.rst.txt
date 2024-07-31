.. _OutPhysic:

Out_Physic Command
******************

.. function:: Connectors.Out_Physic( Tag, OutFlowTag, MaterialsTagList, PhysicalEffectTagList, PhysProbabilityList=None,)


   Same definition of :ref:`DS_LOC <DSLOC>` but for connecting each outflow model and material or substance to their corresponding physical effects.


   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  OutFlowTag, int, The defined outflow model tag that user wants to define its corresponding physical effect models. 
	  MaterialsTagList, list of int, List of defined materials that user wants to their corresponding outflow and physical effect.
	  PhysicalEffectTagList, list of int, List of physical effect models that can happen after happening defined OutFlowTag tag.
	  PhysProbabilityList, list of float, List of the outflow models probabilities that program select a loss of containment (LOC) model according them.

	  

   .. note::
   
      If user do not enter PhysProbabilityList or enter None, the program will consider a uniform distribution for the defined models. If summation of the defined probabilities does not be equal to unity, program will normal the according their weights to be equal unity.

   .. admonition:: Example:
   
      Create some imaginary materials:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.Connectors.Out_Physic(Tag=10,OutFlowTag=5, MaterialsTagList=[1,2,3], PhysicalEffectTagList=[3],PhysProbabilityList=[1])

        opr.Connectors.Out_Physic(Tag=11,OutFlowTag=6, MaterialsTagList=[4], PhysicalEffectTagList=[3],PhysProbabilityList=[1])




Code Developed by: |bsz|