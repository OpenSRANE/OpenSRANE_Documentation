.. _DateTimeEx:

********************************
DateAndTime Subpackage Structure
********************************

Main Goal Of this Subpackage
----------------------------

   The main goals of this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/DateAndTime>`_ are:

      * Getting the time or date distribution data.
      * Returning a time of day corresponding to random created value between zero and 1.
	  
	  
_GlobalParameters
-----------------

   Currently in this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/DateAndTime>`_ because seems there will be no additional new modules in future and any new feature can be added simply to the available module (if needed). In future if the need of the new modules feels, simply the GlobalParameters.py can be created and added.
   But the parameters and methods that expect to be return from the module of this subpackage are as the following table:
   
      .. csv-table:: Global parameters
         :header: "Parameter", "Description"
         :widths: 20, 40
	     
         SampledisDay, It shows that each class(in the module) should store the sampled isDay in each analysis in this parameter.
		 
		 
      .. csv-table:: Global methods
         :header: "Method", "Arguments", "Description"
         :widths: 10, 10, 40
	     
		 SampleisDay, "---", It shows that each class(in the module) should have this method that specify the Day or night status and should fill the **SampledisDay** parameter with the result.
	     wipeAnalysis, "---", This method initialize **SampledisDay** parameter at the beginning of each analysis with None as described :ref:`here <FrameworkGLBP>`.
   
         
		 
Existing modules
----------------
   
   In the following the existing modules for this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/DateAndTime>`_ are described:
   
   .. toctree::
      :maxdepth: 1
   
      DateAndTime-spk/DateTime