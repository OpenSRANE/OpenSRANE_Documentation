.. _BasicExam4:

*********************************************
Basic Example 4. (Individual Risk for 1 Tank) 
*********************************************

In this example one tank has been modeled and the individual risk of the tank calculated.

Data are recorded by Objs_recorder. Also the code completely can be downloaded from :download:`here <files/Basic Example4.ipynb>` in the Jupyter Notebook format.


Import required packages
************************

In this example only |opr| package is enough and there is no need to any other Python packages. So:

   .. code-block:: python
      
	  import opensrane as opr
	  


Initialize the model and define reorder
***************************************
   
   .. code-block:: python
      
      #Wipe the model to clear any created object if it is created before
      opr.wipe()
      
      #Define the recorder
      opr.Recorders.Objs_recorder(tag=1,filename='Recorder_ex4', fileAppend=False)
      
      #Clear Warning File content
      opr.Misc.warningClear()
	
	
Define Hazard Curve and DateTime object and wind Data and Site data
*******************************************************************

   .. code-block:: python
      
      #define Hazard Curve
      PGA=[1.4, 1.29984,1.27091,1.24865,1.22194,1.20191,1.17297,1.13959,1.11065,1.08172, 
           1.05501,1.03275,0.994913,0.961526,0.92814,0.899205,0.872496,0.843561,0.816852, 
           0.790143,0.761208,0.732273,0.696661,0.667727,0.636566,0.609857,0.589825,0.569793, 
           0.549762,0.525278,0.503021,0.48744,0.469634,0.451828,0.431797,0.409539,0.38283, 
           0.356121,0.338315,0.307154,0.280445,0.260413,0.23593,0.211447,0.17806,0.158029, 
           0.142448,0.126868,0.113514,0.0979332,0.0845787,0.0712242,0.0578696,0.0534181, 
           0.0489666,0.0445151,0.0356121,0.0356121,0.0311606, 0]
      PGA=[p*9.81 for p in PGA]
      
      Prob=[0, 0.000000446937,0.000000529832,0.000000607087,0.000000695608,0.000000824624,0.000000944864, 
            0.00000115888,0.00000137382,0.00000157414,0.0000019307,0.00000206667,0.00000262252,0.00000321654, 
            0.00000381312,0.00000452035,0.00000535876,0.00000657255,0.00000779158,0.00000955643,0.0000113289, 
            0.0000134301,0.0000176322,0.000021626,0.0000265244,0.0000325323,0.0000372759,0.0000441896,0.000050633, 
            0.0000621017,0.0000711569,0.0000843545,0.0000966544,0.000110748,0.000131288,0.000155639,0.0001975, 
            0.000259294,0.000318026,0.000403563,0.000548171,0.000744597,0.00104642,0.00152148,0.00253478,0.00356225, 
            0.00467682,0.00657255,0.00892769,0.0109499,0.0143759,0.0209024,0.0274425,0.0325323,0.0399011,0.048939, 
            0.060024,0.0687762,0.0843545, 0.9999]
      
      opr.Hazard.Earthquake(1,'PGA',PGA,Prob) #Create Hazard Object with tag=1 that is 0th Object
      
      #Define date time distribution
      opr.DateAndTime.DateTime(1,Day_Night_Ratio=2)
      
      #Define a simple windRose
      windobj=opr.WindData.WindRose(1)
      
      windobj.WindDayClassList=['F','D','D']  
      windobj.WindNightClassList=['F','D','D']
      
      windobj.AlphaCOEFlist=[0.6,0.25,0]
      
      windobj.DayWindSpeedList=[[1,5],[5,9],[9]]
      windobj.NightWindSpeedList=[[1,5],[5,9],[9]]
      
      windobj.DayWindFreqMatrix=[[0.5,0.5,0],
                              [0.5,0.5,0],
                              [0.5,0.5,0],
                              [0.5,0.5,0],
                                ]                                      
      windobj.NightWindFreqMatrix=windobj.DayWindFreqMatrix
	  
      #Define Site Condition and Geometry
      SiteTAg=1
      opr.Sites.Site(SiteTAg, Temperature=25+273, Pressure=1*10**5, XSiteBoundary=[0,100,100,0], YSiteBoundary=[0,0,100,100], g=9.81)
	  
	  
Define Materials and Fragilities and Probits
*******************************************************************
   
   Butene considered as tank content. A new value considered for the specific heat of combustion of this material, so the considered value of defined object modified after the definition.

   .. code-block:: python
      
      #Define Substances
      opr.Substance.DataBank.Butene(1) #Use DataBank to Load Material
      opr.Substance.ObjManager[1].Specific_Heat_of_Combustion=45.334*10**6
      
      #Define Fragilities
      opr.Fragilities.Fragility(tag=1,Distribution_Type='lognormal',modename='EBF',mean=-0.652,StdDev=0.286)
      opr.Fragilities.Fragility(tag=2,Distribution_Type='lognormal',modename='GDF',mean=-0.659,StdDev=0.452)
      
      #Define Probits
      Radiation=3
      opr.Fragilities.Probit(tag=Radiation, Distribution_Type='normal', K1=1/5000, K2=5-25000/5000)
      PeopleOverP=4
      opr.Fragilities.Probit(tag=PeopleOverP, Distribution_Type='normal', K1=1/3000, K2=5-20000/3000,MinRndVar=5000)
      PeopleRadiation=5
      opr.Fragilities.Probit(tag=PeopleRadiation, Distribution_Type='normal', K1=1/4000, K2=5-14500/4000,MinRndVar=2500)

