.. _PostProcessSPK:

*************************
PostProcess SubPackage
*************************

Using this subpackage, user can export easily some specific data or results or plots from the recorders and user do not need to write code for post processing. Currently there are ObjsRecorder and Recorder modules for recording. In the following, some commands that has been provided are described for exporting some results from recorded data.

.. note::

   Using the results in the form of this section for post processing is not mandatory and users can use their own code on the resulted values from analysis of the software. Also, users can develope the current module for post processing or add their modules or methods to the source code for further usages. 
   
.. _First Step:

First Step: Create PostProcess Object
-------------------------------------
   
   At very fist step, user should create the object of post processing. By creating this object, its constructor load data and get the results. For :ref:`Objs_recorder <Objsrecorder>` and :ref:`Recorder <Recorder>` there are a specific command for this purpose. These commands are described in the following:
   
   * To create post process object for recorded data via :ref:`Objs_recorder <Objsrecorder>` use the following command. In this command **filename** is the name of recoded file using :ref:`Objs_recorder <Objsrecorder>` recorder. All the statistical analysis and data will be in this created object. (In the following examples the created object is named Post_Process_Object)
   
      .. code-block:: python
	     
         import opensrane as opr
  
         Post_Process_Object=opr.PostProcess.ObjsRecorderPP(ObjsRecorer_filename=filename, Number_Of_LOC_Histogram_Bins=100)
   
   * To create post process object for recorded data :ref:`Recorder <Recorder>` use the following command. When user is using :ref:`Recorder <Recorder>` to record data and results, there are one separated file for each desired result and so finally there will be more than one file for recorded results. In this command **Recorder_FilenamesList** is the list of the recoded files name using :ref:`Recorder <Recorder>` recorder. All the statistical analysis and data will be in this created object. In the following sample it is assumed that user recorded the desired results in the mentioned file names. 
   
      .. code-block:: python
	     
         import opensrane as opr
  
         Post_Process_Object=opr.PostProcess.RecorderPP(Recorder_FilenamesList=['RecorderA.OPRrec','RecorderB.OPRrec','RecorderC.OPRrec','RecorderD.OPRrec','RecorderE.OPRrec'],Number_Of_LOC_Histogram_Bins=100)

Second Step: Methods
--------------------

   By creating the post process object, various methods will be available for user that contains various results or plots that are resulted from recorded results by recorder object/s. In the following tables these methods and their its results are described.
   
