.. _Recorder:

Recorder Command
================

.. function:: Recorders.recorder(tag, filename='Recorder', fileAppend=True, recordfield='DamageLevel', NodesGroupTag=1, MergeSavedFiles=False)

  
   Using this command, a specific result will be recorded for each simulation. The results that can be recorded by this command are listed in the following. The command is fast and it do not take much huge hard disk space. The simulated scenarios will no longer exist and user cannot load them after analysis.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  filename, str, Name of the file that user wants to record data in.
	  fileAppend, boolean, "True says that if the filename exists, add the recorded scenarios to the existing file and false will clear the file if exists."
      recordfield, str, "A specific Flag that shows which data should be record. In the following, the possible Flags are described."
	  NodesGroupTag, int, "If a property of a NodesGroup is considered in the recordfield to record, the tag of the NodesGroup object should be define here."
      MergeSavedFiles, boolean, "By setting this option to True, When analysis finished all saved files will be merge into one file with suffix M. Attention that for huge models it may takes so much memory and time and is not recomonded for huge models!"
	  
   .. note::
      
      The **recordfield** existing Flags are as the following table:
	  
      .. csv-table:: 
         :header: "Flag", "Needs NodesGroupTag" ,  "Description"
         :widths: 10, 10, 40
      
         'DamageLevel', No, Records the damage level of each plant unit with respect to the tag number (DamageLevel: the level that the plant unit got damage)
         'NodesGroupIsDamaged', Yes, Records the nodesgroup with tag equal NodesGroupTag is damaged or not (0 for not damaged and 1 for damaged or failed or dead).
         'FragilityTag', No, Records Fragility tag of each damaged plant unit. Every recorded value is the fragility tag number that cause damage to the corresponding plant unit.
		 'LOC', No, Records loss of containment value of each plant unit.
		 'HazardMag', No, Records the sampled hazard magnitude.
		 'NodesRadiationOverPressure', Yes, "Records NodesGroup Radiation and OverPressure values (To prevent creating huge files, the number are recorded with 4 decimals)."
		 'NodesRadiationProbit', Yes, Records the NodesGroup Radiation probit value [Probit(Radiation)]
		 'NodesOverPressureProbit', Yes, Records the NodesGroup OverPressure probit value [Probit(OverPressure)]
	  
	  

   .. admonition:: Example:
   
      The following demonstrates the use of the Recorder command.
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        #To record each simulation DamagedLevel of each plant unit and store in 'RecorderDam' file
        opr.Recorders.recorder(tag=1, filename='RecorderDam', fileAppend=False, recordfield='DamageLevel',)
		
        #To record nodes damage probability under radiation using defined probit function and store results is RecorderNodeRad for nodesgroup with tag 2
        opr.Recorders.recorder(tag=2, filename='RecorderNodeRad', fileAppend=False, recordfield='NodesRadiationProbit',NodesGroupTag=2)

Code Developed by: |bsz|