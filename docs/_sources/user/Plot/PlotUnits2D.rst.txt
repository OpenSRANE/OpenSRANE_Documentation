.. _PlotUnitsPLT:

***************
PlotUnits2D
***************
		   
   To plot plant units hazards. 
   
   .. note::
      
	  As said frequently before, plot commands will plot what is currently exist in the memory or what is loaded into the memory.     
	   
   
   .. function:: Plot.Plotly.PlotUnits2D(PlotMode=1, OverPressureList=[], OverPressureHeight=2, OverPressurePointNumber=20, RadiationList=[], RadiationHeight=2, RadiationPointNumber=20, GasConcentrationlist=[], GasConcentrationHeght=2, ConcentrationPointNumber=10, raw=False,width=None, height=None, fontsize=18, labelfontsize=18)

   
   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
	  PlotMode, int, "Options with values equal to 1,2 or 3 to change the plot mode. For various Editors with one on these option plot will be activate!"
	  OverPressureList, list of float, list of overpressure values that user wants to be shown on plot and they will be calculated in OverPressureHeight height with OverPressurePointNumber points in boundary.
	  OverPressureHeight, float, The height that calculations be done for OverPressure. 
	  OverPressurePointNumber, int, Number or boundary points. 
	  RadiationList, list of float, list of radiation values that user wants to be shown on plot and they will be calculated in RadiationHeight height with RadiationPointNumber points in boundary.
	  RadiationHeight, float, The height that calculations be done for Radiation.
	  RadiationPointNumber, int, Number or boundary points. 
	  GasConcentrationlist, list of float, list of gas concentration values that user wants to be shown on plot and they will be calculated in GasConcentrationHeght height with ConcentrationPointNumber points in boundary.
	  GasConcentrationHeght, float, The height that calculations be done for Gas Concentration.
	  ConcentrationPointNumber, int, Number or boundary points. 
      raw, boolean, "If this option set to True, then only the plant units and defined objects without any data of happened scenario will be plotted."
	  width, int, Determines the width of plot
	  height, int, Determines the height of plot
	  fontsize, int, Determines font size of plot
	  labelfontsize, int, Determines labels font size
	  
   .. admonition:: Example:
   
      In the following results of some imaginary provided model has been shown. By clicking on the name of the legends, they will be activate
   
      **Python Code**
   
      .. code-block:: python
      
        opr.Plot.Plotly.PlotUnits2D(PlotMode=1,GasConcentrationlist=[  0.1  ], GasConcentrationHeght=1, ConcentrationPointNumber=15,OverPressureList=[3000],
                            RadiationList=[ 4000, 1600],RadiationHeight=2, RadiationPointNumber=15,)
	
      Results for first model:
	  
      .. raw:: html
          :file: figures/PlotUnits2D.html	

      | 
	  
      Results for second model: (**Zoom and click on legends to make them active and watch more details**)
	  
      .. raw:: html
          :file: figures/PlotUnits2D2.html		
		
		
Code Developed by: |bsz|