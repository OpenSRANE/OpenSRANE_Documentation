.. _BritterMcQuaid:

BritterMcQuaid Command
**********************

**a bug exist on this command and soon it will be solve**


.. function:: DispersionSpreadModels.BritterMcQuaid(Tag, MatTags, OutFlowModelTags, C0=1, MassParts=20,)



   This model is used for gas dispersions and its formulation is according [Ref.1]_.


   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  MatTags, list of int, List of defined materials that user wants to consider this module for them as their behavior.
	  OutFlowModelTags, list of int, List of outflow models that can happen after happening defined fragility tag.
	  C0, float, "Initial concentration of the gas at the outflow point. If user do not define any value for this parameter, it will be considered equal to 1."
	  MassParts, int, "to calculate the outflow mass volume, code uses a numerical approach and divide the volume in the range of the LFL and UFL to MassParts parts and do the calculations according these parts."

   .. admonition:: Example:
   
      Create some imaginary materials:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.DispersionSpreadModels.BritterMcQuaid(Tag=2,MatTags=[5],OutFlowModelTags=[6,7], C0=2.84)


.. [Ref.1] `J. Casal, Evaluation of the Effects and Consequences of Major Accidents in Industrial Plants section 7.5.1, vol. 8. 2018.`

Code Developed by: |bsz|