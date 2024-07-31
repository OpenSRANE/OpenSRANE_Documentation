#Python OpenSRANE model of Article with Title: OpenSRANE, a flexible and extensible platform for quantitative risk assessment of NaTech events 


import opensrane as opr

#Define Initial Data According data presented in the Article


Tanks_location={'TK-300':(0,0), 
                'TK-200C':(42.7,6.03), 'TK-200B':(75.25,6.03), 'TK-200A': (107.8,6.03),
                'TK-100D': (19,47.02), 'TK-100C':(49.4,47.02), 'TK-100B': (79.8,47.02), 'TK-100A': (110.2,47.02)}

Tanks_Diameter={'TK-300': 10*2,
                'TK-200C': 12.2*2, 'TK-200B': 12.2*2, 'TK-200A': 12.2*2,
                'TK-100D': 11.4*2, 'TK-100C': 11.4*2, 'TK-100B': 11.4*2, 'TK-100A': 11.4*2}

Tanks_tag={j:i+1 for i,j in enumerate(Tanks_location.keys())}

Tanks_Dike_Area={i:850 for i in Tanks_location.keys()}

Tanks_Height={i:13.5 for i in Tanks_location.keys()}

Tanks_Liquid_Level={i:12 for i in Tanks_location.keys()}

#Fragility
Tanks_D4=(-0.652,0.286) #(Median,Dispersion)
Tanks_D5=(-0.659,0.452) #(Median,Dispersion)

#Wipe the model to clear any created object if it is created before
opr.wipe()

#Define the recorder/s
opr.Recorders.Objs_recorder(tag=5, filename='Recorder', fileAppend=False)
opr.Recorders.recorder(tag=1,filename='RecorderA',fileAppend=False, recordfield='NodesGroupIsDamaged', NodesGroupTag=1)
opr.Recorders.recorder(tag=2,filename='RecorderB',fileAppend=False, recordfield='DamageLevel', NodesGroupTag=1)
opr.Recorders.recorder(tag=3,filename='RecorderC',fileAppend=False, recordfield='FragilityTag', NodesGroupTag=1)
opr.Recorders.recorder(tag=4,filename='RecorderD',fileAppend=False, recordfield='LOC', NodesGroupTag=1)
opr.Recorders.recorder(tag=6,filename='RecorderE',fileAppend=False, recordfield='HazardMag', NodesGroupTag=1)
opr.Recorders.recorder(tag=7,filename='RecorderF',fileAppend=False, recordfield='NodesRadiationOverPressure', NodesGroupTag=1)
opr.Recorders.recorder(tag=8,filename='RecorderG',fileAppend=False, recordfield='NodesRadiationProbit', NodesGroupTag=1)
opr.Recorders.recorder(tag=9,filename='RecorderH',fileAppend=False, recordfield='NodesOverPressureProbit', NodesGroupTag=1)





#Clear Warning File content
opr.Misc.warningClear()


#define Hazard Curve
PGA=[i*5/100 for i in range(1,61)]

Prob=[0.0004*i**(-1.82) for i in PGA]
Prob[-1]=0

opr.Hazard.Earthquake(1,'PGA',PGA,Prob) #Create Hazard Object with tag=1 that is 0th Object
# opr.Plot.PlotHazard()


#Define date time distribution
opr.DateAndTime.DateTime(1,Day_Night_Ratio=2)


#Define windRose
windobj=opr.WindData.WindRose(1)

windobj.WindDayClassList=['F','D','B','E','D','D']  
windobj.WindNightClassList=['F','D','B','E','D','D']

windobj.AlphaCOEFlist=[0.6,0.25,0.15,0.4,0.25,0.25]

windobj.DayWindSpeedList=[[1,2],[2,3],[3,5],[5,7],[7,9],[9]]
windobj.NightWindSpeedList=[[1,2],[2,3],[3,5],[5,7],[7,9],[9]]

