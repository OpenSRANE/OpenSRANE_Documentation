.. _wipe:

wipe Command
************

.. function:: wipe

   This command is used to clear all defined |opr| objects, the recorders, and any analysis objects.
   
   wipe command is used to start over without having to exit and restart the software. This is useful for example if you want to change the model one or multiple parameters inside loops (In each loop a new parameter will be used)! It causes all elements, outflow and dispersion models to be removed. In addition it deletes all recorders, analysis objects and all material objects created. 
   
   .. admonition:: Example:
   
      The following demonstrates the use of the wipe command.
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
      
        opr.Misc.wipe()
   
      This command also can be call directly as shown in the following.
      
      .. code-block:: python
      
        import opensrane as opr
      
        opr.wipe()
	 
Code Developed by: |bsz|