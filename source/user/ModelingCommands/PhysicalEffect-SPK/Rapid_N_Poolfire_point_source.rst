.. _rapidnpoolfirepointsource:

Rapid_N_Poolfire_point_source Command
-------------------------------------

.. function:: PhysicalEffect.Rapid_N_Poolfire_point_source(tag, Radiative_Fraction=1)


   This command is for modelling the heat radiation of a burning pool fire. If there were no liquid spread this module do not return any results. This model is hired from Rapid-N webapp [Ref.2]_, :download:`Equation (8) <files/JRC130323_01.pdf>`.


   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  Radiative_Fraction, float, "Radiation factor of heat of combustion, This value will modify the heat of combustion of material. This factor will be multiply in specific heat of combustion of material or substace. [Ref.2]_"



   .. admonition:: Example:
   
      Create some imaginary materials:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.PhysicalEffect.Rapid_N_Poolfire_point_source(1,Radiative_Fraction=0.4)


.. [Ref.2] `Rapid-N docs: https://publications.jrc.ec.europa.eu/repository/bitstream/JRC130323/JRC130323_01.pdf`

Code Developed by: |bsz|