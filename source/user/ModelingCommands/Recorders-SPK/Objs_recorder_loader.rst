.. _Objsrecorderloader:

Objs_recorder_loader module
============================


   
   This module contains the following subcommands that are used to load the recorded data using :ref:`Objs_recorder <Objsrecorder>`. In the following each subcommand with their usage are described. There are two approaches for loading recorded scenarios that are described in the following.
   
   .. note::
   
      **Important attention**:  As explained in :ref:`Objs_recorder <Objsrecorder>`, just subpackages that are defined using RecodingSubpackages option will be recorded and the other subpackages are recorded just once. The following approaches (Ordinary and Bank) are for loading the objects that are recorded in each simulation. So, the related commands in each approach will load just one scenario that contains objects that are defined for recording in each simulation and do not load other objects that are recorded only once. 
      
      
      Objects that are recorded only once also should be loaded for plotting and other purposes. To load these object the below command should be used.
	  
      * **LoadOtherSubPackages command**
	  
	  .. function:: Recorders.Objs_recorder_loader.LoadOtherSubPackages(filename)
   
         This command will load objects that are recorded only once and their subpackages are **not** defined in **RecodingSubpackages** option of :ref:`Objs_recorder <Objsrecorder>`. 
         
         .. csv-table:: 
            :header: "Argument", "Type", "Description"
            :widths: 10, 10, 40
         
            filename, str, Name of the :ref:`Objs_recorder <Objsrecorder>` created file.  

Ordinary approach
+++++++++++++++++

   In this approach only scenarios of one recoded file will be loaded in the memory. According to the number of target scenario, code loads the file that target scenario is stored in and then makes the target scenario as the current scenario. 
   
TotalNumberOfAnalysis subcommand
---------------------------------

   .. function:: Recorders.Objs_recorder_loader.TotalNumberOfAnalysis(filename)
   
      This command returns The number of total simulations or analysis that has been done and their happend or created scenarios are recorded with :ref:`Objs_recorder <Objsrecorder>`. 
   
      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40
      
         filename, str, Name of the :ref:`Objs_recorder <Objsrecorder>` created file.  
		 
   .. note::
   
      Attention: User determines the number of simulation or analysis and this subcommand returns this number. During the analysis only created scenarios will be recorded and the number of created or recorded scenarios can be called using TotalNumberOfScenarios subcommand that is explained in the following.

TotalNumberOfScenarios subcommand
---------------------------------

   .. function:: Recorders.Objs_recorder_loader.TotalNumberOfScenarios(filename)
   
      This command returns The number of total created and recorded scenarios using :ref:`Objs_recorder <Objsrecorder>`.
   
      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40
      
         filename, str, Name of the :ref:`Objs_recorder <Objsrecorder>` created file.  

load1RecordedScenario subcommand
--------------------------------

   .. function:: Recorders.Objs_recorder_loader.load1RecordedScenario(ScenarioNumber, filename)
   
      This command loads created Scenario with number ScenarioNumber. 
   
      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40
      
         ScenarioNumber, int, Number of target Scenario that wanna be open.
         filename, str, Name of the :ref:`Objs_recorder <Objsrecorder>` created file.  

load1ScenarioItt subcommand
--------------------------------

   .. function:: Recorders.Objs_recorder_loader.load1ScenarioItt(ScenarioNumber, filename)
   
      This command loads created Scenario with number ScenarioNumber. The difference of this command with previous command (load1RecordedScenario) is in its speed. This command is great and fast when you use it inside a loop while the previous command is great when you wanna load just one scenario.
   
      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40
      
         ScenarioNumber, int, Number of target Scenario that wanna be open.
         filename, str, Name of the :ref:`Objs_recorder <Objsrecorder>` created file. 

Bank approach
+++++++++++++

   Bank approach is another way to load scenarios. It loads all scenarios into the memory and so calling them are so much fast but if there were no enough memory probably user encounter with system problem!
   So just use it when a powerful system is available.

   .. note::
   
      **THIS METHOD USES HUGE AMOUNT OF MEMORY AND NOT RECOMMENDED FOR LARGE SIMULATIONS NUMBER**. 

loadScenarioBank SUBCOMMAND
---------------------------

   .. function:: Recorders.Objs_recorder_loader.loadScenarioBank(filename)
   
      This command loads all recorder scenarios using :ref:`Objs_recorder <Objsrecorder>` in to the system memory. User can send all recorded scenarios (ScenarioBank) to the memory and call them faster. It is obvious that weak systems with low memory capacity, this method may encounter with system hanging. Also, it returns all scenarios as a dictionary that keys are the number of the simulation.
   
      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40
      
         filename, str, Name of the :ref:`Objs_recorder <Objsrecorder>` created file.
     

load1ScenarioOfBank SUBCOMMAND
------------------------------

   .. function:: opr.Recorders.Objs_recorder_loader.load1ScenarioOfBank(ScenarioTag)
   
      By defining the file name to previous command (loadScenarioBank), all the recorded scenarios with all their objects will be load in the memory. **After loading the scenario bank using loadScenarioBank**, Using this command, user can load a scenario into the memory. **By loading a scenario into the memory, it is ready to be investigated and ready to plot and also all analysis results are accessible**.
   
      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40
      
         ScenarioTag, int, The number of desired scenario.      
   

ClearScenarioBank SUBCOMMAND
------------------------------

   .. function:: opr.Recorders.Objs_recorder_loader.ClearScenarioBank()
   
      By the this command memory will be clear from loaded Scenario Bank.
   


Code Developed by: |bsz|