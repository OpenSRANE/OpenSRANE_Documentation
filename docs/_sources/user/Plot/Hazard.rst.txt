.. _HazardPLT:

***************
PlotHazard
***************
		   
   To plot defined hazards. 
   
   .. function:: Plot.Plotly.PlotHazard(PlotMode=1, width=None, height=None)
   
   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
	  PlotMode, int, "Options with values equal to 1,2 or 3 to change the plot mode. For various Editors with one on these option plot will be activate!"
	  width, int, Determines the width of plot
	  height, int, Determines the height of plot
	  
   .. admonition:: Example:
   
      In the following A hazard has defined and then it has been plotted.
   
      **Python Code**
   
      .. code-block:: python
      
        opr.wipe()

        #define Hazard Curve
        PGA=[i*5/1000 for i in range(1,610)]
        
        Prob=[0.0004*i**(-1.82) for i in PGA]
        Prob[-1]=0
        
        opr.Hazard.Earthquake(1,'PGA',PGA,Prob) #Create Hazard Object with tag=1 that is 0th Object
        
        opr.Plot.Plotly.PlotHazard(PlotMode=1)
	
      The above command causes to plot hazard curve as shown in the following.
	  
      .. raw:: html
          :file: figures/PlotHazard.html	
		
		
		
Code Developed by: |bsz|