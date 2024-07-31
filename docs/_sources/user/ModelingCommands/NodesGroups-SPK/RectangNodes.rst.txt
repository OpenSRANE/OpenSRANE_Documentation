.. _RecNodes:

RectangNodes Command
*********************

.. function:: NodesGroups.RectangNodes(tag, xRefPoint, yRefPoint, xDim, yDim, xMesh, yMesh, PointsHeight, Intensity, pressure_probit_tag=None, radiation_probit_tag=None, Toxic_probit_tag=None, Type='Social')
   
   This command create nodes with a rectangle layout.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
      tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  xRefPoint, float, The rectangle bottom left x coordinate.
	  yRefPoint, float, The rectangle bottom left y coordinate.
	  xDim, float, Length of rectangle horizontal dimension.
	  yDim, float, Length of rectangle vertical dimension.
	  xMesh, int, Number of meshes along rectangle horizontal dimension.
	  yMesh, int, Number of meshes along rectangle vertical dimension.
	  PointsHeight, float, The height value that will be consider for all created nodes.
	  Intensity, float, An intensity value that will be consider for all created nodes.
	  pressure_probit_tag, int, The defined probit tag for vulnerability under overpressure loads.
	  radiation_probit_tag, int, The defined probit tag for vulnerability under thermal loads.
	  Toxic_probit_tag, int, The defined probit tag for vulnerability under toxic concentration.
	  Type, str, A string that specify the type of node.

   .. admonition:: Example:
   
      The following demonstrates the use of the Earthquake command.
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
		#Define Vulnerable object
        obj=opr.NodesGroups.RectangNodes(3,10,20,50,100,10,20,1,10)
		
		#Get created nodes Data to print
        x=obj.xGlobalList
        y=obj.yGlobalList
        
        print('List of nodes x values=',x)
        print('List of nodes y values=',y)

      Vulnerable object created in this :ref:`page (First Example) <IndividualRiskPLT>` is a sample for this command.

Code Developed by: |bsz|