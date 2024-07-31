.. _MatDataBank:

DataBank Command
****************

.. function:: Substance.DataBank.SAVEDMATERIALNAME(Tag)
   
   This command is used for defining the substances using predefined data.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  

   .. note::
   
      * DataBank command has saved materials in its self. To call one of the saved materials, by putting a "." sign after DataBank command, list of the predefined materials will be appear (Some editors may not show). Then user should enter the tag number of the selected material in parenthesis just after the selected material.
	  
      * After selecting the material, it is also possible to define or modify some properties of selected material. This case is also shown in the following example part. List of existing materials in the DataBank are mentioned in the following list.
   
   **List of existing materials in DataBank**
   
   .. csv-table::
      :header: "Name"
      :widths: 10
   
      Butene
      Dimethylhydrazine
      propane
      Octane
      n_hexane
      Gasoline
	  LPG_Liquefied_Petroleum_Gas

   .. admonition:: Example:
   
      Define some materials using DataBank command:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.Substance.DataBank.Butene(1)
        
        opr.Substance.DataBank.Dimethylhydrazine(2)
   
      Define a material using DataBank and modify or add some properties to it:

      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr	  

Code Developed by: |bsz|