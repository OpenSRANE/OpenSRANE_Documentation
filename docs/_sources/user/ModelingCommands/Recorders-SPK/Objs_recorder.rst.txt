.. _Objsrecorder:

Objs_recorder Command
*********************

.. function:: Recorders.Objs_recorder(tag, filename='', fileAppend=True, RecodingSubpackages=['PlantUnits', 'Hazard', 'DateAndTime', 'WindData', 'NodesGroups'], MergeSavedFiles=False)

   
   Using this command, a file will be determined by the user to record all simulated scenarios objects. By every analyze, the created objects and results will be record in the mentioned file and user can call them using the load commands.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  filename, str, Name of the file that user wants to record data in.
	  fileAppend, boolean, "True says that if the filename exists, add the recorded scenarios to the existing file and false will clear the file if exists."
	  RecodingSubpackages, list, "List of subpackages that Users wanna to be recorded by recorders. The default value is ['PlantUnits','Hazard', 'DateAndTime', 'WindData'] which contains some variables that their values usually changaed by each simulation. But also other subpackages can be added by user except 'Recorders'. The Other subpackages that their variables values are initially assigned and never changes during simulation will be record once at the first savefile."
      MergeSavedFiles, boolean, "By setting this option to True, When analysis finished all saved files will be merge into one file with suffix M. Attention that for huge models it take so much memory and time and is not recomonded for huge models!"


   .. admonition:: Example:
   
      The following demonstrates the use of the Objs_recorder command and just saves 'PlantUnits' objects in each simulation.
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.Recorders.Objs_recorder(tag=1, filename='ObjsRecorder', SaveStep=100, fileAppend=False, RecodingSubpackages=['PlantUnits'])


   .. note::
      Attention: Initially this command had SaveStep option that was the Number of steps that after that data will be move to the file and memory become empty but it has removed to Anlysis command because different recorders because of parallel issues can not have different save step. So, the following definition does not exist here else. To prevent any probable error still it exist in the input argument but do not have any effect.
      
      
   	  **SaveStep, int, Number of steps that after that data will be move to the file and memory become empty. Bigger values cause faster analysis but it needs enough system memory.**

Code Developed by: |bsz|