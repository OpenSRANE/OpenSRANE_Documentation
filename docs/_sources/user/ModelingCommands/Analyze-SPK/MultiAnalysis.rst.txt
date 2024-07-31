.. _MultiAnalysis:

MultiAnalysis Command
*********************

.. function:: opr.Analyze.ScenarioAnalyze.MultiAnalysis(AnalysisNumber=100, fileindex=0)
   
   This command as obvious from its name, **implement multiple analysis** equal to specified AnalysisNumber.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
      AnalysisNumber, int, Number of analysis that should be run
	  fileindex, int, An integer value that will be add to the end of the filename to save recorded scenarios in seperate file.
	  
   .. note::
     Initially this command had **MergeSavedFiles** that was used to merge all saved files. But this option moved to recorders and objs_recorders and now this option does not have any effect on performance of the command.
   	  
	  
.. note::

   When the number of analyses reaches to the defined SaveStep number, the resulted scenarios will be saved in the defined file specified in the recorder object with defined fileindex as suffix. 
   


Code Developed by: |bsz|