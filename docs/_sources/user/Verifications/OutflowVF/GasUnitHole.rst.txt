.. _GasUnitHoleVF:

*************************************
GasUnitHole Module Verification 
*************************************

To verify this module, Casal Example has been chosen 2.3.1. A model has been created according to Casal mentioned example and the results are checked with.

The below codes can be downloaded from :download:`here <files/OutFlowGasUnitHole.ipynb>` in Jupyter Notebook format.

.. admonition:: Verification:  

   .. code-block:: python
      
      #Import the software
      import opensrane as opr
      
      #Clear Memory from probable created objects
      opr.wipe()

      #Define Site properties
      opr.Sites.Site(tag=1, Temperature=20+273, Pressure=1.013*10**5, g=9.81, OngroundTemprature=20, Airdensity=1.21)
      
      #define substance 
      propane=1
      opr.Substance.Material(propane,Specific_Heat_Ratio=1.15,Molecular_Weight=44.1/1000,GasDensity=1.808)
      
      #define outflow model
      OutFlowObj1=opr.OutFlowModel.GasUnitHole(1, Hole_Diameter=0.02, Total_t=20, Cd=0.62, Gas_Constant=8.31446261815324,)
      OutFlowObj2=opr.OutFlowModel.GasUnitHole(2, Hole_Diameter=0.02, Total_t=40, Cd=1, Gas_Constant=8.31446261815324,)
      
      #define plant unit object
      UniObj=opr.PlantUnits.ONGStorage(tag=1, SiteTag=1, SubstanceTag=1, Pressure=10*10**5,  Temperature=25+273, SubstanceVolumeRatio=1, Diameter=10, Height=10)
      
      #Assign outflow object to the plant unit handy and call the calculation method
      UniObj.OutFlowModelObject=OutFlowObj1
      UniObj.OutFlowModelObject.UnitObject=UniObj
      UniObj.OutFlowModelObject.Calculate()
      
      #get some of the calculation results
      mdot=UniObj.OutFlowModelObject.MassGasReleaseRate
      mTotal=UniObj.OutFlowModelObject.TotalMassGas_Release
      print('For Cd=0.62 the mass outflow rate = ', mdot[1],' and the total released mass =',mTotal[-1])
      
      #Check for second case
      UniObj.OutFlowModelObject=OutFlowObj2
      UniObj.OutFlowModelObject.UnitObject=UniObj
      UniObj.OutFlowModelObject.Calculate()
      mdot=UniObj.OutFlowModelObject.MassGasReleaseRate
      mTotal=UniObj.OutFlowModelObject.TotalMassGas_Release
      print('For Cd=1 the mass outflow rate = ', mdot[1],' and the total released mass =',mTotal[-1])
      
      print('Results are compatible with casal outflow rate results on example 2.3 that for cd=0.62 md=0.525 and for cd=1 md=0.847')

The result of above code has been shown in the following:
   
.. code-block:: 

   *** Check Warning File ***
   For Cd=0.62 the mass outflow rate =  0.524780573836817  and the total released mass = 10.49561147673634
   For Cd=1 the mass outflow rate =  0.846420280381963  and the total released mass = 33.85681121527852
   Results are compatible with casal outflow rate results on example 2.3 that for cd=0.62 md=0.525 and for cd=1 md=0.847   
      	  
Verification by: |bsz|