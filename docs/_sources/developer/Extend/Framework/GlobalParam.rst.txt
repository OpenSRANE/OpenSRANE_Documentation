.. _FrameworkGLBP:

*******************
_GlobalParameters
*******************

   Every subpackage as shown in :ref:`Fig.1 <SPKStrFig>` contains a **_GlobalParameters.py** file that involves variables and methods that are common for all classes inside the subpackage. It plays a key rule to make integrity between subpackage modules and specifies the minimum methods and variables and type of variables that each module should have.

   It contains GlobalParameters class and all of the common variables and methods with no initial values and calculations are defined in this class and they show that subpackage modules should contain and fill these methods and variables.

   .. _FrameworkEx1:
   
   .. admonition:: Example:
   
      The `_GlobalParameters.py <https://github.com/OpenSRANE/OpenSRANE/blob/main/opensrane/OutFlowModel/_GlobalParameters.py>`_ file content of `OutFlowModel <https://github.com/OpenSRANE/OpenSRANE/blob/main/opensrane/OutFlowModel/>`_ subpackage has been shown as a sample in the following. 
      
      **Python Code**
      
      .. code-block:: python
      
         class _GlobalParameters():
   
   
             def __init__(self):
                 
                 self.wipeAnalysis()
          
             def wipeAnalysisGlobal(self):    
             
                 self.t_release=None  #Time list of outFlow or release
                 
                 self.MassLiquidReleaseRate=None   #Mass Liquid Release rate in each step 
                 self.dMassLiquid_release=None     #Mass Liquid list of OutFlow Or release in each time step (Delta Mass)
                 self.TotalMassLiquid_Release=None #Total Mass Liquid list of OutFlow Or release in each time step
                 
                 self.MassGasReleaseRate=None      #Mass Gas Release rate in each step 
                 self.dMassGas_release=None        #Mass Gas list of OutFlow Or release in each time step (Delta Mass)
                 self.TotalMassGas_Release=None    #Total Mass Gas list of OutFlow Or release in each time step
                 
                 self.UnitObject=None
          
             def wipeAnalysis(self):
                 self.wipeAnalysisGlobal()
                 pass          
                 
   
             def Calculate(self):
                 
                 UnitObject=self.UnitObject #self.UnitObject is defined in _GlobalParameters
                 if UnitObject==None:         
                     raise 'Error: self.UnitObject is emptey and before any usage it should be assigned before'
                 
                 return -1
   
      Variables like **MassLiquidReleaseRate, dMassLiquid_release, TotalMassLiquid_Release and ...** are the ones that every class of outflow subpackage should calculate and fill them. These variables in each analysis or sampling could varies depend on the various conditions, so they should be reset at the start of each analysis. To get ensure these variables will be restart and the beginning of the analysis, they are put in **wipeAnalysisGlobal(self)** that will be explained in related part. Also, there is a **Calculate(self)** method that all classes in the `OutFlowModel <https://github.com/OpenSRANE/OpenSRANE/blob/main/opensrane/OutFlowModel/>`_ subpackage, should have this method and calculate and return what is explained in its related description in :ref:`outflow subpackage structure <OutFlowModelEx>` part.
                  


   All classes in each subpackage should inherits **_GlobalParameters** class and initialize the _GlobalParameters variables and also fill them with the results or entered parameters by the user. Also, methods that should be common for all classes in the subpackage should be define in _GlobalParameters class. However, in any class the method code can changes by developer. 

   These parameters should be filled by each module and the results of calculations should be stored in them. Each module can have their own internal methods and these methods are used only for internal calculations of the module and they won’t be call with other modules or subpackages. Sometimes there are some methods that maybe useful for subpackage modules so they are located in _GlobalParameters.py and started with “_” sign.
   
   .. _FrameworkEx2:
   
   .. admonition:: Example:
      
	  In the following code `Liquid10Min <https://github.com/OpenSRANE/OpenSRANE/blob/main/opensrane/OutFlowModel/Liquid10min.py>`_ class from `OutFlowModel <https://github.com/OpenSRANE/OpenSRANE/blob/main/opensrane/OutFlowModel/>`_ subpackage has been shown as a sample. 
	  
      **Python Code**
      
      .. code-block:: python
      
         class Liquid10min(_NewClass,_GlobalParameters):
             
             def __init__(self,tag):
                 
                 #---- Fix Part for each class __init__ ----
                 ObjManager.Add(tag,self)
                 _NewClass.__init__(self,tag)
                 #------------------------------------------
                 
                 _GlobalParameters.__init__(self)
                 
                 self.name=f'Liquid10Min'
                 self.wipeAnalysis()
             
             def wipeAnalysis(self):

                 self.wipeAnalysisGlobal()
                 
             def Calculate(self):
                 
                 UnitObject=self.UnitObject #self.UnitObject has been defined in _GlobalParameters
                 if UnitObject==None:         
                     raise 'Error: self.UnitObject is empty and before any usage it should be assigned before'

                 time=10
                 dt=60
                 
                 t_release=[i for i in range(time)]
                 MassLiquidReleaseRate=[UnitObject.V_subs/time for i in range(time)]
                 dMassLiquid_release=[UnitObject.V_subs/time*dt for i in range(time)]
                 TotalMassLiquid_Release=[sum(dMassLiquid_release[0:i]) for i in range(1,len(dMassLiquid_release)+1)]
                 
                 self.t_release=t_release
                 self.MassLiquidReleaseRate=MassLiquidReleaseRate
                 self.dMassLiquid_release=dMassLiquid_release   
                 self.TotalMassLiquid_Release=TotalMassLiquid_Release   
         
                 self.MassGasReleaseRate=[0 for i in self.t_release]
                 self.dMassGas_release=[0 for i in self.t_release]
                 self.TotalMassGas_Release=[0 for i in self.t_release]        
                 
                 return 0
				 
      As shown in the above code `Liquid10Min <https://github.com/OpenSRANE/OpenSRANE/blob/main/opensrane/OutFlowModel/Liquid10min.py>`_ class has inherited the _GlobalParameters and initialized it. **Developers should pay attention that never change the fix part shown in the beginning of the classes**. As it is seen, the Calculate() method that defined in the _GlobalParameters, filled with and in this method the global parameters is calculated. **In** :ref:`OpenSRANE Framework architecture page <extend>` **the parameters and methods of each subpackage has been explained**. 



   For some subpackages there are Calculate method in some _GlobalParameters.py is responsible to start module calculations to fill the parameters with results. So, the main code of the module should be written in the Calculate method and this part is called by analysis subpackage and after it, the parameters should be filled by the results.

   There are some other methods in some _GlobalParameters.py (That are not started with “_”). These methods can be called and used within each module (class) and may help developers to calculate some calculations more convenient. These methods are explained in each subpackage description in :ref:`OpenSRANE Framework architecture page <extend>`.
 