windobj.DayWindFreqMatrix=[[0.446,0.372,0.355,0.109,0.017,0],
                        [0.44,0.938,1.55,0.755,0.097,0.029],
                        [0.898,1.321,3.06,1.402,0.767,0.892],
                        [0.875,1.241,2.626,1.51,0.892,0.646],
                        [0.801,0.927,1.63,0.658,0.355,0.097],
                        [0.87,1.121,0.984,0.309,0.023,0.029],
                        [0.778,0.801,0.91,0.315,0.029,0],
                        [0.652,0.875,1.35,0.498,0.086,0.023],
                        [0.566,0.887,1.659,0.709,0.149,0],
                        [0.583,0.807,2.128,2.998,1.041,0.137],
                        [0.898,1.093,2.408,2.059,1.327,0.154],
                        [1.985,2.088,2.488,1.098,0.332,0.069],
                        [4.067,3.123,1.442,0.292,0.063,0.011],
                        [3.93,5.372,3.85,1.201,0.349,0.057],
                        [1.71,1.619,2.38,0.767,0.109,0.006],
                        [0.698,0.469,0.383,0.154,0.011,0],
                          ]                                      
windobj.NightWindFreqMatrix=windobj.DayWindFreqMatrix
# opr.Plot.PlotWindRose(1)


#Define Site Condition
SiteTAg=1
obj=opr.Sites.Site(SiteTAg, Temperature=25+273, Pressure=1*10**5, g=9.81)


#Define Substances
opr.Substance.DataBank.Gasoline(1) #Use DataBank to Load Material


#Define Fragilities
D4fragtag=1
opr.Fragilities.Fragility(tag=D4fragtag,Distribution_Type='lognormal',modename=f'Tanks Fragility D4 (Sever Damage)',mean=Tanks_D4[0],StdDev=Tanks_D4[1])

D5fragtag=2
opr.Fragilities.Fragility(tag=D5fragtag,Distribution_Type='lognormal',modename=f'Tanks Fragility D5 (Collapse)',mean=Tanks_D5[0],StdDev=Tanks_D5[1])




#Define Probits (Because Fragility and Probit are in same subpackage so the tag should be continued)
TankHeatProbittag=3
opr.Fragilities.Probit(tag=TankHeatProbittag, Distribution_Type='normal', K1=1/5000, K2=5-25000/5000)

TankOVPProbittag=4
opr.Fragilities.Probit(tag=TankOVPProbittag, Distribution_Type='normal', K1=1/5000, K2=5-45000/5000)

HumanRadiation=5
opr.Fragilities.Probit(tag=HumanRadiation, Distribution_Type='normal', K1=1/4000, K2=5-14500/4000,MinRndVar=2500)

HumanOVP=6
opr.Fragilities.Probit(tag=HumanOVP, Distribution_Type='normal', K1=1/3000, K2=5-20000/3000,MinRndVar=5000)

#Define Outflow Models
opr.OutFlowModel.SimultaniousLiquid(tag=1, Release_Ratio=1)
opr.OutFlowModel.SimultaniousLiquid(tag=2, Release_Ratio=0.8)
opr.OutFlowModel.NoOutFlow(tag=3)


#Define the DS_LOC for each Fragility
ConnectorTag=0

ConnectorTag +=1
opr.Connectors.DS_LOC(tag=ConnectorTag, FragilityTag=D4fragtag, OutFlowModelTagList=[1,2], LOCProbabilityList=[1,1])
ConnectorTag +=1
opr.Connectors.DS_LOC(tag=ConnectorTag, FragilityTag=D5fragtag, OutFlowModelTagList=[1], LOCProbabilityList=[1])


#Define Probit - LOC loss of containment Connectors
ConnectorTag +=1
opr.Connectors.Pb_LOC(tag=ConnectorTag, ProbitTag=TankHeatProbittag, OutFlowModelTagList=[1,2,3], LOCProbabilityList=[50,30,20])
ConnectorTag +=1
opr.Connectors.Pb_LOC(tag=ConnectorTag, ProbitTag=TankOVPProbittag, OutFlowModelTagList=[1,2,3], LOCProbabilityList=[50,30,20])


