.. _DateTimeMEx:

*******************************************
DateTime Module Structure
*******************************************


   The description of this `module <https://github.com/OpenSRANE/OpenSRANE/blob/048f3ac7eb2aabb4729bf81f0b29d58ab6bca15d/opensrane/DateAndTime/DateTime.py>`_ presented in this :ref:`Page <DateTime>`. In the following some details about the parameters and methods of this module has been presented.

Parameters
----------

   * All local `parameters <https://github.com/OpenSRANE/OpenSRANE/blob/048f3ac7eb2aabb4729bf81f0b29d58ab6bca15d/opensrane/DateAndTime/DateTime.py#L45>`_ of this module are data parameters and filled with arguments and no need to be reset at the beginning of each analysis, so they are not defined in the wipeAnalysis.
   * The SampledisDay parameter is a global parameter that stores the sampled time of day as a boolean that True means it is day. It is located in `wipeAnalysis <https://github.com/OpenSRANE/OpenSRANE/blob/048f3ac7eb2aabb4729bf81f0b29d58ab6bca15d/opensrane/DateAndTime/DateTime.py#L59>`_  and by beginning of each analysis it will be reset and initialize.

Methods
-------

   * `SampleisDay <https://github.com/OpenSRANE/OpenSRANE/blob/048f3ac7eb2aabb4729bf81f0b29d58ab6bca15d/opensrane/DateAndTime/DateTime.py#L64>`_ is a  method that using defined data, determines if it is day or not and stores result in SampledisDay parameter. It creates a random value between zero and one and then regarding the defined day to night ratio, determines if it is day or not.
	  