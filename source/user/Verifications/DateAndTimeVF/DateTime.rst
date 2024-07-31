.. _DateTimeVF:

*************************************
DateTime Module Verification 
*************************************

The question is that **Does the SampleisDay method of DateTime object correctly samples the defined ratio for it?**. To find the answer of this question, first a DateTime object will be created. Then numerous samples will be created and record. Finally the distribution of recorded samples will be check by defined DateTime object (Ratio of day to night). 10000 samples considered for checking results and 100 times this check repeated.

The below codes can be downloaded from :download:`here <files/DateTime.ipynb>` in Jupyter Notebook format.

.. admonition:: Verification1:  

   .. code-block:: python
      
      #Import the software
      import opensrane as opr
      
      #Import Matplotlib package for plot purposes
      import matplotlib.pyplot as plt 
      
      #Clear Memory from probable created objects
      opr.wipe()
      
      #Generate an DateTime Obj with day to night ratio equal to 2
      obj=opr.DateAndTime.DateTime(1,Day_Night_Ratio=2)

      Results=[]
      for i in range(100):
          N=10000
          
          Samples=[obj.SampleisDay() for i in range(N)]
      
          Results.append(Samples.count(True)/Samples.count(False))
          
      plt.plot(Results)
      plt.ylim(0,4)
      plt.xlabel('Times of sulation repeated')
      plt.ylabel('Day to Night Ratio')
      
	  
   The result of above code has been shown on the following image:

   .. _DateTimeVFResFig:

   .. figure:: figures/DateTimeRatioVF.png 
   	 :align: center
   	 :figclass: align-center
      
   	 Results of 100 times checking simulated day to night ratio (2) 	  
	 
	  
Verification by: |bsz|