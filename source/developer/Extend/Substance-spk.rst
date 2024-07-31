.. _SubstanceEx:

*******************************************
Substance Subpackage Structure
*******************************************


Main Goal Of this Subpackage
----------------------------

   The main goals of this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/Substance>`_ are:
   
      * Getting the material properties or data from user to use them in the other subpackages and modules.
      * Present some predefined materials to user.
	  
	  
_GlobalParameters
-----------------

   This subpackage as said is mainly for getting data from user and just one module is enough for this purpose so the `_GlobalParameters.py <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/Substance/_GlobalParameters.py>`_ have no usage in this subpackage and it is leaved empty.
   
   All the parameters that existing modules (mentioned in the following) should return are described in the :ref:`related command page <Material>`:
   
    
		 
Existing modules
----------------
   
   In the following the existing modules for this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/Substance>`_ are described:
   
   .. toctree::
      :maxdepth: 1
   
      Substance-spk/Material
      Substance-spk/DataBank
      