.. _DateTime:

DateTime Command
****************

.. function:: DateAndTime.DateTime(Tag, Day_Night_Ratio=2)
   
   This command is used To define day night ratio.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  Day_Night_Ratio, float, Specifies the day to night ratio. The predefined value is 2 that means in a day 16 hours is duration of day and 8 hours is night duration.



   .. admonition:: Example:
   
      The following demonstrates the use of the DateTime command.
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.DateAndTime.DateTime(1,Day_Night_Ratio=2) 


Code Developed by: |bsz|