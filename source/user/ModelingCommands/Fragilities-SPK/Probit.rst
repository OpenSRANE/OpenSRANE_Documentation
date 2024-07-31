.. _Probit:

Probit Command
**************

.. function:: Fragilities.Probit( Tag, Distribution_Type='normal', K1=1, K2=0.5, Scale_Factor=1, MinRndVar=0)


   This command is used to define the structures vulnerability to the physical effects. Obviously one of its axes is the magnitude of the physical effect (Radiation, Overpressure, Toxic) that this model is considered for.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, "Unique integer value that will be used for referring to the defined elements or objects."
	  Distribution_Type, str, "Type of the distribution that is considered for the fragility. Currently there is three types that can be select by the users: 'normal', 'lognormal'."
	  "K1, K2", float, "Probit Normal (:math:`Y=K_1 x+K_2`) and Lognormal (:math:`Y=K_1  ln⁡x+K_2`) coefficients."
	  Scale_Factor, float, "Scale factor for magnitude of the physical effect that converts the Probit magnitude values to the SI system."
	  MinRndVar, float, "A value that will be consider as the minimum intensity of random variable and the defined probit function returns 0 for random variables less than this value (Example: if minimum radiation that injure is 4 this value should be enter 4 then for any value less or equal to 4 its probit will return 0 as the probit probability)"


   .. admonition:: Example:
   
      Create some imaginary materials:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        Radiation=5
        opr.Fragilities.Probit(Tag=Radiation, Distribution_Type='lognormal', K1=2, K2=-30.9,Scale_Factor=1000)

        OverPressure=6
        opr.Fragilities.Probit(Tag=OverPressure, Distribution_Type='normal', K1=1.37, K2=-1.47,Scale_Factor=1000)

        Toxic=7
        opr.Fragilities.Probit(Tag=Toxic, Distribution_Type='lognormal', K1=0.71, K2=-9.82)




Code Developed by: |bsz|