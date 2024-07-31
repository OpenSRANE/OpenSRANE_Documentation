.. _FragilitiesPLT:

***************
PlotFragilities
***************

   To plot defined fragilities. 
   
   .. function:: Plot.Plotly.PlotFragilities(StdNumber=3, NPoints=100, FragilityTagList=[],PlotMode=1, width=None, height=None, fontsize=18, labelfontsize=18, XTitle='Random Variable')

   
   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      StdNumber, int, The number of the standard deviation that will be consider for each fragility to plot in this range
	  NPoints, int, The number of the points that will be consider for each fragility 
	  FragilityTagList, list of int, the list of fragility tags and those that mentioned in this list will be plotted and if nothing entered all fragilities will be plot.
	  PlotMode, int, "Options with values equal to 1,2 or 3 to change the plot mode. For various Editors with one on these option plot will be activate!"
	  width, int, Determines the width of plot
	  height, int, Determines the height of plot
	  fontsize, int, Determines font size of plot
	  labelfontsize, int, Determines labels font size
	  XTitle, int, Determines title of plot
	  
	  
   .. admonition:: Example:
   
      In the following example three Fragilities are defined and also plotted with various NPoints and StdNumber.
   
      **Python Code**
   
      .. code-block:: python
      
        opr.wipe()
        
        #Define the Fragilities
        opr.Fragilities.Fragility(1,'EFB','normal',5,1)
        opr.Fragilities.Fragility(2,'Gear Damage','normal',6,1.2)
        opr.Fragilities.Fragility(3,'Body Buckling','normal',7,1.4)
		
        #Plot command
        opr.Plot.Plotly.PlotFragilities(StdNumber=3, NPoints=100, FragilityTagList=[], PlotMode=1)
	
      The above command causes to plot Fragilities all together as shown in the following.
	  
      .. raw:: html
          :file: figures/FragAll.html
	  
      But the following command will cause to plot only fragilities with tags 1 and 2 and only with 10 numbers along their curves.
	  
      **Python Code**
   
      .. code-block:: python
		
        #Plot command
        opr.Plot.Plotly.PlotFragilities(StdNumber=3, NPoints=10, FragilityTagList=[1,2], PlotMode=1)

      .. raw:: html
          :file: figures/Frag12.html			
		
		
		
Code Developed by: |bsz|