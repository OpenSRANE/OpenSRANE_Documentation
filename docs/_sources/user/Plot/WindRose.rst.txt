.. _WindRosePLT:

***************
PlotWindRose
***************
		   
   To plot defined windrose. 
   
   .. function:: Plot.Plotly.PlotWindRose(WindRoseTag, Draw_For_Day=True,PlotMode=1, width=None, height=None)
   
   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
	  PlotMode, int, "Options with values equal to 1,2 or 3 to change the plot mode. For various Editors with one on these option plot will be activate!"
	  WindRoseTag, int, Tag of defined windrose.
	  Draw_For_Day, boolean, Determines to plot Data defined for day or night.
	  width, int, Determines the width of plot
	  height, int, Determines the height of plot
	  
   .. admonition:: Example:
   
      In the following A windrose has defined and then it has been plotted.
   
      **Python Code**
   
      .. code-block:: python
	  
        import opensrane as opr
		
        opr.wipe()
		
        DTobj=opr.DateAndTime.DateTime(1)
        
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
        
        opr.Plot.Plotly.PlotWindRose(WindRoseTag=1, Draw_For_Day=True, PlotMode=1)
	
      The above command causes to plot wind rose as shown in the following.
	  
      .. raw:: html
          :file: figures/WindDay.html	
		
		
		
Code Developed by: |bsz|