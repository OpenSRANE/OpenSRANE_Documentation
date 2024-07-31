.. _Nodes:

Nodes Command
******************

.. function:: NodesGroups.Nodes(tag, xGlobalList, yGlobalList, zGlobalList, AreaList, IntensityList, pressure_probit_tag=None, radiation_probit_tag=None, Toxic_probit_tag=None, Type='Social')
   
   This command is for defining arbitrary nodes.  

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
      tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  xGlobalList, list of float, list of x coordinate of nodes.
	  yGlobalList, list of float, list of y coordinate of nodes.
	  zGlobalList, list of float, list of z coordinate of nodes.
	  AreaList, list of float, list of each node area.
	  IntensityList, list of float, "list of each node intensity. For example if a value equal to 10 enter as intensity for a node that present population, it means that in each unit area of this node 10 person exist. If node is Social, then it shows the crowd per area, if environmental then it shows the plants per area and ..."
	  pressure_probit_tag, int, The defined probit tag for vulnerability under overpressure loads.
	  radiation_probit_tag, int, The defined probit tag for vulnerability under thermal loads.
	  Toxic_probit_tag, int, The defined probit tag for vulnerability under toxic concentration.
	  Type, str, A string that specify the type of node.


   .. admonition:: Example:
   
      The following demonstrates the use of the Earthquake command.
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        #Define Vulnerable Area
        opr.wipe()

        obj=opr.NodesGroups.Nodes(1,[4,5,6],[4,5,6],[1,1,1],[2,2,2],[2,3,4])
        obj1=opr.NodesGroups.Nodes(2,[4,8,5,6],[4,5,6,7], [1,1,1,1],[2,4,2,2],[2,2,3,4],Type='Environment')
        
        print("tag 1 intensity list=",obj.IntensityList)
        print("tag 2 intensity list=",obj1.IntensityList)
        
        print('tag 2 type:',obj1.Type)
        
        opr.NodesGroups.ObjManager[1].name
		
      Another example:
	  
	  **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
        import random as rnd

        opr.wipe()

        xGlobalList=[rnd.uniform(-50,50) for i in range(20)]
        yGlobalList=[rnd.uniform(-50,50) for i in range(20)]
        zGlobalList=[2 for i in range(20)]
        AreaList=[2 for i in range(20)]
        IntensityList=[rnd.uniform(0,5) for i in range(20)]
        pressure_probit_tag=1
        radiation_probit_tag=1
        opr.NodesGroups.Nodes(1, xGlobalList, yGlobalList, zGlobalList, AreaList, IntensityList,
                              pressure_probit_tag, radiation_probit_tag, Type='Social')


Code Developed by: |bsz|