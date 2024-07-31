.. _VCETNTVF:

******************************************
VCE_TNT Module Verification 
******************************************

The VCE TNT model is formulated according model explained in Casal book [Ref.1]_. To validate the calculations of this module, example 4.1 of Casal book chose. The following code model the example condition and the final result is checked by example results.

The below codes can be downloaded from :download:`here <files/VCE_TNT.ipynb>` in Jupyter Notebook format.

.. admonition:: Verification:  

   .. code-block:: python
   
      opr.wipe()

      #Define Wind Rose 
      windobj=opr.WindData.WindRose(1)
      windobj.WindSpeed=0
      windobj.WindDirection=90
      
      #Define Site Condition and Geometry
      SiteTAg=1
      obj=opr.Sites.Site(SiteTAg, Temperature=16+273, Pressure=1.013*10**5, XSiteBoundary=[0,100,100,0], YSiteBoundary=[0,0,100,100],
                         g=9.81,Humidity=0.79,Airdensity=0.270)
      
      #Define Substance
      propane=1
      subsobj=opr.Substance.Material(propane,name='Propane',Density=553,GasDensity=1,BoilingPointGasDensity=2.32, Specific_Heat_Ratio=1.15,
                                     Molecular_Weight=44.1/1000, Specific_Heat_of_Combustion=43.930*10**6,
                                     Lower_Flammability_Limit=0.2, Upper_Flammability_Limit=0.7,)
      
      #Define OutFlow Model
      OutflowObj=opr.OutFlowModel.GasUnitHole(tag=1, Hole_Diameter=0.1, Total_t=20, Cd=1, Gas_Constant=8.31446261815324)
      
      #Define Dispersion Model
      DispObj=opr.DispersionSpreadModels.BritterMcQuaid(tag=1, MatTags=1, OutFlowModelTags=[1], MassParts=20,)
      
      #Define Dike for Tanks
      opr.Safety.Dike(1,0,3.1415*6**2/4)
      
      #Define Plant Unit 
      PlantObj=opr.PlantUnits.ONGStorage(1,SiteTag=1,DikeTag=1, SubstanceTag=1,  Diameter=10, Pressure= 1.769025*10**5, Temperature=16+273,
                                         Horizontal_localPosition=0,    Vertical_localPosition=0,
                                         Height=20,SubstanceVolumeRatio=0.9)
      
      #Manually define OutFlow Model for above Unit Object
      PlantObj.OutFlowModelObject=OutflowObj
      OutflowObj.UnitObject=PlantObj
      PlantObj.OutFlowModelObject.Calculate()
      
      
      #Manually define DispersionSpread Model for above Unit Object
      PlantObj.DispersionSpreadModelObject=DispObj
      PlantObj.DispersionSpreadModelObject.UnitObject=PlantObj
      PlantObj.DispersionSpreadModelObject.Calculate()
      
      print("Exposive mass =",DispObj.GasExplosiveMass)
      print("Explosive Mass center = ", DispObj.GasExplosiveCenterX,DispObj.GasExplosiveCenterY,DispObj.GasExplosiveCenterZ)
      
      
      
      obj=opr.PhysicalEffect.VCE_TNT(1)
      obj.UnitObject=PlantObj
      obj.Calculate()
      dP=obj.OverPressure_at_Point(DispObj.GasExplosiveCenterX[0]+500,0,0)
      print("The Over Pressure Value in 500 m Over Explosive mass Center =",dP/10**5, " Bar")
      
      print('in casal Example 4.1, \nd=500 m \nM (Explosive Mass)= 30,000 \nDeltaHc=43930*1000')
      print('And the result of over pressure is = 0.049 Bar')
      print('That is compatible with the above results!')

   The result of above code has been shown in the following:
      
   .. code-block:: 
   
      Exposive mass = [30000.0545780576]
      Explosive Mass center =  [205.0062463385579] [0.0] [1.6781175585645267e-07]
      The Over Pressure Value in 500 m Over Explosive mass Center = 0.048807472058782414  Bar
      
      in casal Example 4.1, 
      d=500 m 
      M (Explosive Mass)= 30,000 
      DeltaHc=43930*1000
      And the result of over pressure is = 0.049 Bar
      That is compatible with the above results!
	
			 
.. [Ref.1] `J. Casal, Evaluation of the Effects and Consequences of Major Accidents in Industrial Plants, vol. 8. 2018.`

Code Developed by: |bsz|