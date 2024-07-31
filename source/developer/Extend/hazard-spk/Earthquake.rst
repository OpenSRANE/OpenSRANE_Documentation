.. _EarthQEx:

*******************************************
Earthquake Module Structure
*******************************************


   The description of this `module <https://github.com/OpenSRANE/OpenSRANE/blob/048f3ac7eb2aabb4729bf81f0b29d58ab6bca15d/opensrane/Hazard/Earthquake.py>`_ presented in this :ref:`Page <hazquake>`. In the following some details about the parameters and methods of this module has been presented.

Parameters
----------

   * All local `parameters <https://github.com/OpenSRANE/OpenSRANE/blob/048f3ac7eb2aabb4729bf81f0b29d58ab6bca15d/opensrane/Hazard/Earthquake.py#L42>`_ of this module are data parameters and filled with arguments and no need to be reset at the beginning of each analysis, so they are not defined in the wipeAnalysis.
   * The SampledMagnitude parameter is a global parameter that described in :ref:`_GlobalParameters <HazardEx>` of parent subpackage and it is located int the `wipeAnalysisGlobal <https://github.com/OpenSRANE/OpenSRANE/blob/048f3ac7eb2aabb4729bf81f0b29d58ab6bca15d/opensrane/Hazard/_GlobalParameters.py#L43>`_ so, there is no need to initialize it again in the body of this module. 

Methods
-------

   * `SampleRandomMagnitude <https://github.com/OpenSRANE/OpenSRANE/blob/048f3ac7eb2aabb4729bf81f0b29d58ab6bca15d/opensrane/Hazard/Earthquake.py#L64>`_ is a global method that described in the :ref:`_GlobalParameters <HazardEx>` of parent subpackage. In the current module this method filled with an algorithm that calculate and returns the SampledMagnitude parameter according defined hazard data using local `parameters <https://github.com/OpenSRANE/OpenSRANE/blob/048f3ac7eb2aabb4729bf81f0b29d58ab6bca15d/opensrane/Hazard/Earthquake.py#L42>`_. The following hypothesists are considered in this method:
      
	  * If there were no rnd or if the value entered as rnd be a number smaller than 0 or greater that 1 then a random number will be consider automatically between 0 and 1.
	  * If the entered value as rnd be less than the defined probabilities for hazard curve, then the maximum defined magnitude will be return as the result of the method.
	  * If the entered value as rnd be greater than the defined probabilities for hazard curve, then 0 value be return as the result of the method.
	  
	  