* **DamagedLevelList** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      **DamagedLevelList()**, Post_Process_Object.DamagedLevelList(), "By calling this method, a list of dictionaries will be shown that each dictionary is related to a scenario and shows tag of the elements and level of damage."
	  
   Sample for resultes:
   
   .. code-block::
   
      [{1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
       {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0, 8: 1},
       {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
       {1: 0, 2: 0, 3: 3, 4: 4, 5: 1, 6: 0, 7: 1, 8: 2},…]



* **FragilityTagList** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      **FragilityTagList**, Post_Process_Object.FragilityTagList(), "This method, returns a list of dictionaries that each dictionary is related to a scenario and each key refers to a plant unit tag and the its result shows the tag of defined fragility or probit that cause damage."
	  
   Results sample:
   
   .. code-block::
   
      [{1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
       {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
       {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
       {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
       {1: 2, 2: 2, 3: 1, 4: 1, 5: 1, 6: 3, 7: 1, 8: 3}, 
       {1: None, 2: None, 3: 1, 4: None, 5: None, 6: None, 7: 1, 8: 1}, 
       {1: None, 2: 3, 3: 1, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1},…]


* **LOCList** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      **LOCList**, Post_Process_Object.LOCList(), "This method, returns a list of dictionaries that each dictionary shows the released liquid mass value (Loss Of Containment) of the plant unit in each scenario."
	  
   Results sample:
   
   .. code-block::
   
      [{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0},
       {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0},
       {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0},
       {1: 2827433.3882308137, 2: 4208351.855042743, 3: 4208351.855042743, 4: 4208351.855042743, 5: 3674532.4313447657, 6: 3674532.4313447657, 7: 3674532.4313447657, 8: 3674532.4313447657},…]
	   
	   
* **NodesGroupDamageList** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      **NodesGroupDamageList**, Post_Process_Object.NodesGroupDamageList(), "This method, return a list of dictionaries each dictionary is results of each scenario and its keys are the NodesGroups tag and its result shows the elements damage condition according defined probit functions (0 shows No damage and 1 shows damaged). It returns empty list for Not damaged case."
	  
   Results sample:
   
   .. code-block::
   
      [{1: []}, {1: []}, {1: []}, {1: []}, {1: []},
       {1:[0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,1,1,0,0,0,1,0]}, ... ]
	   

* **NodesGroupTypeDict** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      **NodesGroupTypeDict**, Post_Process_Object.NodesGroupTypeDict(), "This metthod returns a dictionary that each key refers to a NodesGroup tag and the its result is the type of the NodesGroup."
	  
   Results sample:
   
   .. code-block::
   
      [{1: []}, {1: []}, {1: []}, {1: []}, {1: []},
       {1:'Social'}, ... ]
	   

* **TotalLOCList** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      **TotalLOCList**, Post_Process_Object.TotalLOCList(), "This method returns list of total liquid mass (kg) that has released in each scenario."
	  
   Results sample:
   
   .. code-block::
   
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3674532.4313447657, 0, 0, 03674532.4313447657, 20593020.94647379, 0, 0, 0, 11557416.717732275, 5674351.416812722, 0, 0, 0, 14028296.729529412, 4208351.855042743, 0, 0, 0, 0, 0,…]
	  

* **LOC_bins_hist_probloc** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      "**LOC_bins_hist_probloc**", "[bins,hist,probloc]= Post_Process_Object.LOC_bins_hist_probloc()", "This method returns 3 lists that are histogram data of the released liquids however they can be calculated from the previous described list. The first list is the bins data that its length should be one value greater than the two other lists. The second list is histogram data that shows the frequency of the bins and the last list is the probability of each bin value."


* **Total_Number_Of_Scenarios** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      "**Total_Number_Of_Scenarios**", "Post_Process_Object.Total_Number_Of_Scenarios()", "This method simply returns total number of sampled scenarios. "
	  
   Results sample:
   
   .. code-block::
   
      1000000


* **UnitsZeroDamageProb** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
    
      **UnitsZeroDamageProb**, Post_Process_Object.UnitsZeroDamageProb(), "This method returns the damage probability of each unit in zero level as a dictionary. The keys are the units tag and their its results show the probability of damaging in the zero level."
	  
   Results sample:
   
   .. code-block::
   
      {1: 0.0018952380952380952, 2: 0.001990476190476190, 3: 0.0021714285714285715, 4: 0.0019047619047619048, 5: 0.0019904761904761905, 6: 0.0021714285714285715, 7: 0.0021523809523809525, 8: 0.001961904761904762}
	  


* **ProbOfFragilities** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      **ProbOfFragilities**, Post_Process_Object.ProbOfFragilities(), "This method returns the probability of happening of each defined fragility or probit function as a dictionary. The keys show the defined fragility or probit tag and the its results shows their governing probability among analysis. Probits that have defined for the Vulnerable areas (NodesGroup) will not consider in this part and their probability will be shown as zero (probits with tag 5 and 6)."
	  
   Results sample:
   
   .. code-block::
   
      {1: 0.003952380952380952, 2: 0.012285714285714285, 3: 0.005238095238095238, 4: 0.0009904761904761905, 5: 0.0, 6: 0.0}
	  
	  
* **Damagelevel_eLOC** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      "**Damagelevel_eLOC**", "Post_Process_Object.Damagelevel_eLOC()", "This method returns the expected released liquid (mass in kg) in each damage level as a dictionary. Each key refers to the damage level and the its result shows expected liquid released mass in that damage level."
	  
   Results sample:
   
   .. code-block::
   
      {0: 56082.8170381438, 1: 8802.563549482884, 3: 925.6543716581589, 4: 395.0027138190845, 2: 3376.962598791185, 6: 26.927937030769655, 5: 116.56262508340092}
	  

* **ScenariosAnalyzeNumbers** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      "**ScenariosAnalyzeNumbers**", "Post_Process_Object.ScenariosAnalyzeNumbers()", "This method returns scenarios name with the following format as key and list of the analyze number as its result as a dictionary."
	  
   Results sample:
   
   .. code-block::
   
      {'(0):[3]': [202, 5646, 16833, 17173, 20846, 23658, 29179, 30415, 41698, 42064, 42114], '(0):[3,5]-(1):[2]-(2):[1,6,7]': [316778], 
       '(0):[1,3,6]-(1):[4,7]': [316830], '(0):[1,3,6]-(1):[4,7]-(2):[8]': [316830], '(0):[4,5]-(1):[3]-(2):[2]-(3):[1,6]': [316858]}
	  
   
   .. note::
   
      The rule of mentioning scenarios is : (Damage level):[list of units tag that damaged in this level] for example:
         '(0):[3]' shows a scenario with damaging plant unit 3 in damage level 0
         '(0):[3,5]-(1):[2]' shows a scenario with damaged plant units with tag 3 and 5 in damage level 0 and damaged plant unit with tag 2 at damage level 1


* **ScenariosProbability** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      "**ScenariosProbability**", "Post_Process_Object.ScenariosProbability()", "This method returns scenarios name as key and the corresponding probability as value. "
	  
   Results sample:
   
   .. code-block::
   
      {'(0):[3]': [202, 5646, 16833, 17173, 20846, 23658, 29179, 30415, 41698, 42064, 42114], '(0):[3,5]-(1):[2]-(2):[1,6,7]': [316778], 
       '(0):[1,3,6]-(1):[4,7]': [316830], '(0):[1,3,6]-(1):[4,7]-(2):[8]': [316830], '(0):[4,5]-(1):[3]-(2):[2]-(3):[1,6]': [316858]}
	   
   .. note::
   
      The rule of mentioning scenarios is : (Damage level):[list of units tag that damaged in this level] for example:
         '(0):[3]' shows a scenario with damaging plant unit 3 in damage level 0
         '(0):[3,5]-(1):[2]' shows a scenario with damaged plant units with tag 3 and 5 in damage level 0 and damaged plant unit with tag 2 at damage level 1
		 
		 
* **ScanariosSubScenario** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      "**ScanariosSubScenario**", "Post_Process_Object.ScanariosSubScenario()[Scenario name]", "This method returns a dictionary that its key is the Scenario name and the its result is next damage level scenarios."
	  
   Results sample:
   
   .. code-block::
   
      Post_Process_Object.ScanariosSubScenario()['(0):[3]']

      ['(0):[3]-(1):[2]', '(0):[3]-(1):[4]', '(0):[3]-(1):[2,4]', '(0):[3]-(1):[7,8]', '(0):[3]-(1):[7]', '(0):[3]-(1):[2,6]', '(0):[3]-(1):[4,7]', '(0):[3]-(1):[4,7,8]', '(0):[3]-(1):[2,7]', '(0):[3]-(1):[1,2]', '(0):[3]-(1):[2,4,7]', '(0):[3]-(1):[5,6,7]', '(0):[3]-(1):[6,7]']
   
   To see next level scenario:
   
   .. code-block::
      
      Post_Process_Object.ScanariosSubScenario()['(0):[3]-(1):[2]']

      ['(0):[3]-(1):[2]-(2):[1]', '(0):[3]-(1):[2]-(2):[5,6]', '(0):[3]-(1):[2]-(2):[6]', '(0):[3]-(1):[2]-(2):[7]', '(0):[3]-(1):[2]-(2):[1,6]', '(0):[3]-(1):[2]-(2):[4]', '(0):[3]-(1):[2]-(2):[4,7]', '(0):[3]-(1):[2]-(2):[6,7]']
	  
   
	   
   .. note::
   
      The rule of mentioning scenarios is : (Damage level):[list of units tag that damaged in this level] for example:
         '(0):[3]' shows a scenario with damaging plant unit 3 in damage level 0
         '(0):[3,5]-(1):[2]' shows a scenario with damaged plant units with tag 3 and 5 in damage level 0 and damaged plant unit with tag 2 at damage level 1
		 
		 
* **Damagelevel_Scenario_Dict** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      "**Damagelevel_Scenario_Dict**", "Post_Process_Object.Damagelevel_Scenario_Dict()", "This method returns a dictionary that its keys are the damage level and its values are list of the Scenarios in the corresponding level."
	
	
* **HazardMagnitude** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      "**HazardMagnitude**", "Post_Process_Object.HazardMagnitude()", "This method returns a list that each cell is a dictionary that its key is the hazard tag and each value is the sampled value."
	  
	  
* **NodesGroupRadiationDict** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      "**NodesGroupRadiationDict**", "Post_Process_Object.NodesGroupRadiationDict()", "This method returns a dictionary that its keys are the NodesGroup tag and the its result is a list of each node radiation average values."
	  
	  
* **NodesGroupOverPressureDict** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      "**NodesGroupOverPressureDict**", "Post_Process_Object.NodesGroupOverPressureDict()", "This method returns a dictionary that its keys are the NodesGroup tag and the its result is a list of each node Overpressure average values."
	  

* **NodesGroup_Rad_Probit_Dict** method


   .. csv-table:: 
      :header: "Method Name","How to call","Description"
      :widths: 10, 10, 40
   
      "**NodesGroup_Rad_Probit_Dict**", "Post_Process_Object.NodesGroup_Rad_Probit_Dict()", "This method returns a dictionary that its keys are the NodesGroup tag and the its result is a list of each node Radiation probit average values [Probit(Radiation)]."


PostProcess Plots
-----------------
   
   Using the following methods user can plot some data using PostProcess results.
   
   
   
* **plot_DamageLevel_ExpectedLoss**
   
   Using this command the expected loss of containment in each damage level will be plotted.

   .. function:: Post_Process_Object.plot_DamageLevel_ExpectedLoss(yaxistype='log',PlotMode=1)
   
   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
      yaxistype, str, "Type of the yaxis ['linear', 'log', 'date', 'category','multicategory']"
      PlotMode, int, "Options between 1,2 and 3 to plot on various editors."
	  
   .. admonition:: Example:
   
      The following demonstrates the use of the mentioned command. 
   
      **Python Code**
   
      .. code-block:: python
      
         import opensrane as opr
		
         Post_Process_Object=opr.PostProcess.ObjsRecorderPP('Recorder',100)
		 
         Post_Process_Object.plot_DamageLevel_ExpectedLoss('linear')
    
      The result of above command is:
	  
      .. raw:: html
          :file: figures/DamageLevel_ExpectedLoss.html
		  


* **plot_Unit_ZeroLevel_DamageProb**
   
   Using this command each plant unit damage probability in zero level will be plotted.

   .. function:: Post_Process_Object.plot_Unit_ZeroLevel_DamageProb(yaxistype='log',PlotMode=1)
   
   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
      yaxistype, str, "Type of the yaxis ['linear', 'log', 'date', 'category','multicategory']"
      PlotMode, int, "Options between 1,2 and 3 to plot on various editors."
	  
   .. admonition:: Example:
   
      The following demonstrates the use of the mentioned command. 
   
      **Python Code**
   
      .. code-block:: python
      
         import opensrane as opr
		
         Post_Process_Object=opr.PostProcess.ObjsRecorderPP('Recorder',100)
		 
         Post_Process_Object.plot_Unit_ZeroLevel_DamageProb(results,'linear')
    
      The result of above command is:
	  
      .. raw:: html
          :file: figures/Unit_ZeroLevel_DamageProb.html
		  

* **plot_Fragilities_Probits_Probability**
   
   Using this command each fragility and probit happening probability will be plotted.

   .. function:: Post_Process_Object.plot_Fragilities_Probits_Probability(yaxistype='log',PlotMode=1)
   
   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
      yaxistype, str, "Type of the yaxis ['linear', 'log', 'date', 'category','multicategory']"
      PlotMode, int, "Options between 1,2 and 3 to plot on various editors."
	  
   .. admonition:: Example:
   
      The following demonstrates the use of the mentioned command.
   
      **Python Code**
   
      .. code-block:: python
      
         import opensrane as opr
		
         Post_Process_Object=opr.PostProcess.ObjsRecorderPP('Recorder',100)
		 
         Post_Process_Object.plot_Fragilities_Probits_Probability('log')
    
      The result of above command is:
	  
      .. raw:: html
          :file: figures/Fragilities_Probits_Probability.html
		  

* **plot_Expected_Total_LOC**
   
   Using this command expected total loss of containment will be plotted.

   .. function:: Post_Process_Object.plot_Expected_Total_LOC(yaxistype='log',PlotMode=1)
   
   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
      yaxistype, str, "Type of the yaxis ['linear', 'log', 'date', 'category','multicategory']"
      PlotMode, int, "Options between 1,2 and 3 to plot on various editors."
	  
   .. admonition:: Example:
   
      The following demonstrates the use of the mentioned command. 
   
      **Python Code**
   
      .. code-block:: python
      
         import opensrane as opr
		
         Post_Process_Object=opr.PostProcess.ObjsRecorderPP('Recorder',100)
		 
         Post_Process_Object.plot_Expected_Total_LOC('log')
    
      The result of above command is:
	  
      .. raw:: html
          :file: figures/Expected_Total_LOC.html
		  

* **plot_ScenarioProbability**
   
   Using this command probability of scenarios will be plotted.

   .. function:: PPost_Process_Object.plot_ScenarioProbability(yaxistype='log',DamageLevel=[],ScenarioList=[],PlotMode=1,)
   
   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
      yaxistype, str, "Type of the yaxis ['linear', 'log', 'date', 'category','multicategory']"
      PlotMode, int, "Options between 1,2 and 3 to plot on various editors."
	  DamageLevel, list of int, List of damage level that user want to watch the results
	  ScenarioList, list of str, List of scenarios that want to be shown in plot. (for Empty it means that plot all scenarios)
	  
	  
   .. admonition:: Example:
   
      The following demonstrates the use of the mentioned command. 
   
      **Python Code**
   
      .. code-block:: python
      
         import opensrane as opr
		
         Post_Process_Object=opr.PostProcess.ObjsRecorderPP('Recorder',100)
		 
         Post_Process_Object.plot_ScenarioProbability('log',)
    
      The result of above command is:
	  
      .. raw:: html
          :file: figures/ScenarioProbability.html
      
      |

      And to plot just for damage level 0 and 1
	  
      .. code-block:: python
      
         import opensrane as opr
		
         Post_Process_Object=opr.PostProcess.ObjsRecorderPP('Recorder',100)
		 
         Post_Process_Object.plot_ScenarioProbability('log',DamageLevel=[0,1],)
		 
      .. raw:: html
          :file: figures/ScenarioProbability01.html
		  

      |

      And if user wants to plot for some specific scenarios:
	  
      .. code-block:: python
		 
         Post_Process_Object.plot_ScenarioProbability('linear', ScenarioList=[f'(0):[{i}]' for i in range(1,9)],)
		 
      .. raw:: html
          :file: figures/ScenarioProbabilityScens.html