Define Outflow, Dispersion and physical effect models
*******************************************************************

   Two different outflow model considered. Also, for all considered outflow models just one dispersion model defined. And fire point source model defined for physical events.
   
   .. code-block:: python
      
      #Define Outflow Models
      tag=1
      opr.OutFlowModel.TankHole(tag, Hole_Diameter=0.05, Hole_Height_FromBot=0, delta_t=500, Cd=1)
      opr.OutFlowModel.SimultaniousLiquid(2)
      
      #Define Dispersion Spread Models and their connections to the materials and outflows
      opr.DispersionSpreadModels.LiquidSpread(tag=1, MatTags=[1], OutFlowModelTags=[1,2],MinDisThickness=0.005,)
      
      #Define Physical Effect models
      opr.PhysicalEffect.fire_point_source(tag=1, minf=0.055, k=1.5)

Define connectors to connect models to each other
*******************************************************************

   DS_LOC: 
      
	  Using DS_LOC for damages caused under Fragility tag 1 the outflow model with tag 2 will be consider as the outflow model. Also, for damages caused under Fragility tag 2 the outflow model with tag 1 will be consider as the outflow model.
   
   Out_Physic: 
      
	  For any unit that have material with tag 1 and Outflow with tag 1 the physical effect with tag 1 will be considered. Also, For any unit that have material with tag 1 and Outflow with tag 2 the physical effect with tag 1 will be considered again. 
   
   Pb_LOC:
      
	  Finally for any units that damaged under because probit tag equal to 3 (Radiation was equal to 3) outflow model with tags 1 or 2 will be consider for them with equal probability. The probability of of seleccting outflowmodel 1 or 2 is equal because the defined weight for them is similar (LOCProbabilityList=[1,1]).
   
   .. code-block:: python
      
      #Define the DS_LOC for each Fragility
      opr.Connectors.DS_LOC(1,FragilityTag=1,OutFlowModelTagList=[2],LOCProbabilityList=[1])
      opr.Connectors.DS_LOC(2,FragilityTag=2,OutFlowModelTagList=[1],LOCProbabilityList=[1])
	  
      #Define OutFlow-Phisycal Effect connection
      opr.Connectors.Out_Physic(tag=3,OutFlowTag=1, MaterialsTagList=[1],PhysicalEffectTagList=[1],PhysProbabilityList=[1])
      opr.Connectors.Out_Physic(tag=4,OutFlowTag=2, MaterialsTagList=[1],PhysicalEffectTagList=[1],PhysProbabilityList=[1])
      
      #Define Probit - LOC loss of containment Connectors
      opr.Connectors.Pb_LOC(tag=5, ProbitTag=Radiation, OutFlowModelTagList=[1,2], LOCProbabilityList=[1,1])

Define Safety dike, plant units and NodesGroups object
*******************************************************************

   Plant units defined and its properties according defined models tag specified for them. The Fragility tag and vulnerability probit and their location and material and internal pressure and temprature and ... . Also, to calculate individual risk, a NodesGroups object defined that covers all around tank and risk values are calculated in its defined nodes.

   .. code-block:: python
      
      #Define Dike Object
      opr.Safety.Dike(1,1,30**2)
      
      #Define Plant Units
      opr.PlantUnits.ONGStorage(tag=1, SiteTag=1, DikeTag=1, SubstanceTag=1, FragilityTagNumbers=[1,2], 
                                Horizontal_localPosition=0, Vertical_localPosition=0,
                                Surface_Roughness=0.0001, Pressure=1.1*10**5, Temperature=25+273,
                                SubstanceVolumeRatio=0.8, Diameter=10, Height=10, GroundTemperature=25+273,
                                radiation_probit_tag=Radiation,)
      
      #Define People Distribution for individual risk
      opr.NodesGroups.RectangNodes(1, xRefPoint=-200, yRefPoint=-200, xDim=400, yDim=400,
                                   xMesh=10, yMesh=10, PointsHeight=1, Intensity=20, pressure_probit_tag=PeopleOverP,
                                   radiation_probit_tag=PeopleRadiation, Toxic_probit_tag=None, Type='Social',)
      
Define Analysis
*******************************************************************

   By finishing the modeling, Using analysis command the number or analysis and type of analysis specified for model. In this model it is considered to do analysis for 40000 times. MultiAnalysis type considered for analysis and this type implement multiple analysis using only one cpu.
   
   .. code-block:: python
      
      #Analysis
      opr.Analyze.ScenarioAnalyze.MultiAnalysis(AnalysisNumber=40_000)
	  
	  
Post Processing and plotting individual risk
*******************************************************************

   By finishing the analysis, using the PostProcess subpackage the individual risk values at each defined nodes will be calculated. 
   
   .. code-block:: python
      
      #Post Process
	  
      #Get results using PostProcess subpackage
      results=opr.PostProcess.ObjsRecorderPP('Recorder_ex4',100)
      
      #Calculate the Average radiation and over pressure in nodegroup
      NGRadDict=results.NodesGroup_Rad_Probit_Dict()
      NGOVPDict=results.NodesGroup_OVP_Probit_Dict()
	  
      #Export and plot max(Radiation,OverPressure) average (Fast Approch with high speed convergency)--------------------------------------------
      NodeGroupTag=1
      MaxProb=[max(i,j) for i,j in zip(NGRadDict[NodeGroupTag],NGOVPDict[NodeGroupTag])]
      
      #Plot Individual risk
      opr.Plot.Plotly.PlotIndividualRisk(PlotMode=1,
          NodesGroupTag=NodeGroupTag,
          NodesProbabilityList=MaxProb,
          ContorList=[1e-8,1e-5],)
		  
      #Plot Individual risk  (With low speed convergency)
      opr.Plot.Plotly.PlotIndividualRisk(PlotMode=1,
          NodesGroupTag=1,
          NodesProbabilityList=results.NodesGroupDamageProbability()[1],
          ContorList=[1e-8,1e-5],)

	  
      
      		  
Example by: |bsz|