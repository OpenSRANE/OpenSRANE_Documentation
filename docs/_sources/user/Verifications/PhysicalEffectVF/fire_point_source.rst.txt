.. _firepointsourceVF:

******************************************
fire_point_source Module Verification 
******************************************

The fire point source model is formulated according point source model explained in Casal book [Ref.1]_. To validate the calculations of this module, example 3.4 of Casal book chose. The following code model the example condition and the final result is checked by example results.

The below codes can be downloaded from :download:`here <files/fire_point_source.ipynb>` in Jupyter Notebook format.

.. admonition:: Verification:  

   .. code-block:: python
   
      opr.wipe()

      #Define Wind Rose 
      windobj=opr.WindData.WindRose(1)
      windobj.WindSpeed=0
      windobj.WindDirection=90
      
      #Define Site Condition and Geometry
      SiteTAg=1
      obj=opr.Sites.Site(SiteTAg, Temperature=16+273, Pressure=1*10**5, XSiteBoundary
                         g=9.81,Humidity=0.79,Airdensity=0.270)
      
      #Define Substance
      subsobj=opr.Substance.DataBank.Butene(1) #Use DataBank to Load Material
      subsobj.Specific_Heat_of_Combustion=41900*1000
      
      #Define OutFlow Model
      OutflowObj=opr.OutFlowModel.TankHole(1, Hole_Diameter=0.05, Hole_Height_FromBot
      #Define Dispersion Model
      DispObj=opr.DispersionSpreadModels.LiquidSpread(tag=1, MatTags=[1], OutFlowMode
      
      #Define Dike for Tanks
      opr.Safety.Dike(1,0,3.1415*6**2/4)
      
      
      PlantObj=opr.PlantUnits.ONGStorage(1,SiteTag=1,DikeTag=1, SubstanceTag=1,    Di
                                         Horizontal_localPosition=0,    Vertical_loca
                                         Height=20,SubstanceVolumeRatio=0.9)
      
      #Manually define OutFlow Model for above Unit Object
      PlantObj.OutFlowModelObject=OutflowObj
      OutflowObj.UnitObject=PlantObj
      PlantObj.OutFlowModelObject.Calculate()
      
      
      #Manually define DispersionSpread Model for above Unit Object
      PlantObj.DispersionSpreadModelObject=DispObj
      PlantObj.DispersionSpreadModelObject.UnitObject=PlantObj
      PlantObj.DispersionSpreadModelObject.Calculate()
      
      
      obj=opr.PhysicalEffect.fire_point_source(1,minf=0.0501,k=1.5)
      obj.UnitObject=PlantObj
      [H,Hmax,D,Dprin,alpha,m]=obj._fireGeometry()
      [Lp,d,phi,xf,yf]=obj._DistanceToFireCenterGeometry(18,0,1.6)
        
      
      print('H,D,m=',round(H,2),round(D,2),round(m,2))
      print('Lp,d,phi=',round(Lp,2),round(d,2),round(phi,2))
      
      print('Thermal Radiation intensity=',obj.Thermal_Radiation_at_Point(18,0,1.6) )
	  
      print('in casal Example 3.4, \nD=6 m \nH=11.5\nPoint coordinate=[18,0,1.6] \nHeat Of Combustion=41900*10^3\nHumidity=0.79\nm=0.05')
      print()
      print('And the result Thermal Radiation intensity= 2800 W/m^2')
      print('That is compatible with the above results!')

   The result of above code has been shown in the following:
      
   .. code-block:: 
   
      H,D,m= 11.5 6.0 0.05
      Lp,d,phi= 18.47 15.39 0.23
      Thermal Radiation intensity= 2878.505632375152
      
      in casal Example 3.4, 
      D=6 m 
      H=11.5
      Point coordinate=[18,0,1.6] 
      Heat Of Combustion=41900*10^3
      Humidity=0.79
      m=0.05
      
      And the result Thermal Radiation intensity= 2800 W/m^2
      That is compatible with the above results!
	
			 
.. [Ref.1] `J. Casal, Evaluation of the Effects and Consequences of Major Accidents in Industrial Plants, vol. 8. 2018.`

Code Developed by: |bsz|