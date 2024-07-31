.. _warning:

warning Command
***************

.. function:: warning(string)
   
   This command is used to add a desired text to warning file (**Warnings.wrn**). By running this command a warning file will be created in the folder of the model python file. The text will be added to the warning file and an alert will be apear on the console that shows the warning file is created.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
      string, str, text of the warning


   .. admonition:: Example:
   
      The following demonstrates the use of the warning command.
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
      
        opr.Misc.warning('This text will be printed in the warning file')

.. note::

   There are some **internal warning** that shows model problem or lack of data. So, by start of the analysis, even user didn't define any warning inside the model, if code encounter with problems the warning alarm will be appear.
   
.. warning::

	It is highly recommended that user solve the problems mentioned in the warning file and provide a model without **internal warnings**.

Code Developed by: |bsz|