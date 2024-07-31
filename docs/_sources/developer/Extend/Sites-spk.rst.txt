.. _SitesEx:

*******************************************
Sites Subpackage Structure
*******************************************


Main Goal Of this Subpackage
----------------------------

   The main goals of this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/Sites>`_ are:
   
      * Getting the site/s data.
	  
	  
_GlobalParameters
-----------------

   Currently in this subpackage there is no special parameters or methods and there is no special comment on this subpackage. So, all input parameters defined in the site module and the `_GlobalParameters.py <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/Sites/_GlobalParameters.py>`_ is empty.
   But the parameters and methods that expect to be return from the module of this subpackage are as the following table that also described in the :ref:`related command page <site>`:
   
      .. csv-table:: Global parameters
         :header: "Parameter", "Description"
         :widths: 20, 40
	     
         Temperature, This prameter will be taken from user and stores the site temprature. 
		 Pressure, This prameter will be taken from user and stores the site pressure. 
		 g, This prameter will be taken from user and stores the site gravity acceleration. 
		 OngroundTemprature, This prameter will be taken from user and stores the site onground temprature. 
		 Airdensity, This prameter will be taken from user and stores the site air density. 
		 Humidity, This prameter will be taken from user and stores the site humidity. 
		 
		 
		 
      .. csv-table:: Global methods
         :header: "Method", "Arguments", "Description"
         :widths: 10, 10, 40
	     
		 "---", "---", There is no method for this subpackage.
   
Existing modules
----------------
   
   In the following the existing modules for this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/Sites>`_ are described:
   
   .. toctree::
      :maxdepth: 1
   
      Sites-spk/Site