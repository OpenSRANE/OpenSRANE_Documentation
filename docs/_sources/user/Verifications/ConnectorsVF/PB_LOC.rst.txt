.. _PBLOCVF:

*************************************
PB_LOC Module Verification 
*************************************

The main response of the connectors is to make decisions for the following consequences according defined probability distribution. So, what should be verified for them is the accuracy of making decisions or selecting the following consequences according defined probability distribution. 

By the following code this accuracy has been checked. The below codes can be downloaded from :download:`here <files/Pb-Loc.ipynb>` in Jupyter Notebook format.

.. admonition:: Verification:  

   .. code-block:: python
      
      #Verify Pb-LOC Distribution
      opr.wipe()
      
      #Define Some Imaginary Outflow Models
      tag=1
      opr.OutFlowModel.TankHole(tag, Hole_Diameter=0.05, Hole_Height_FromBot=0, delta_t=100, Cd=1)
      opr.OutFlowModel.TankHole(2, Hole_Diameter=0.01, Hole_Height_FromBot=1, delta_t=150, Cd=0.62)
      opr.OutFlowModel.TankHole(3, Hole_Diameter=0.5, Hole_Height_FromBot=0.5, delta_t=100, Cd=0.62)
      opr.OutFlowModel.Liquid10min(4)
      opr.OutFlowModel.Liquid10min(5)
      
      #Define a DS_LOC 
      DSLOCOBJ=opr.Connectors.Pb_LOC(tag=1,ProbitTag=1,OutFlowModelTagList=[1,4,3],LOCProbabilityList=[6,3,1]) 
      
      Generated=[]
      for i in range(100):
          N=1000
          rslt=dict()
          rslt={i:0 for i in DSLOCOBJ.OutFlowModelTagList}
          for i in range(N):
              obj=DSLOCOBJ.Give1OutFlowModel()
              rslt[obj.tag]=rslt[obj.tag]+1
      
          for i,j in rslt.items():
              rslt[i]=j/N
          
          Generated.append(rslt)
      
      
      plt.figure()
      
      plt.plot([0.6 for i in Generated], color='green',linestyle='dashed')
      plt.plot([0.3 for i in Generated], color='green',linestyle='dashed')
      plt.plot([0.1 for i in Generated], color='green',linestyle='dashed')
      
      plt.plot([i[1] for i in Generated], label='Reults for OutFlow 1 with Probability 0.6')
      plt.plot([i[4] for i in Generated], label='Reults for OutFlow 4 with Probability 0.3')
      plt.plot([i[3] for i in Generated], label='Reults for OutFlow 3 with Probability 0.1')
      
      plt.title('Resutls of 1000 sampling in 100 repeating test')
      plt.xlabel('Test Number')
      plt.ylabel('Frequency of Occurance')
      plt.ylim(0,0.8)
      plt.legend(loc=2,fontsize = 9);

   The result of above code has been shown on the following image:

   .. _PBLOCVFFig:

   .. figure:: figures/PB-LOC.png 
   	 :align: center
   	 :figclass: align-center
      
   	 Results of PB-LOC Connector Sampling
	 
Verification by: |bsz|