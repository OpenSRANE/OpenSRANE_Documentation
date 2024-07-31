.. _WindRoseVF:

*************************************
WindRose Module Verification 
*************************************

The question is that **Does the GetRandomWindِSample method of WindRose object correctly samples the Defined wind Data?**. To find the answer of this question, first a WindRose object will be created. Then numerous samples will be created and record. Finally the distribution of recorded samples will be check by defined WindRose data.

The below codes can be downloaded from :download:`here <files/WindRose.ipynb>` in Jupyter Notebook format.

.. admonition:: Verification:  

   .. code-block:: python
      
      #Import the software
      import opensrane as opr
      
      
      #Clear Memory from probable created objects
      opr.wipe()
      
      #Define Date time object
      DTobj=opr.DateAndTime.DateTime(1)
   
      #Defind WindRose Object
      windobj=opr.WindData.WindRose(1)
      
      windobj.WindDayClassList=['F','D','B','E','D','D']  
      windobj.WindNightClassList=['F','D','B','E','D','D']  
      
      windobj.AlphaCOEFlist=[0.6,0.25,0.15,0.4,0.25,0.25]
      
      windobj.DayWindSpeedList=[[1,2],[2,3],[3,5],[5,7],[7,9],[9,9]]
      windobj.NightWindSpeedList=[[1,2],[2,3],[3,5],[5,7],[7,9],[9,9]]
      
      #You don't need to define calmn Condition and program will understand it automatically
      windobj.DayWindFreqMatrix=[ [0.446,0.372,0.355,0.109,0.017,0],
                                  [0.44,0.938,1.55,0.755,0.097,0.029],
                                  [0.898,1.321,3.06,1.402,0.767,0.892],
                                  [0.875,1.241,2.626,1.51,0.892,0.646],
                                  [0.801,0.927,1.63,0.658,0.355,0.097],
                                  [0.87,1.121,0.984,0.309,0.023,0.029],
                                  [0.778,0.801,0.91,0.315,0.029,0],
                                  [0.652,0.875,1.35,0.498,0.086,0.023],
                                  [0.566,0.887,1.659,0.709,0.149,0],
                                  [0.583,0.807,2.128,2.998,1.041,0.137],
                                  [0.898,1.093,2.408,2.059,1.327,0.154],
                                  [1.985,2.088,2.488,1.098,0.332,0.069],
                                  [4.067,3.123,1.442,0.292,0.063,0.011],
                                  [3.93,5.372,3.85,1.201,0.349,0.057],
                                  [1.71,1.619,2.38,0.767,0.109,0.006],
                                  [0.698,0.469,0.383,0.154,0.011,0],
                              ]   
      
      
      windobj.NightWindFreqMatrix=windobj.DayWindFreqMatrix


      #---------------- Verification For Day---------------------------------
	  N=100000 #Number of Sampling
	  
	  #Define Variables to store data
      windDir=set()
      WindDirData=dict()
      WindSpeedFreq=[[0.0,0.0,0.0,0.0,0.0,0] for i in range(16)]
      
      #Sampling DayTime
      DTobj.SampleisDay()
      WindDirData['isCalmn']=0
	  
      for i in range(N):
          
          rslt=windobj.GetRandomWindِSample(); #Create a sample
          
          #Get wind Direction
          if rslt['isCalmn']==False: windDir.add(rslt['WindDirection'])
          if len(windDir)!=len(WindDirData)-1 and rslt['isCalmn']==False:
              wdir=list(windDir)
              add=[i for i in wdir if i not in WindDirData.keys()][0]
              WindDirData[add]=0
              
          if rslt['isCalmn']== True:
              WindDirData['isCalmn'] =WindDirData['isCalmn']+1
          else:
              WindDirData[rslt['WindDirection']] =WindDirData[rslt['WindDirection']]+1
          
              
          #Calculating Wind Speed Frequency
          if rslt['isCalmn']==False:
              
              WindRow=[i for i in range(len(windobj.DayTheta)) if windobj.DayTheta[i]==rslt['WindDirection']][0]
              WindCol=[i for i in range(len(windobj.DayWindSpeedList)) if (windobj.DayWindSpeedList[i][0]<=rslt['WindSpeed']<=windobj.DayWindSpeedList[i][1])][0]
              WindSpeedFreq[WindRow][WindCol]=WindSpeedFreq[WindRow][WindCol]+1
              
      #Normalize Wind Matrix
      for i in range(len(WindSpeedFreq)):
          for j in range(len(WindSpeedFreq[0])):
              WindSpeedFreq[i][j]=WindSpeedFreq[i][j]/N*100
              
      #print('Monte Carlo Sampling Results: \n',  WindSpeedFreq)
      #print('\n Defined Values: \n',windobj.DayWindFreqMatrix)
      #print()
      
      #Normalizing Wind Direction Data        
      for key in WindDirData.keys():
          WindDirData[key]=WindDirData[key]/N*100
          
      print('\nComparision of Direction Sampling Ratio and User Defined Values:\n')
      userdata=dict(zip(windobj.DayTheta,windobj.DayDirectProbability));
      for keys in userdata.keys():
          print(f'for direction {keys} average of \t sampled values: {round(WindDirData[keys],3)} \t and UserDefined value: {round(userdata[keys],3)}')
      print(f"and Calm condition is= {WindDirData['isCalmn']}")


   The result of above code has been printed in the following:

   .. code-block::
      
      Comparision of Direction Sampling Ratio and User Defined Values:
      
      for direction 0.0 average of 	 sampled values: 1.289 	 and UserDefined value: 1.299
      for direction 22.5 average of 	 sampled values: 3.855 	 and UserDefined value: 3.809
      for direction 45.0 average of 	 sampled values: 8.296 	 and UserDefined value: 8.34
      for direction 67.5 average of 	 sampled values: 7.768 	 and UserDefined value: 7.79
      for direction 90.0 average of 	 sampled values: 4.424 	 and UserDefined value: 4.468
      for direction 112.5 average of 	 sampled values: 3.293 	 and UserDefined value: 3.336
      for direction 135.0 average of 	 sampled values: 2.827 	 and UserDefined value: 2.833
      for direction 157.5 average of 	 sampled values: 3.516 	 and UserDefined value: 3.484
      for direction 180.0 average of 	 sampled values: 4.033 	 and UserDefined value: 3.97
      for direction 202.5 average of 	 sampled values: 7.831 	 and UserDefined value: 7.694
      for direction 225.0 average of 	 sampled values: 7.922 	 and UserDefined value: 7.939
      for direction 247.5 average of 	 sampled values: 7.913 	 and UserDefined value: 8.06
      for direction 270.0 average of 	 sampled values: 9.003 	 and UserDefined value: 8.998
      for direction 292.5 average of 	 sampled values: 14.692  and UserDefined value: 14.759
      for direction 315.0 average of 	 sampled values: 6.638 	 and UserDefined value: 6.591
      for direction 337.5 average of 	 sampled values: 1.749 	 and UserDefined value: 1.715
      and Calm condition is= 4.951
   
   As it can bee seen, the samples values and defined values for each direction have properly close to each other.
   
Verification by: |bsz|