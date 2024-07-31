.. _VCETNT:

VCE_TNT Command
---------------

.. function:: PhysicalEffect.VCE_TNT(tag, Etta=0.03)



   This module is for modelling Vapor Cloud explosion with TNT model [Ref.1]_. This model doesn’t work if no gas dispersion calculated in corresponding dispersion model in the previous step. So, the defined dispersion model should consider gas dispersion and if it models only liquid spread so no results will be back.


   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  Etta, float, Explosion Yield Factor That is between 1% to 10% and it is recommended to be considered equal to 3%.


   .. admonition:: Example:
   
      Create some imaginary materials:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.PhysicalEffect.VCE_TNT(1)


.. [Ref.1] `J. Casal, Evaluation of the Effects and Consequences of Major Accidents in Industrial Plants, vol. 8. 2018.`

Code Developed by: |bsz|