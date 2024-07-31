.. _Framework:

*******************
Framework Structure
*******************
|opr| framework consist of a collection of subpackages. There are two types of SubPackages, common subpackages and special subpackages. Special subpackages are the ones that are used for special purposes like Misc (That is for managing modules and special required commands like wipe), Plot and PostProcess that as are obvious from their name are for post processing activities (That maybe remove in future into another Package). Rest of the subpackages are common packages that have the following structure:

.. _SPKStrFig:

.. figure:: figures/SPKStructure.png
	:align: center
	:figclass: align-center

	**Fig.1 - A Subpackage content structure**

.. note::

   | All |opr| subpackages should follow and observe the architecture shown in :ref:`Fig.1 <SPKStrFig>`. 
   | The **__init__.py** and **ObjManager.py** and **_GlobalParameters.py** are constant modules that **should exist in any subpackages and should never change**! 
   

In the following parts of :ref:`Fig.1 <SPKStrFig>` is describing.

   .. toctree::
      :caption: OpenSRANE Framework Details
      :maxdepth: 1
   
      Framework/GlobalParam
      Framework/SubpackageMod
      Framework/HowAddNewMod
      Framework/HowAddNewSubPK
   