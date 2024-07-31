.. _BritterMcQuaidVF:

*************************************
BritterMcQuaid Module Verification 
*************************************

This module is used  for modeling dispersion of the gas. Because of its analytical formulation and fast calculation is a proper model for using in this platform. To check its validity, the results of this model is checked by an example that is provided in Casal book. (Example 7.5)


The below codes can be downloaded from :download:`here <files/BritterMcQuaid.ipynb>` in Jupyter Notebook format. **Also, some extra calculations and some investigations on gas concentration exist in this file**. 

.. admonition:: Verification:  

   .. code-block:: python
      
	  
      opr.wipe()

      opr.Sites.Site(tag=1, Temperature=20+273, Pressure=1.013*10**5,  g=9.81,    OngroundTemprature=20, Airdensity=1.21)
      
      windobj=opr.WindData.WindRose(1)
      windobj.WindDirection=90
      windobj.WindSpeed=5.2
      
      propane=1
      opr.Substance.Material(propane,Density=553,GasDensity=1, BoilingPointGasDensity=2.32, Specific_Heat_Ratio=1.15,Molecular_Weight=44.1/1000,
                             Lower_Flammability_Limit=0.3,Upper_Flammability_Limit=0.7)
      
      OutFlowObj=opr.OutFlowModel.GasUnitHole(1, Hole_Diameter=0.02, Total_t=20, Cd=1, Gas_Constant=8.31446261815324)
      
      DispObj=opr.DispersionSpreadModels.BritterMcQuaid(1, MatTags=[1], OutFlowModelTags=[1],)
      
      
      
      UniObj=opr.PlantUnits.ONGStorage(tag=1, SiteTag=1, SubstanceTag=1, FragilityTagNumbers=[1], Horizontal_localPosition=0,
                                        Vertical_localPosition=0, Pressure=375*10**5,  Temperature=-42+273,  
                                        SubstanceVolumeRatio=1,
                                        Diameter=10, Height=10)
      
      #Do the Analysis Part Handy
      UniObj.OutFlowModelObject=OutFlowObj
      UniObj.OutFlowModelObject.UnitObject=UniObj
      UniObj.OutFlowModelObject.Calculate()
      # print(mdot[0])
      
      UniObj.DispersionSpreadModelObject=DispObj
      UniObj.DispersionSpreadModelObject.UnitObject=UniObj
      UniObj.DispersionSpreadModelObject.Calculate()
      
      #To get Concentration at a specific distance
      print('Concentration at distance 340 m is=',UniObj.DispersionSpreadModelObject.GasConcentration(340,0,0))
      print('The result is compatible with what is solved in cascal book example 7.5 for LFL=2.1%')
	  
	  #Get Distance Corresponding to a Concentration
      print('Distance Corresponding to the Concentration 0.021 is=',UniObj.DispersionSpreadModelObject.Concdist(0.021)[0])
      print('The result is compatible with what is solved in cascal book example 7.5 for LFL=2.1% that is 340 m')

   The result of above code has been shown in the following:
      
   .. code-block:: 
   
      Concentration at distance 340 m is= 0.019549915257768426
      The result is compatible with what is solved in cascal book example 7.5 for LFL=2.1%

      Distance Corresponding to the Concentration 0.021 is= 321.1696981693521
      The result is compatible with what is solved in cascal book example 7.5 for LFL=2.1% that is 340 m	  
 
	  
Verification by: |bsz|