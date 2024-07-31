.. _IndividualRiskPLT:

******************
PlotIndividualRisk
******************
		   
   To plot any set of values on defined nodesGroup object. If we set the individual risk values on each node of a defined nodesGroup then this command will plot the individual risk.
   
   .. function:: Plot.Plotly.PlotIndividualRisk(PlotMode=1, NodesGroupTag=1, NodesProbabilityList=[], ContorList=[], width=None, height=None, xrange=[], yrange=[], fontsize=18, labelfontsize=18)

   
   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
	  PlotMode, int, "Options with values equal to 1,2 or 3 to change the plot mode. For various Editors with one on these option plot will be activate!"
	  NodesGroupTag, int, The tag of NodesGroup that user want to be shown on plot. 
	  NodesProbabilityList, list of float, "the probability values that has been resulted from analysis and the specify the death probability of each node (Obviously its length should be equal to the number of the NodesGroupTag nodes. "
	  ContorList, list of float, "The list of the minimum and maximum contour value that we want to be plot. If user do not fill it, the code automatically consider the range according the minimum and maximum values of NodesProbabilityList."
	  width, int, Determines the width of plot
	  height, int, Determines the height of plot
	  xrange, list, A list with two values of start and end of x axis to limit plot to these values
	  yrange, list, A list with two values of start and end of y axis to limit plot to these values
	  fontsize, int, Determines font size of plot
	  labelfontsize, int, Determines labels font size
	  XTitle, int, Determines title of plot
	  
   .. admonition:: Example:
      
      Consider the following model with defined nodesGroup (Vulnerable Object). Click on Vulnerabe legend to see the defined nodesGroup with tag 1.
      
      .. raw:: html
          :file: figures/PlotUnits2DRaw.html	
	
      |	  
	  
      In the following the individual risk values at each node has stored in CalculatedValues variable for NodesGroup with tag 1. Then using following command it has been plotted.
   
      **Python Code**
   
      .. code-block:: python
      
        opr.Plot.Plotly.PlotIndividualRisk(PlotMode=1, NodesGroupTag=1, NodesProbabilityList=CalculatedValues, ContorList=[1e-8,1e-5],)
	
	  
      .. raw:: html
          :file: figures/PlotIndividualRisk.html	
	
      |
	  
      For previous model now the radiation values are calculated at each node of NodesGroup 1 and stored in the RadVals variable.  Then using following command it has been plotted as shown in the following.
	  
      **Python Code**
   
      .. code-block:: python
      
        opr.Plot.Plotly.PlotIndividualRisk(PlotMode=1, NodesGroupTag=1, NodesProbabilityList=RadVals, ContorList=[],)
	
	  
      .. raw:: html
          :file: figures/PlotNodesRadiation.html			
		
Code Developed by: |bsz|