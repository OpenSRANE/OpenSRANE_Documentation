.. _ProbitsPLT:

***************
PlotProbits
***************
		   
   To plot defined probits.
   
   .. function:: Plot.Plotly.PlotProbits(StdNumber=3, NPoints=100, ProbitTag=None, PlotMode=1, width=None, height=None)
   
   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      StdNumber, int, The number of the standard deviation that will be consider for each fragility to plot in this range
	  NPoints, int, The number of the points that will be consider for each fragility 
	  ProbitTag, int, the tag of a special defined probit to plot and in nothing enter all probits will be plotted.
	  PlotMode, int, "Options with values equal to 1,2 or 3 to change the plot mode. For various Editors with one on these option plot will be activate!"
	  width, int, Determines the width of plot
	  height, int, Determines the height of plot
	  
   .. admonition:: Example:
   
      In the following example three Fragilities are defined and also plotted with various NPoints and StdNumber.
   
      **Python Code**
   
      .. code-block:: python
      
        opr.wipe()

        opr.Fragilities.Probit(tag=1,Distribution_Type='normal',K1=5,K2=2)
        opr.Fragilities.Probit(2,'normal',3,2)
        opr.Fragilities.Probit(3,'lognormal',4,3)
		
        #Plot command
        opr.Plot.Plotly.PlotProbits(StdNumber=3, NPoints=100, ProbitTag=None, PlotMode=1)
	
      The above command causes to plot probits all together as shown in the following.
	  
      .. raw:: html
          :file: figures/ProbAll.html
	  
      But the following command will cause to plot only Probit with tags 1 and only with 10 numbers along its curves.
	  
      **Python Code**
   
      .. code-block:: python
		
        #Plot command
        opr.Plot.Plotly.PlotProbits(StdNumber=3, NPoints=10, ProbitTag=1, PlotMode=1)

      .. raw:: html
          :file: figures/Prob1.html		
		
		
		
Code Developed by: |bsz|