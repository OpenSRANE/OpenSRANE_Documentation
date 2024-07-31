.. _wipeAnalysis:

wipeAnalysis Command
********************

.. function:: wipeAnalysis

   By this command all of the saved results and selected and assigned objects will be clear. Many objects depend on the user definition and generated random values will be select and will be assign to other objects in each simulation. For example, a defined outflow object may be assigned in a simulation to a plant unit object but in next simulation maybe no outflow will be happen, so by wipeAnalysis() command without clearing main objects, only resulted and assigned secondary objects will be clear and the main initial objects will remain.
   
   .. admonition:: Example:
   
      The following demonstrates the use of the wipeAnalysis command.
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
      
        opr.Misc.wipeAnalysis()
   

Code Developed by: |bsz|