#Define Dispesion Spread Models and their connections to the materials and outflows
opr.DispersionSpreadModels.LqdSprdGaussianGasDisp(tag=1, MatTags=[1], OutFlowModelTags=[1,2], MinDisThickness=0.01, Surface_Roughnesslist=[0.0001, 0.0002], 
                                                  Surface_RoughnessThickness=[0.005, 0.01], Vaporization_Delta_t=10, TotalDuration=1800,
                                                  GasConstant=8.31446261815324, GasDispersionXSegments=10, GasDisperstionErrorPercent=1,)


#Define Physical Effect models
opr.PhysicalEffect.Simple_fire_point_source(tag=1, minf=0.055, k=1.5)
opr.PhysicalEffect.VCE_TNT(tag=2)
opr.PhysicalEffect.SAFE(tag=3)


#Define OutFlow-Phisycal Effect connection
ConnectorTag +=1
opr.Connectors.Out_Physic(tag=ConnectorTag, OutFlowTag=1, MaterialsTagList=[1], 
                          PhysicalEffectTagList=[1,2,3], PhysProbabilityList=[55.48,35.7,8.82])
ConnectorTag +=1
opr.Connectors.Out_Physic(tag=ConnectorTag, OutFlowTag=2, MaterialsTagList=[1], 
                          PhysicalEffectTagList=[1,2,3], PhysProbabilityList=[55.48,35.7,8.82])
ConnectorTag +=1
opr.Connectors.Out_Physic(tag=ConnectorTag, OutFlowTag=3, MaterialsTagList=[1], 
                          PhysicalEffectTagList=[1,2,3], PhysProbabilityList=[55.48,35.7,8.82])


#Define Dike for Tanks (Dike hight considered equal to the tank height to ensure that it's capacity is more than tank containment)
for TankName,area in Tanks_Dike_Area.items():
    
    D=Tanks_Diameter[TankName]
    h=Tanks_Liquid_Level[TankName]
    v=3.1415*D**2/4*h
    hd=v/area #Dike height considered coresponding required hight to store tank capacity
    opr.Safety.Dike(Tanks_tag[TankName], Height=hd, Area=area)

    
#Define Plant Units
for TankName,Location in Tanks_location.items():
    opr.PlantUnits.ONGStorage(tag=Tanks_tag[TankName], SiteTag=1, DikeTag=Tanks_tag[TankName],
                              SubstanceTag=1, FragilityTagNumbers=[D4fragtag,D5fragtag],
                              Horizontal_localPosition=Location[0], Vertical_localPosition=Location[1],
                              Pressure=1.00001*10**5, Temperature=25+273,
                              SubstanceVolumeRatio=Tanks_Liquid_Level[TankName]/Tanks_Height[TankName],
                              Diameter=Tanks_Diameter[TankName], Height=Tanks_Height[TankName],
                              boundary_points_Number=20,   boundary_points_height_levels=10,
                              pressure_probit_tag=TankOVPProbittag,  radiation_probit_tag=TankHeatProbittag,)

#Define Vulnerable Area
opr.NodesGroups.RectangNodes(tag=1, 
                             xRefPoint=-300, yRefPoint=-300, xDim=700, yDim=700, xMesh=40, yMesh=40,
                             PointsHeight=1.8, Intensity=1, 
                             pressure_probit_tag=HumanOVP, radiation_probit_tag=HumanRadiation, Toxic_probit_tag=None,
                             Type='Social',)

#Plot Model
# opr.Plot.Plotly.PlotUnits2D()


#Analyze
import time
if __name__=='__main__':
    t0=time.time()
    print('start time is=',t0)
    opr.Analyze.ScenarioAnalyze.MultiParallel(AnalysisNumber=1_000_000, NumberOfProcessors=15,RecordersSaveStep=5000)
    print('Time consumed for this analysis is=', time.time()-t0)
    # opr.Analyze.ScenarioAnalyze.UniAnalyze()
    # for i in range(3):
    #     opr.Analyze.ScenarioAnalyze.MultiAnalysis(100)


