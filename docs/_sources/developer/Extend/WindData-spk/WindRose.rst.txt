.. _WindRoseEx:

*******************************************
Earthquake Module Structure
*******************************************


   The description of this `module <https://github.com/OpenSRANE/OpenSRANE/blob/048f3ac7eb2aabb4729bf81f0b29d58ab6bca15d/opensrane/WindData/WindRose.py>`_ presented in this :ref:`Page <WindRose>`. In the following some details about the parameters and methods of this module has been presented.

Parameters
----------

   * All local parameters of this module are data parameters and filled with arguments and no need to be reset at the beginning of each analysis, so they are not defined in the wipeAnalysis.
   * **DayDirectProbability** and **DayTheta** and **DayCalmn** and also **NightDirectProbability** and **NightTheta** and **NightCalmn** are some internal parameters that describes the probability of wind blast in each direction and also return the directions angle and the probalility of the calm condition. These data are exported from user defined data described in :ref:`Page <WindRose>`. Using **_CalcDirectionProbabilities** method these internal parameters will be calculated.

Methods
-------

   * **GetRandomWindِSample** is a global method that described in the :ref:`_GlobalParameters <WindDataEx>` of parent subpackage. In the current module this method filled with an algorithm that calculates and returns the Sampled wind data parameter according defined data described in :ref:`Page <WindRose>`. The following hypothesists are considered in this method:
      
	  * If :ref:`DateTime <DateTime>` object didn't define, it returns an error and do not calculate sampling data.
	  * Using sampled Day condition it uses data related to day or night.
	  * By sampling a random value between 0 and 1, calculates the other wind parameters and fill them as the response of the method.
	  
   * **_CalcDirectionProbabilities** method is mostly an internal method that specify calm condition probability according user input data and also calculates the mentioned internal parameters (**DayDirectProbability** and **DayTheta** and **DayCalmn** and also **NightDirectProbability** and **NightTheta** and **NightCalmn**) that described in above. 
	  
	  