.. _UniAnalyze:

UniAnalyze Command
******************

.. function:: opr.Analyze.ScenarioAnalyze.UniAnalyze(SavetoFile=True, fileindex=0, MergeSavedFiles=False)
   
   By running this command, **only one scenario analysis will be run** and the defined algorithm will be implemented for defined model. After running this command all recorder objects will record the results.
   
   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
      SavetoFile, boolean, "Setting this command to True leads to move all recorded data from memort to a file. When user run this command with setting SavetoFile to True, then all recorded objects or data will be moved to the defined file."
      fileindex, int, An integer value that will be add to the end of the filename to save recorded scenarios in seperate file.
      MergeSavedFiles, boolean, "If set this option into True, When analysis finished it runs merge and clear method for all recorder objects and for any recorder object that MergeSavedFiles was set to true it will merge all saved files to a file with M suffix."
	  

.. note::

   When one analyze finished, all objects and results are in the memory and user can use them for post processing. By running next analysis without setting SavetoFile option to True, the previous results will go into the memory of the system and new results will be activate. By setting SavetoFile option to True all recorded data or objects will be move into the defined filename with defined index and memory will be clear. 
   
   if user set SavetoFile to False, then the results won't save into the defined recorder object and results remain in the memory. If user, for some reasons had to use UniAnalyze to do multiple analysis, then the SavetoFile option can set to False to make the analysis faster and then after some steps (for example 1000 steps) can set it True till the recorded results will be save into the defined recorder file or object.
   


Code Developed by: |bsz|