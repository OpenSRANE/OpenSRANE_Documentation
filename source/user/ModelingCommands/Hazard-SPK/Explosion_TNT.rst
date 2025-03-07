.. _Explosion_TNT:

Explosion_TNT Command
*********************

.. function:: Hazard.Explosion_TNT(Tag,TNT_weight, "X,Y,Z",CEP,n)
   
   This command allows the launch of a specified number of missiles with a defined explosive weight towards a target, with their accuracy determined by the Circular Error Probable (CEP). 

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
   
	  Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  TNT_weight, int, Weight of explosive (TNT) in kg.
	  "X,Y,Z", int, Coordinates of the target point.
	  CEP, int, Circular Error Probability is the radius of a circle within which 50% of impact points fall. It is a common measure of the accuracy of guided weapon systems.
	  n, int, Number of missiles.

   .. admonition:: Example:
   
      The following demonstrates the use of the Explosion_TNT command.
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        #Create an Object Hazard with Tag=1 and 3 explosions with 500 kg explosives to the target point at coordinates (x =-50, y =100, z=0) and a CEP of 10.
        hz=opr.Hazard.Explosion_TNT(1, 500, -50,100,0, 10, 3) 


Code Developed by: Saeedeh Koohestani
