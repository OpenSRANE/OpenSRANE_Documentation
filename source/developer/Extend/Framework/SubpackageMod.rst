.. _SBPKMDLS:

*******************
Subpackage modules
*******************

SubPackages Modules should comply the following important rules:

   * Each module should contain a class and **its name should be equal to the filename of the module**.
   * The **_NewClass** and **_GlobalParameters** should be imported to be inherited by the module class as shown in the following example.
   * The **__init__** command should have **tag** argument just after self and then it is obvious that required class arguments and GlobalPrameter arguments (_globalParametersArguments) also should be define.
   * After **__init__** definition, the 2 lines that are shown in Fix Part block (As shown in the following example) should be define without any changes and finally :ref:`_globalParameters <FrameworkGLBP>` should be initialize using the defined arguments.
   
   .. admonition:: Example:
   
      **Python Code**
      
      .. code-block:: python
      
         class _GlobalParameters():
		    
            from opensrane.Misc._NewClass import _NewClass
            from ._GlobalParameters import _GlobalParameters
            
            class moduleFilename(_NewClass,_GlobalParameters):
            
            	def __init__(self,tag,arguments, _globalParametersArguments):
                    
                    #---- Fix Part for each class __init__ ----
                    ObjManager.Add(tag,self)
                    _NewClass.__init__(self,tag)
                    #------------------------------------------
                            
                    _GlobalParameters.__init__(self, _globalParametersArguments)
             
      * After above part the class content can be written. All modules in the subpackages obey the mention rules and are proper samples to check the above rules and how they are implemented.
      * Developed classes can have their own methods but they should have all methods that are defined in the _GlobalParameters.py located in the subpackage folder and should return the parameters that are specified. 