.. _Acs2Obj:

*************************
Access to defined objects
*************************

In any subpackage there is an ObjManager class that can be call and have 2 variables that stores defined objects data (Taglst, TagObjDict). 

* Taglst: Returns list of the defined objects tags.
* TagObjDict: Returns dictionary of the defined objects that its keys are tag of the objects and its values are the corresponding defined object.

So, users to get access to the defined object using defined tag can use TagObjDict and enter the tag of the object and get the defined object. For example, if user want to get defined plant unit object with tag 4:

   .. code-block:: python
  
	 opr.PlantUnits.ObjManager.TagObjDict[4]

or if user wants to get all defined tags can get them using Taglst:

   .. code-block:: python
  
	 opr.PlantUnits.ObjManager.Taglst