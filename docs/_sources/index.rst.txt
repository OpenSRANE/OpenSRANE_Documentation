.. _home:

.. comment: in the below line add meta data from google search console to verify it on google search engine
.. meta::
   :google-site-verification: urOWf3F5etdxQeLrqblrNbk_blbvilo-RyoLSlAuOak
   
OpenSRANE documentation
=======================
 
.. raw:: html
   
   <p style="font-size: 20px; margin-bottom: 50px"><b style="font-size: 25px">Open S</b>ystem for <b style="font-size: 25px">R</b>isk <b style="font-size: 25px">A</b>ssessment of <b style="font-size: 25px">N</b>aTech <b style="font-size: 25px">E</b>vents</p>

.. admonition:: Latest News

   * New Version Has been released (Version 0.1.4) 11/15/2024 (**ATTENTION**: You should use Python version 3.12.3 for this package and for other versions the released package won't work)

   * New update and loading approach (Ordinary approach) and commands are added to :ref:`Objs_recorder_loader <Objsrecorderloader>` subpackage. 4/23/2024

   * MergeSavedFiles option added to :ref:`Analyze <Analyze>` subpackage commands. 4/23/2024

   * New version of OpenSRANE (Version 0.0.4) Released. 3/21/2024

   * :ref:`Rapid_N_Poolfire_point_source <rapidnpoolfirepointsource>` added to :ref:`PhysicalEffect <PhysicalEffect>` subpackage. 3/21/2024

   * :ref:`fire_point_source <firepointsource>` and :ref:`Simple_fire_point_source <simplefirepointsource>` commands are modified and Radiative_Fraction added to them. 3/21/2024

   * :ref:`ConstIM <constim>` added to :ref:`Hazard <hazSPK>` subpackage. 3/09/2024

   * :ref:`Spherical Tank <sphericaltank>` element added to :ref:`PlantUnits <PlantUnits>` subpackage. 12/23/2023

   * :ref:`Liquefied Petroleum Gas (LPG) <MatDataBank>` Material added to data bank of materials. 12/23/2023

   * :ref:`First Article <references>` of OpenSRANE Released. 11/25/2023

   * Verification of :ref:`PhysicalEffect <PhysicalEffectVF>` verification section completed. Date: 11/18/2023

   * Verification of :ref:`VCE_TNT <VCETNTVF>` added to the documentation. Date: 11/18/2023

   * Verification of :ref:`fire_point_source <firepointsourceVF>` added to the documentation. Date: 11/17/2023

   * Verification of :ref:`DispersionSpreadModels <DispersionSpreadVF>` added to the documentation. Date: 11/10/2023
   

|opr| is an open-source, extensible, flexible and object-oriented software for calculating the quantitative risk of NaTech events in process plants. For performing NaTech analysis using |opr|, **Python** popular scripting language has been extended, by extended we mean additional commands have been added to the languages.
   
The |doc| for using the software and getting familiar with the framework of the software and the platform (|githubLink|) that the package has been located and presented are described here. This documentation is divided to two parts. In the first part (:ref:`Users Guideline`) the procedure of modelling and usage of the program has been described for users and steps of modelling has been explained. In the second part (:ref:`Developers Guideline`) the |opr| framework is described for developers wishing to create their own applications or extend the existing applications.

.. _Users Guideline:

.. toctree::
   :caption: Users Guideline
   :maxdepth: 1

   user/installation
   user/Systemofunits
   user/ModelingStepsDiagram
   user/ModelingCommands
   user/Plot
   user/PostProcessing
   user/Examples
   user/Verifications


.. _Developers Guideline:

.. toctree::
   :caption: Developers Guideline
   :maxdepth: 1

   developer/sourceCode
   developer/build
   developer/extend
   developer/contribute
   developer/issues
   developer/references



.. raw:: html
   
   <script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=080808&w=250&t=n&d=xfUYwOzPIuGXebr4Z0BoBdjTS42lJZQLFhrQ37AeWP8&co=ffffff&ct=808080&cmo=3acc3a&cmn=ff5353'></script>