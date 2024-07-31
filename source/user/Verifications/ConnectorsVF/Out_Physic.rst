.. _OutPhysicVF:

*************************************
Out_Physic Module Verification 
*************************************

The main response of the connectors is to make decisions for the following consequences according defined probability distribution. So, what should be verified for them is the accuracy of making decisions or selecting the following consequences according defined probability distribution. 

By the following code this accuracy has been checked. The below codes can be downloaded from :download:`here <files/out-physic.ipynb>` in Jupyter Notebook format.

.. admonition:: Verification:  

   .. code-block:: python
      
      #Verify Out_Physic Distribution
      opr.wipe()
      
      #Define Physical Effect models
      opr.PhysicalEffect.fire_point_source(tag=1, minf=0.055, k=1.5)
      opr.PhysicalEffect.fire_point_source(tag=2, minf=0.06, k=1.3)
      opr.PhysicalEffect.SAFE(3)
      opr.PhysicalEffect.VCE_TNT(4)
      
      #Define a DS_LOC 
      DSLOCOBJ=opr.Connectors.Out_Physic(tag=1,OutFlowTag=1,MaterialsTagList=[1],PhysicalEffectTagList=[1,4,3],PhysProbabilityList=[6,3,1])
      
      Generated=[]
      for i in range(100):
          N=1000
          rslt=dict()
          rslt={i:0 for i in DSLOCOBJ.PhysicalEffectTagList}
          for i in range(N):
              obj=DSLOCOBJ.Give1PhysicalEffectModel()
              rslt[obj.tag]=rslt[obj.tag]+1
      
          for i,j in rslt.items():
              rslt[i]=j/N
          
          Generated.append(rslt)
      
      plt.figure()
      
      plt.plot([0.6 for i in Generated], color='green',linestyle='dashed')
      plt.plot([0.3 for i in Generated], color='green',linestyle='dashed')
      plt.plot([0.1 for i in Generated], color='green',linestyle='dashed')
      
      plt.plot([i[1] for i in Generated], label='Reults for PhysicalEffect 1 with Probability 0.6')
      plt.plot([i[4] for i in Generated], label='Reults for PhysicalEffect 4 with Probability 0.3')
      plt.plot([i[3] for i in Generated], label='Reults for PhysicalEffect 3 with Probability 0.1')
      
      plt.title('Resutls of 1000 sampling in 100 repeating test')
      plt.xlabel('Test Number')
      plt.ylabel('Frequency of Occurance')
      plt.ylim(0,0.8)
      plt.legend(loc=2,fontsize = 9);

   The result of above code has been shown on the following image:

   .. _OUTPHYSICVFFig:

   .. figure:: figures/Out-Physic.png 
   	 :align: center
   	 :figclass: align-center
      
   	 Results of Out-Physic Connector Sampling
	 
Verification by: |bsz|