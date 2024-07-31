.. _LiquidSpreadVF:

*************************************
LiquidSpread Module Verification 
*************************************

In this module the outflow mass will be dispersed in a circular shape with the center equal to the unit or equipment and radius equal to dike area if defined or radius equal to volume of the outflow mass with defined thickness. 
This module is responsible for check the availability of dike and limiting the spread of liquid to the dike area and if there is no dike, determine the minimum thickness of the liquid depend on the defined surface toughness and return the area (radius) of the spread liquid.
To check the functionality of this module to handle the above responsibilities, using the following examples, results has been checked and compared with handy calculations.


The below codes can be downloaded from :download:`here <files/LiquidSpread.ipynb>` in Jupyter Notebook format.

.. admonition:: Verification:  

   .. code-block:: python
      
	  
      #Verification for Pool Liquid Spread
      import opensrane as opr
      opr.wipe()
      
      SiteTAg=1
      opr.Sites.Site(SiteTAg, Temperature=40,Pressure=1*10197.16)
      
      #Define Material
      Subsobj=opr.Substance.DataBank.CasCalEx2_1(tag=1)
      
      #Define Outflow Models
      OutFlowObj=opr.OutFlowModel.TankHole(tag=1, Hole_Diameter=0.1, Hole_Height_FromBot=0, delta_t=100, Cd=1)
      
      #Define Dispesion Spread Models and their connections to the materials and outflows
      DispObject=opr.DispersionSpreadModels.LiquidSpread(tag=1, MatTags=[1], OutFlowModelTags=[1],
                                                         MinDisThickness=0.005,Surface_Roughnesslist=[0.1,0.2,0.3],
                                                         Surface_RoughnessThickness=[0.01,0.015,0.02])
      
      #Define Plant Unit
      UnitObj=opr.PlantUnits.ONGStorage(1,SiteTag=SiteTAg,
                                          Horizontal_localPosition=10,Vertical_localPosition=15,
                                          Diameter=5,Height=10,
                                          SubstanceTag=1,SubstanceVolumeRatio=0.85,Surface_Roughness=0.2)
      
      #Handy Calculations
      VSubs=3.1415*5**2/4*10*0.85
      MassSub=Subsobj.Density*VSubs
      PoolArea=VSubs/0.015
      PoolRadius=(PoolArea*4/3.1415)**0.5/2
      
      #These steps will be done Automatically By the Program inside the Analysis Part
      UnitObj.OutFlowModelObject=deepcopy(OutFlowObj)  #Assign OutFlow Model to Unit Object
      UnitObj.OutFlowModelObject.UnitObject=UnitObj
      UnitObj.OutFlowModelObject.Calculate();          #Calculate OutFlow Calculations to get 
      
      
      UnitObj.DispersionModelObject=DispObject           #Assign Dispersion Object to the Unit Object
      UnitObj.DispersionModelObject.UnitObject=UnitObj   #Assign the UnitObject to the Dispersion Model
      UnitObj.DispersionModelObject.Calculate()      #Do Calculations
      
      print('\n Dispersion Time=',UnitObj.DispersionModelObject.t_disp)
      print('\n Liquid Dispersion Center at each Time=',UnitObj.DispersionModelObject.LiquidCenter)
      print('\n Liquid Dispersion Radious =',max(UnitObj.DispersionModelObject.LiquidRadious), 'And handy Calculated Radius is=',PoolRadius)
      print('\n Liquid Dispersion Thickness =',min(UnitObj.DispersionModelObject.LiquidThickness))

   The result of above code has been shown in the following:
      
   .. code-block:: 
   
      Dispersion Time= [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200.5558851357086]
   
      Liquid Dispersion Center at each Time= [(10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15)]
   
      Liquid Dispersion Radious = 59.51278116960603 And handy Calculated Radius is= 59.511903571190416
   
      Liquid Dispersion Thickness = 0.015  

To check the effect of the dike, above example has been repeated in the following by considering a dike with area and radius less than above calculated area.

.. admonition:: Second Verification:  

   .. code-block:: python
   
      #Verification for Pool Liquid Spread With considering a dike
      opr.wipe()
      
      SiteTAg=1
      opr.Sites.Site(SiteTAg, Temperature=40,Pressure=1*10197.16)
      
      #Define Material
      Subsobj=opr.Substance.DataBank.CasCalEx2_1(tag=1)
      
      #Define Outflow Models
      OutFlowObj=opr.OutFlowModel.TankHole(tag=1, Hole_Diameter=0.1, Hole_Height_FromBot=0, delta_t=100, Cd=1)
      
      #Define Dispesion Spread Models and their connections to the materials and outflows
      DispObject=opr.DispersionSpreadModels.LiquidSpread(tag=1, MatTags=[1], OutFlowModelTags=[1],
                                                         MinDisThickness=0.005,Surface_Roughnesslist=[0.1,0.2,0.3],
                                                         Surface_RoughnessThickness=[0.01,0.015,0.02])
      #Define Dike Object
      Adike=5000
      opr.Safety.Dike(tag=1,Height=2, Area=Adike)
      
      #Define Plant Unit
      UnitObj=opr.PlantUnits.ONGStorage(1,SiteTag=SiteTAg,DikeTag=1,
                                          Horizontal_localPosition=10,Vertical_localPosition=15,
                                          Diameter=5,Height=10,
                                          SubstanceTag=1,SubstanceVolumeRatio=0.85,Surface_Roughness=0.2)
      
      #Handy Calculations
      VSubs=3.1415*5**2/4*10*0.85
      MassSub=Subsobj.Density*VSubs
      PoolRadius=(Adike*4/3.1415)**0.5/2
      
      #These steps will be done Automatically By the Program inside the Analysis Part
      UnitObj.OutFlowModelObject=deepcopy(OutFlowObj)  #Assign OutFlow Model to Unit Object
      UnitObj.OutFlowModelObject.UnitObject=UnitObj
      UnitObj.OutFlowModelObject.Calculate();          #Calculate OutFlow Calculations to get 
      
      
      UnitObj.DispersionModelObject=DispObject           #Assign Dispersion Object to the Unit Object
      UnitObj.DispersionModelObject.UnitObject=UnitObj   #Assign the UnitObject to the Dispersion Model
      UnitObj.DispersionModelObject.Calculate()      #Do Calculations
      
      print('\n Dispersion Time=',UnitObj.DispersionModelObject.t_disp)
      print('\n Liquid Dispersion Center at each Time=',UnitObj.DispersionModelObject.LiquidCenter)
      print('\n Liquid Dispersion Radious =',max(UnitObj.DispersionModelObject.LiquidRadious), 'And handy Calculated Radius is=',PoolRadius)
         
   The result of above code has been shown in the following:
      
   .. code-block:: 
   
      Dispersion Time= [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200.5558851357086]

      Liquid Dispersion Center at each Time= [(10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15), (10, 15)]

      Liquid Dispersion Radious = 39.89481634448608 And handy Calculated Radius is= 39.89481634448608  
	  
Verification by: |bsz|