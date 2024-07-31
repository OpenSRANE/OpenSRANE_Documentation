.. _sphericaltank:

SphericalTank Command
*********************

.. function:: PlantUnits.SphericalTank(tag,SiteTag=None,DikeTag=None, SafetyTag=None, SubstanceTag=None, FragilityTagNumbers=None, Horizontal_localPosition=0,Vertical_localPosition=0, Surface_Roughness=None, Pressure=0,Temperature=0, SubstanceVolumeRatio=None, Diameter=None,Botton_Point_Height=None, GroundTemperature=None,Ks_Soil_Thermal_conductivity=None,Alphas_Soil_thermal_diffusivity=None, boundary_points_Number=20,Number_of_boundary_points_height_levels=10, pressure_probit_tag=None, radiation_probit_tag=None, RadiationDifferenceDose=1000)
   
   Above Ground Spherical tank object is defined by this command. Defined features also should be assigned by their tags to this/these object/s.

   .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40
	  
      Tag, int, Unique integer value that will be used for referring to the defined elements or objects.
	  SiteTag, int, Tag of the site.
	  DikeTag, int, Tag of the dike that surrounded the tank. There is no need to define if the tank is not surrounded by any dike.
	  SubstanceTag, int, Tag of the tank content substance or material.
	  FragilityTagNumbers, list of int, List of the tank fragilities tag.
	  Horizontal_localPosition, float, "Horizontal location of the tank respect to the local reference point (0,0)."
	  Vertical_localPosition, float, "Vertical location of the tank respect to the local reference point (0,0)."
	  Surface_Roughness, float, Value of the surface roughness. This value will be used for liquid dispersion models.
	  Pressure, float, Internal pressure value of the tank.
	  Temperature, float, Internal temperature value of the tank.
	  SubstanceVolumeRatio, float, Ratio of the tank content to the total volume of the tank.
	  Diameter, float, Spherical Tank diameter.
	  Botton_Point_Height, float, Height of the most bottom point of spherical tank from ground.
	  GroundTemperature, float, "Temperature of the ground around the tank that will be used for liquids vaporization. If user do not enter any value, it will be considered equal to site temperature."
	  Ks_Soil_Thermal_conductivity, float, "Soil thermal conductivity or Ks that will be used for liquid vaporization calculation. If user do not enter any value, it will be considered equal to 0.9."
	  Alphas_Soil_thermal_diffusivity, float, "Soil thermal diffusivity that will be used for liquid dispersion and If user do not enter any value, it will be considered equal to 4.3×10^(-7)."
	  boundary_points_Number, int, Number of the boundary points that program uses them to calculate the pressure and temperature at these points at each specified level of height.
	  Number_of_boundary_points_height_levels, int, "Number of the levels that boundary points will be repeated in the height of the spherical tank. If boundary points defined equal to 20 and heigh points level defined equal to 10, there will be 200 points on the tank body that temperatures and pressures will be calculated for."
	  pressure_probit_tag, int, Tag of the defined probit object to be use for vulnerability under pressure loads.
	  radiation_probit_tag, int, Tag of the defined probit object to be use for vulnerability under temperature loads.
	  RadiationDifferenceDose, float, "A thermal radiation dose if the increase of radiation become more than this value, code will check the vulnerability of the object using the new thermal radiation dose and defined probit function. In any level it may new units suffer damage and create thermal radiation dose for all other not damaged units, but for far units these doses are less and program shouldn’t recheck the thermal vulnerability. So, if the increase of the radiation becomes more than RadiationDifferenceDose the code assume that a high new radiation happened and checks the vulnerability of unit under the new total dose."

   .. note::
   
      The default values are shown in the command structure. 

   .. admonition:: Example:
   
      As said, defining all above parameters while defining the wind rose object is tough and author suggests that define step by step as shown in the following. The below values are according to the example of chapter 7 of Casal book [Ref.1]_ :
   
      **Python Code**
   
      .. code-block:: python
      
        import opensrane as opr
		
        opr.PlantUnits.SphericalTank(1,SiteTag=SiteTAg, DikeTag=2, Horizontal_localPosition=10, Vertical_localPosition=15, Pressure=2*10**5, Temperature=273+3, SubstanceTag=1, FragilityTagNumbers=[1,2,4,6], radiation_probit_tag=2, pressure_probit_tag=4, Diameter=10, Botton_Point_Height=5, SubstanceVolumeRatio=0.85)

   

Code Developed by: |bsz|