.. _FragilityEx:

*******************************************
Fragility Module Structure
*******************************************


   The description of this `module <https://github.com/OpenSRANE/OpenSRANE/blob/048f3ac7eb2aabb4729bf81f0b29d58ab6bca15d/opensrane/Fragilities/Fragility.py>`_ presented in this :ref:`Page <Fragility>`. In the following some details about the parameters and methods of this module has been presented.

Parameters
----------

   * All local `parameters <https://github.com/OpenSRANE/OpenSRANE/blob/048f3ac7eb2aabb4729bf81f0b29d58ab6bca15d/opensrane/Fragilities/Fragility.py>`_ of this module are data parameters and filled with arguments and no need to be reset at the beginning of each analysis, so they are not defined in the wipeAnalysis.


Methods
-------

   * `GetProbability <https://github.com/OpenSRANE/OpenSRANE/blob/048f3ac7eb2aabb4729bf81f0b29d58ab6bca15d/opensrane/Fragilities/Fragility.py>`_ is a global method that described in the :ref:`_GlobalParameters <FragilitiesEx>` of parent subpackage. In the current module this method returns the probability of entered damage magnitude depending the type of defined distribution. The Scipy library has been used to do the calculations. 

   * `_constant <https://github.com/OpenSRANE/OpenSRANE/blob/048f3ac7eb2aabb4729bf81f0b29d58ab6bca15d/opensrane/Fragilities/Fragility.py>`_ is an internal method of this module. This method creates a constant distribution type and for any random variable it returns 1 as the probability of damage.
	  
	  