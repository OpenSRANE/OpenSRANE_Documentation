.. _ProbitVF:

*************************************
Probit Module Verification 
*************************************

The question is that **Does the GetProbability method of Probit object correctly samples the defined distribution?**. To find the answer of this question, first a Probit object will be created. Then a range of manitude will be define and for each magnitude the result of the GetProbability method will be record and recorded results will be check by results of data created using Excel.

The below codes can be downloaded from :download:`here <files/Probit.ipynb>` in Jupyter Notebook format. Also the Excel file that results are checked with, can be downloaded from :download:`here <files/Probit.xlsx>`.

.. admonition:: Verification1 for Normal Distribution:  

   .. code-block:: python
      
      #Import the software
      import opensrane as opr
      
      #Import Matplotlib package for plot purposes
      import matplotlib.pyplot as plt 
      
      #Verification for normal distribution
      opr.wipe()
      
      obj=opr.Fragilities.Probit(1,Distribution_Type='normal', K1=1, K2=0.5)
      #Excel results for mean=4.5 and std=1
      Excel=[3.39767312473005E-06,3.16712418331199E-05,0.000232629079035525,0.00134989803163009,0.00620966532577613,0.0227501319481792,0.0668072012688581,0.158655253931457,0.308537538725987,0.5,0.691462461274013,0.841344746068543,0.933192798731142,0.977249868051821,0.993790334674224,0.99865010196837,0.999767370920964,0.999968328758167,0.999996602326875,0.999999713348428,0.999999981010438,0.999999999013412,0.99999999995984]
      
      #Excel range of the Random Variable
      Dose=[i/2 for i in range(23)]
      
      #List of generated values by Created Object (obj)
      Generated=[obj.GetProbability(i) for i in Dose]
      
      
      plt.figure()
      plt.plot(Dose,Excel,label='Excel')
      plt.plot(Dose,Generated,label='Generated')
      plt.legend()
      plt.xlabel('Dose')
      plt.ylabel('Probability')
      plt.title(f'CDF Distribution for distribution={obj.DistType} mean={obj.mean} and std={obj.StdDev}',color='g')
      plt.show()


   The result of above code has been shown on the following image:

   .. _Prob1VF:

   .. figure:: files/Probit.png
   	 :align: center
   	 :figclass: align-center
      
   	 Comparision of results and defined curve in Excel	  
	 
	 
.. admonition:: Verification2 for LogNormal Distribution:  

   .. code-block:: python
      
      #Import the software
      import opensrane as opr
      
      #Import Matplotlib package for plot purposes
      import matplotlib.pyplot as plt 
	  
      #Verification for log normal distribution
      opr.wipe()
      
      obj=opr.Fragilities.Probit(1,Distribution_Type='lognormal', K1=1, K2=0.5)
      #Excel results for mean=4.5 and std=1
      Excel=[4.30656462230891E-20,0.0139954138003093,0.0662562227267046,0.135927084948079,0.208648223994374,0.278273867277455,0.342497894582516,0.400711942041258,0.453044380936582,0.499924069447986,0.541879616184157,0.579447543942368,0.613132088240471,0.643389800296413,0.670626009729306,0.695196771402629,0.717413125048509,0.737546096844058,0.755831684715014,0.772475484841812,0.787656828725862,0.801532406011979,0.8142393985932,0.8258981728861,0.836614583647308,0.846481941822576,0.855582694679972,0.863989860981988,0.871768258271563,0.878975554000964,0.885663167438306,0.891877045105856,0.897658328920541,0.903043933167712,0.908067043878904,0.912757552036115,0.917142430226971,0.921246060871349,0.925090522882637,0.928695842574893,0.932080213746174,0.935260191129611,0.938250860783288,0.941065990467936,0.943718162621335,0.946218892166573,0.948578731076635,0.950807361350948,0.952913677832627,0.954905862101998,0.956791448517015]
      
      #Excel range of the Random Variable
      Dose=[0.01]+[i*10 for i in range(1,51)]
      
      #List of generated values by Created Object (obj)
      Generated=[obj.GetProbability(i) for i in Dose]
      
      
      plt.figure()
      plt.plot(Dose,Excel,label='Excel')
      plt.plot(Dose,Generated,label='Generated')
      plt.legend()
      plt.xlabel('Dose')
      plt.ylabel('Probability')
      plt.title(f'CDF Dist-Type={obj.DistType} mean={obj.mean} and std={obj.StdDev}',color='g')
      plt.show()


   The result of above code has been shown on the following image:

   .. _Prob2VF:

   .. figure:: files/ProbitLog.png
   	 :align: center
   	 :figclass: align-center
      
   	 Comparision of results and defined curve in Excel		
	 
Verification by: |bsz|