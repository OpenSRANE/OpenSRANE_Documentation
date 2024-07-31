.. _build:

********************
Building Application
********************

   After providing the source code on your local machine (:ref:`source <sourceCode>`), using following commands the build process is somewhat simple! 
   
   * First check if an existing version of |opr| exist in the installed packages, remove it (using command prompt for windows). 
   
      .. code-block:: console
         :caption: Remove the existing |opr| package from local machine 
	     
         pip uninstall OpenSRANE
	  
   * To install the forked |opr| on you local machine, go to the |opr| folder and delete **setup.py** and rename the **setup-Local.py** to **setup.py**.
   
   * Go to the |opr| folder that **setup.py** exist and using command prompt for windows run the following command.
   
      .. code-block:: console
         :caption: Installing |opr| package from local machine 
	     
         pip install -e .
		 
   Now |opr| has been installed on your local machine and any changes in the source code will be directly implement on |opr|.
   
.. note::

   * Attention that **setup.py** and **setup-Local.py** changes should not be push to the main repository.