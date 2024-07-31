.. _MultiParallel:

MultiParallel Command
*********************

.. function:: opr.Analyze.ScenarioAnalyze.MultiParallel(AnalysisNumber=100, NumberOfProcessors=3, RecordersSaveStep=5000)

   
   By this command users can analyze their model with multiple cores or CPUs. Depend on the number of the cores the analysis duration will be reduce more. 
   
   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
      RecordersSaveStep, int, "for recorder objects, this number will be consider as save step and each processor will run analysis with this number of analysis and then save the recorded results (All recorded data or objects will be removed from memory to defined files in recorders) and then will go to next analysis."

   .. note::
   
      * If user define NumberOfProcessors more than the number of the available cores, it will be reduced to the available number of the cores.
      
      * Users should pay attention that this command should be used after (if __name__=='__main__':) and outside of that, it will be encounter with error!. Because of mentioned limitation it cannot be used inside the Jupyter NoteBook (for windows operating system). Here is an example of how should it be hire:
   
   .. note::
      Initially this command had **MergeSavedFiles** that was used to merge all saved files. But this option moved to recorders and objs_recorders and now this option does not have any effect on performance of the command.
	  
   .. admonition:: Example:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        if __name__=='__main__':
           opr.Analyze.ScenarioAnalyze.MultiParallel(AnalysisNumber=1_000_000, NumberOfProcessors=15, RecordersSaveStep=5000)

   .. warning::
   
      Users should attention that **Never use MultiParallel inside a loop!**. MultiParallel uses **multiprocessing** package that contains commands for parallel proccessing but it do not let you to use it inside a loop and you probably encounter with errors. This issue happens on windows operating system and maybe on mac and linux you'll find no error!
      
      There are some tricks that you can use MultiParallel command inside a loop. Look at the examples to get somes ideas.
	  

Code Developed by: |bsz|