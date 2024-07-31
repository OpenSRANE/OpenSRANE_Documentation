.. _WindRose:

WindRose Command
****************

.. function:: WindData.WindRose(Tag, WindDayClassList=None, WindNightClassList=None, AlphaCOEFlist=None, DayWindSpeedList=None, DayWindFreqMatrix=None, NightWindSpeedList=None, NightWindFreqMatrix=None)
   
   This module contains several inputs that can directly be inserted among object definition that is tough and is not suggested.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  WindDayClassList, list of str, Specifies list of the wind classes corresponding to each wind speed range in windSpeedList in day.
	  WindNightClassList, list of str, Specifies list of the wind classes corresponding to each wind speed range in windSpeedList in night.
	  AlphaCOEFlist, list of float, Specifies list of the wind height alpha coefficient corresponding to each wind speed range in windSpeedList.
	  DayWindSpeedList, list of float, List of wind speed corresponding to each direction for day.
	  DayWindFreqMatrix, nested lists of float, A list of wind speed probabilities that for each direction divided to the probabilities of corresponding wind speed range defined in wind list for day.
	  NightWindSpeedList, list of float, List of wind speed corresponding to each direction for night.
	  NightWindFreqMatrix, nested lists of float, A list of wind speed probabilities that for each direction divided to the probabilities of corresponding wind speed range defined in wind list for night.
	  

   .. note::
   
      Attention that the lists in WindFreqMatrix considered for each direction and the first list is for north direction and consider as zero degree. 

   .. admonition:: Example:
   
      As said, defining all above parameters while defining the wind rose object is tough and author suggests that define step by step as shown in the following. The below values are according to the example of chapter 7 of Casal book [Ref.1]_ :
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        #Define Wind Rose with Tag=1 and store the wind rose object in a variable (windobj)
        windobj=opr.WindData.WindRose(1)
        
        #define wind classes
        windobj.WindDayClassList=['F','D','B','E','D','D']  
        windobj.WindNightClassList=['F','D','B','E','D','D']
        
        #define AlphaCOEFlist
        windobj.AlphaCOEFlist=[0.6,0.25,0.15,0.4,0.25,0.25]
        
        #define Wind speeds list
        windobj.DayWindSpeedList=[
        [1,2],[2,3],[3,5],[5,7],[7,9],[9]]
        
        windobj.NightWindSpeedList=[
        [1,2],[2,3],[3,5],[5,7],[7,9],[9]]
        
        #Define wind probabilities for Day and night for each direction and corresponding to the wind speeds
        
        windobj.DayWindFreqMatrix=[
        [0.446,0.372,0.355,0.109,0.017,0],
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
        [0.698,0.469,0.383,0.154,0.011,0],]
                                              
        windobj.NightWindFreqMatrix=windobj.DayWindFreqMatrix

      The results are shown in the following figure:
      
      .. raw:: html
         :file: figures/WindDay.html
   


.. [Ref.1] `J. Casal, Evaluation of the Effects and Consequences of Major Accidents in Industrial Plants, vol. 8. 2018.`

Code Developed by: |bsz|