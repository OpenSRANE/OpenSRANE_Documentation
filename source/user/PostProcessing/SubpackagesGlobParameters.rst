.. _SubGlobPara:

**************************************
Subpackages callable global parameters
**************************************

For any defined object (that has its own tag) after finishing the analysis, user can call the parameters that that are evaluated. Each object has global parameters and also its internal defined parameters. In this part global parameters of each object that users can call and check the resulted values are described.

.. note::
   The called parameters return the results of the current analyzed scenario or current loaded scenario. So, if user get the following parameters after :ref:`MultiParallel <MultiParallel>` analysis command, it just returns the last scenario result. So, if user wants to get all scenario results the following ways are applicable:
   
   * Use :ref:`UniAnalyze <UniAnalyze>` analysis in a loop and call the desired parameters after the analysis command. (Not Suggested)
   
   * Use :ref:`Objs_recorder_loader <Objsrecorderloader>` commands and load the ObjsRecorder file and load it into the memory and then using load1ScenarioOfBank(ScenarioTag) loop on all ScenarioTags and call the desired parameter/s.

Hazard
------

   .. csv-table:: 
      :header: "Parameter", "Description"
      :widths: 10, 40
	  
      SampledMagnitude, Obvious.
	  
   .. admonition:: Example:
      
	  In the following example the Earthquake has defined with tag 1 and its SampledMagnitude has been called.
   
      **Python Code**
   
      .. code-block:: python
		
        opr.Hazard.ObjManager.TagObjDict[1].SampledMagnitude  
		
DateAndTime
-----------

   .. csv-table:: 
      :header: "Parameter", "Description"
      :widths: 10, 40
	  
      Day_Night_Ratio , Defined by user.
	  SampledisDay, A boolean that shows the result of sampling. True shows it is day.
	  
   .. admonition:: Example:
      
	  In the following example the Datetime has defined with tag 1 and its SampledisDay has been called:
   
      **Python Code**
   
      .. code-block:: python
		
        opr.DateAndTime.ObjManager.TagObjDict[1].SampledisDay
		
WindData
-----------

   .. csv-table:: 
      :header: "Parameter", "Description"
      :widths: 10, 40
	  
      WindClass , Class of sampled wind
	  WindDirection, Direction of sampled wind.
	  WindSpeed, Speed of sampled wind.
	  AlphaCOEF, Alpha coefficient of sampled wind.
	  isCalmn, The calm condition of sampled wind. True shows the calm condition.
	  
   .. admonition:: Example:
      
	  In the following example the WindData has defined with tag 1 and its Wind speed has been called:
   
      **Python Code**
   
      .. code-block:: python
		
        opr.WindData.ObjManager.TagObjDict[1].WindSpeed
		
Sites
-----------

   Nothing special to call.
   
Substance
-----------

   Nothing special to call.
   
Fragilities
-----------

   Nothing special to call.
   
Connectors
-----------

   Nothing special to call.
   
Safety
-----------

   Nothing special to call.
   
OutFlowModel
------------

   .. note::
      
	  This class can not be called directly and it should be called from the object(like plant unit) that it was assigned to. Look at the following example.

   .. csv-table:: 
      :header: "Parameter", "Description"
      :widths: 10, 40
	  
      t_release , Returns list of the release time.
	  MassLiquidReleaseRate , Returns list of Liquid release rate at each t_release.
      dMassLiquid_release , Returns list of released mass of the liquid at each t_release.
      TotalMassLiquid_Release , Returns list of total released mass at each t_release.
      MassGasReleaseRate , Returns list of Gas mass release rate at each t_release.
      dMassGas_release , Returns list of released mass of the gas at each t_release.
      TotalMassGas_Release , Returns list of total released mass of gas at each t_release.

	  
   .. admonition:: Example:
      
	  To get list of total gas released of the PlantUnit with tag 1 :
   
      **Python Code**
   
      .. code-block:: python
		
        opr.PlantUnits.ObjManager.TagObjDict[1].OutFlowModelObject.TotalMassGas_Release

