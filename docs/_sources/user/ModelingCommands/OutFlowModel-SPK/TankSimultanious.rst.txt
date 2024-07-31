.. _TankSimultanious:

TankSimultanious Command
************************

.. function:: OutFlowModel.TankSimultanious(Tag, Release_Ratio=1)
   
   This model considers a simultaneous release from Tank with a volume equal to the entered ratio of total amount of stored material by the user.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  "Release_Ratio", float, "A value between 0 and 1 that defines the ratio of released material with respect to the total amount of the stored material in the Tank. As it is shown in the command structure if user don't enter anything for this parameter, it will be consider equal unity."


   .. admonition:: Example:
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.OutFlowModel.TankSimultanious(Tag=9, Release_Ratio=0.65)

Code Developed by: |bsz|