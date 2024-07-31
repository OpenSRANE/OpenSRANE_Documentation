.. _TankHoleVF:

*************************************
TankHole Family Modules Verification 
*************************************

To verify this module, Casal Example [Ref.1]_ has been chosen 2.1. A model has been created according to Casal mentioned example and the results are checked with. There are also many other cases that completely are similar to TankHole model and have a small difference in their hypothesis. These model's results are checked with mentioned example.

The below codes can be downloaded from :download:`here <files/OutFlowTankHole.ipynb>` in Jupyter Notebook format.

.. admonition:: Verification:  

   .. code-block:: python
      
      #Import the software
      import opensrane as opr
	  
      #Import Matplotlib for plotting purposes
      import matplotlib.pyplot as plt
      
      #Clear Memory from probable created objects
      opr.wipe()
      
      SiteTAg=1
      opr.Sites.Site(SiteTAg, Temperature=20+273,Pressure=1*10197.16 ,XSiteBoundary=[0,100,100,0], YSiteBoundary=[0,0,100,100], g=9.81)
      
      
      #Define Material
      opr.Substance.DataBank.CasCalEx2_1(1)
      
      #Define Plant Unit
      Uni=opr.PlantUnits.ONGStorage(1,Pressure=1*10197.16 ,Temperature=2,Diameter=5,Height=10,
                                    SubstanceTag=1,SubstanceVolumeRatio=0.85) #Define a StorageTank
      
      # define outflow model object
      OutFlowObj=opr.OutFlowModel.TankHole(1,Hole_Diameter=0.05, Hole_Height_FromBot=1, delta_t=180, Cd=0.62,);
      
      OutFlowObj.UnitObject=Uni
      OutFlowObj.Calculate()
      
      MassRateG=OutFlowObj.MassLiquidReleaseRate
      MassTotal=OutFlowObj.TotalMassLiquid_Release
      t=OutFlowObj.t_release
      # print(t,MassTotal)
      
      #Casal Example 2.1 Results
      TotalMass=[0,2304,4586,6850,9092,11313,13514,15694,17853,19991,22107]
      MassRate=[0,12.8,12.68,12.57,12.45,12.34,12.23,12.11,11.99,11.88,11.76]
      Casalt=[i*180 for i in range(len(TotalMass))]
      
      plt.figure()
      plt.plot(Casalt,TotalMass, label='Casal Results')
      plt.plot(t[0:len(TotalMass)],MassTotal[0:len(TotalMass)],label='Generated')
      plt.title('Total mass release')
      plt.xlabel('time (s)')
      plt.ylabel('Total mass released (kg)')
      plt.legend()
      
      plt.figure()
      plt.plot(Casalt,MassRate, label='Casal Results')
      plt.plot(t[0:len(MassRate)],MassRateG[0:len(MassRate)],label='Generated')
      plt.legend()
      plt.title('Release Mass Rate ')
      plt.xlabel('time (s)')
      plt.ylabel('Mass Release rate (kg/2)')

   The result of above code has been shown in the following:
   
   .. _OutFlow1VF:

   .. figure:: figures/TankHole1.png
   	 :align: center
   	 :figclass: align-center
      
   	 Comparision of Total mass release between code and [Ref.1]_ Example
   
   .. _OutFlow2VF:

   .. figure:: figures/TankHole2.png
   	 :align: center
   	 :figclass: align-center
      
   	 Comparision of release mass rate between code and [Ref.1]_ Example

.. [Ref.1] `J. Casal, Evaluation of the Effects and Consequences of Major Accidents in Industrial Plants, 2018.`
      	  
Verification by: |bsz|