DispersionSpreadModels
----------------------

   .. note::
      
	  This class can not be called directly and it should be called from the object(like plant unit) that it was assigned to. Look at the following example.

   .. csv-table:: 
      :header: "Parameter", "Description"
      :widths: 10, 40
	  
      t_disp , Returns list of the Dispersion time.  
      LiquidRadious , Returns list of the liquid radius at each t_disp.
      LiquidCenter , Returns list of the liquid center at each t_disp.
      LiquidThickness , Returns list of the liquid thickness at each t_disp.
      t_dispLiquidVaporization , Returns list of the liquid vaporization time.
      LiquidVaporizationMassRate , Returns list of the vaporization mass rate at each t_dispLiquidVaporization.
      LiquidVaporizationMass , Returns list of the total vaporized mass at each t_dispLiquidVaporization.
      GasExplosiveMass , Returns list of the total explosive mass at each t_dispLiquidVaporization.
      GasExplosiveCenterX , Returns list of the explosive mass x center at each t_dispLiquidVaporization. 
      GasExplosiveCenterY , Returns list of the explosive mass y center at each t_dispLiquidVaporization.
      GasExplosiveCenterZ , Returns list of the explosive mass z center at each.

	  
   .. admonition:: Example:
      
	  To get list of total mass of vaporized gas of the PlantUnit with tag 1 :
   
      **Python Code**
   
      .. code-block:: python
		
        opr.PlantUnits.ObjManager.TagObjDict[1].DispersionSpreadModelObject.GasExplosiveMass


PhysicalEffect
--------------

   .. note::
      
	  This class can not be called directly and it should be called from the object(like plant unit) that it was assigned to. Look at the following example.

   .. csv-table:: 
      :header: "Parameter", "Description"
      :widths: 10, 40
	  
      "Thermal_Radiation_at_Point(x,y,z)", Returns thermal radiation and entered point.
      "RadiationBoundary(Radiation,Height,PointNumber)", Returns Boundary points with equal radiation value equal to entered Radiation and entered height.
      "OverPressure_at_Point(x,y,z)", Returns over pressure value at entered point.
      "OverPressureBoundary(OverPressure, Height, PointNumber)", Returns Boundary points with equal Over pressure value equal to entered Radiation and entered height.
	  
   .. admonition:: Example:
      
	  To get Thermal radiation value of a fired PlantUnit with tag 1 at point with coordinate (5,8,2):
   
      **Python Code**
   
      .. code-block:: python
		
        opr.PlantUnits.ObjManager.Objlst[1].PhysicalEffectObject.Thermal_Radiation_at_Point(5,8,2)	

PlantUnits
--------------

   .. csv-table:: 
      :header: "Parameter", "Description"
      :widths: 10, 40
	  
      DamageSource, Returns damage source name.
      DamageSourceTag, Returns damage source tag.
      DamageSourceDose, Returns damage source dose.
      DamageSourceType, Returns damage source type.
      DamageFragilityTag, Returns Fragility/Probit tag that cause damage.
      DamageLevel, Returns damage level.
      OutFlowModelTag, Returns Outflow model tag.
      OutFlowModelname, Returns Outflow model name.
      OutFlowModelObject, Returns Outflow model object.
      DispersionSpreadModelTag, Returns Dispersion model tag.
      DispersionSpreadModelname, Returns Dispersion model name.
      DispersionSpreadModelObject, Returns Dispersion model Object.
      PhysicalEffectModelTag, Returns Physical effect model tag.
      PhysicalEffectModelname, Returns Physical effect model name.
      PhysicalEffectObject, Returns Physical effect model object.

	  
   .. admonition:: Example:
      
	  To get Damage Source of a damaged PlantUnit with tag 1:
   
      **Python Code**
   
      .. code-block:: python
		
        opr.PlantUnits.ObjManager.Objlst[1].DamageSource	
		
NodesGroup
--------------

   .. csv-table:: 
      :header: "Parameter", "Description"
      :widths: 10, 40
	  
      isDamagedList, Returns list of damage condition of each node    
      DamageSource, Returns list of damage source name of each node      
      DamageSourceTag, Returns list of damage source tag of each node    
      DamageSourceDose, Returns list of damage source dose of each node    
      DamageSourceType, Returns list of damage source type of each node    
      Radiation_Intensity, Returns list of Radiation dose of each node    
      OverPressure_Intensity, Returns list of OverPressure dose of each node    
      Toxic_Intensity, Returns list of Toxic dose of each material of each node
      Radiation_Probit, Returns list of probit value corresponding to the Radiation value at each node [Probit(Radiation)]
      OverPressure_Probit, Returns list of probit value corresponding to the OverPressure value at each node [Probit(OverPressure)]


   .. admonition:: Example:
      
	  To get list of Damage Source of all nodes that defined with NodesGroup tag 1 :
   
      **Python Code**
   
      .. code-block:: python
		
        opr.NodesGroup.ObjManager.Objlst[1].DamageSource