.. _wipeAnalysisEX:

wipeAnalysis and wipeAnalysisGlobal
-----------------------------------
	   
   wipeAnalysis and wipeAnalysisGlobal in _GlobalParameters.py and classes are very important methods that show the local and global parameters that should filled with their initial value at the beginning of each analysis.

   :ref:`wipeAnalysisGlobal <wipeAnalysisEX>` contains variables that are common between all classes and after each analysis by calling wipeAnalysis command their assigned data will be clear and the initial value should be assigned to them to get ready for next analysis. These variables are those that will be use and call by the other classes in other SubPackages or call by recorders or by users to be stored for postprocess analysis. :ref:`wipeAnalysis <wipeAnalysisEX>` method or command is responsible to reset and initialize the class local variables and the :ref:`wipeAnalysisGlobal <wipeAnalysisEX>` method should be called inside this method and by this way all global variables also will be reset. 
   
   :ref:`wipeAnalysis <wipeAnalysisEX>` in _GlobalParameters.py is for module parameters and it is responsible to initialize the parameters that are used only inside the module at the start of each analysis and remove the last analysis values from them. To making code briefer, the code only calls wipeAnalysis and so in each wipeAnalysis command the wipeAnalysisGlobal also should be called to reset the global parameters. (Watch :ref:`Example1 <FrameworkEx1>` and :ref:`Example2 <FrameworkEx2>`)
   
   So, each time that analysis command repeat, these parameters will be reset and initialize and their previous values from the last analysis will be removed. **constant variables and variables that their values won't change do not need to be defined in the** :ref:`wipeAnalysisGlobal or wipeAnalysis <wipeAnalysisEX>` **body**.