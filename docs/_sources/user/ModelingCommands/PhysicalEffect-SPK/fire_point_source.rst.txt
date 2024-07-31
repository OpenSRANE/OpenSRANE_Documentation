.. _firepointsource:

fire_point_source Command
-------------------------

.. function:: PhysicalEffect.fire_point_source(tag, minf=0.055, k=1.5, Radiative_Fraction=1)



   This command is for modelling the heat radiation of a burning liquid base on [Ref.1]_. If there were no liquid spread this module do not return any results.


   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  minf, float, is burning velocity for an infinite diameter pool. some sample values are presented in table 3.8 in [Ref.1]_.
	  k, float, constant according table 3.8 in [Ref.1]_.
	  Radiative_Fraction, float, "Radiation factor of heat of combustion, This value will modify the heat of combustion of material. This factor will be multiply in specific heat of combustion of material or substace. [Ref.2]_"



   .. admonition:: Example:
   
      Create some imaginary materials:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.PhysicalEffect.fire_point_source(1,minf=0.0501,k=1.5,Radiative_Fraction=0.4)


.. [Ref.1] `J. Casal, Evaluation of the Effects and Consequences of Major Accidents in Industrial Plants, vol. 8. 2018.`
.. [Ref.2] `Rapid-N docs: https://publications.jrc.ec.europa.eu/repository/bitstream/JRC130323/JRC130323_01.pdf`

Code Developed by: |bsz|