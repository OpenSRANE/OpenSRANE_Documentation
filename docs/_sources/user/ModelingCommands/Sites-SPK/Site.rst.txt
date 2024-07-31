.. _site:

Site Command
************

.. function:: Sites.Site(Tag, Temprature=293, Pressure=100000, g=9.81, OngroundTemprature=None, Airdensity=1.21, Humidity=0.6,)
   
   This command is used for defining various properties of the site that target plant is located in.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  Temperature, float, Specifies site atmosphere temperature
	  Pressure, float, Specifies site atmosphere pressure.
	  g, float, Earth gravity acceleration. 
	  OngroundTemprature, float, Specifies the site onground temperature.
	  Airdensity, float, Obvious. 
	  Humidity, float, Obvious.



   .. admonition:: Example:
   
      The following demonstrates the use of the Site command.
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.Sites.Site(SiteTAg, Temprature=25+273, Pressure=1*10**5, g=9.81, OngroundTemprature=23+273, Airdensity=1.21, Humidity=0.6) 


Code Developed by: |bsz|