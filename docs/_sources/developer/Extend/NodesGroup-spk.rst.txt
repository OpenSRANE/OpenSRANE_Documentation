.. _NodesGroupEx:

*******************************************
NodesGroup Subpackage Structure
*******************************************
   
Main Goal Of this Subpackage
----------------------------

   The main goals of this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/NodesGroups>`_ are:

      * Define set of the nodes to assess their vulnerability under various physical effects.
	  
	  
_GlobalParameters
-----------------

   In the following tables the existing global parameters and methods in `_GlobalParameters.py <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/NodesGroups/_GlobalParameters.py>`_ of this subpackage has been shown:
   
      .. csv-table:: Global parameters
         :header: "Parameter", "Description"
         :widths: 20, 40
  	     
         Type, Is a string that user specify for created set of the nodes and is useful for postprocess when multiple set of the nodes exist.
		 xGlobalList, list of the local x coordinate of the nodes.
		 yGlobalList, list of the local y coordinate of the nodes.
		 zGlobalList, list of the local z coordinate of the nodes.
		 AreaList, list of the nodes area.
		 IntensityList, list of the intensity of each node.
		 pressure_probit_tag, tag of the defined probit function to be used for calculating vulnerability under overpressure loads.
		 radiation_probit_tag, tag of the defined probit function to be used for calculating vulnerability under heat radiation.
		 Toxic_probit_tag, tag of the defined probit function to be used for calculating vulnerability under toxic materials.
		 isDamagedList, List that shows the damage condition of each node.
		 DamageSource, List that shows the name of subpackage of damage source for each node.
		 DamageSourceTag, List that shows the tag of damage source for each node.
		 DamageSourceDose, List that shows the dose of damage source for each node.
		 DamageSourceType, List that shows the physical effect type for each node.
		 Radiation_Intensity, List that shows the radiation intensity for each node.
		 OverPressure_Intensity, List that shows the overpressure intensiry for each node.
		 Toxic_Intensity, List that shows the toxic dose for each node.
		 Radiation_Probit, List the shows the multiplication of heat radiation value and coresponding probit value for each node.
		 OverPressure_Probit, List the shows the multiplication of overpressure value and coresponding probit value for each node.
		 
		 
		 
      .. csv-table:: Global methods
         :header: "Method", "Arguments", "Description"
         :widths: 10, 10, 40
	     
         wipeAnalysisGlobal, "---", Shows the global parameters that should be initialize and the beginning of each analysis as described :ref:`here <FrameworkGLBP>`.
		 
		 
		 
Existing modules
----------------
   
   In the following the existing modules for this `subpackage <https://github.com/OpenSRANE/OpenSRANE/tree/main/opensrane/NodesGroups>`_ are described:
   
   .. toctree::
      :maxdepth: 1
   
      NodesGroup-spk/Nodes
      NodesGroup-spk/RectangNodes