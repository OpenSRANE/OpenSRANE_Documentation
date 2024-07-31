.. _Fragility:

Fragility Command
*****************

.. function:: Fragilities.Fragility( Tag, modename='No Fragility Mode name', Distribution_Type='normal', mean=1, StdDev=None,)
   
   This command is used for defining the substances using predefined data.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, "Unique integer value that will be used for referring to the defined elements or objects."
	  modename, str, "Name of the corresponding mode that fragility is being define."
	  Distribution_Type, str, "Type of the distribution that is considered for the fragility. Currently there is three types that can be select by the users: 'normal', 'lognormal', 'constant'."
	  mean, float, "mean of the distribution."
	  StdDev, float, Standard deviation of the distribution.

   .. admonition:: Example:
   
      Define some materials using DataBank command:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.Fragilities.Fragility(Tag=1,Distribution_Type='normal',modename='EBF',mean=15,StdDev=2.5)
        
        opr.Fragilities.Fragility(Tag=2,Distribution_Type='lognormal',modename='Gas Failure',mean=15,StdDev=4)		

Code Developed by: |bsz|