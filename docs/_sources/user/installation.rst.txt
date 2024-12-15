.. _installation:

**********************
Installation and Token
**********************

Install Python
--------------

   Install  Python from `python.org <https://www.python.org/>`_ (version: 3.9x)

Install OpenSRANE
-----------------

   OpenSRANE developed as a package on Python programming environment. it has published on PyPI and users can install this package using following command for windows:
   
   .. code-block:: python
      
      pip install OpenSRANE
   
   To upgrade:
   
   .. code-block:: python
      
      pip install OpenSRANE -U
   
   .. note::
      
      For other systems (Mac, Linux …) using corresponding commands for installing Python packages users can install the package.

Editor
----------------

   Users can use any editor for writing Python codes. However, it is highly recommended to use `Visual Studio Code <https://code.visualstudio.com/Download>`_ as the main editor of your scripts.

Import OpenSRANE
----------------
   
   By installing the package on the system, users can call it like all the other Python packages or libraries using import command:
   
   
   .. code-block:: python
      
      import opensrane as opr

Enter Your Token
----------------
   After importing the OpenSRANE, you Token (username and password) should be eneter as shown in the followin:
   
   .. code-block:: python
      
      opr.Token.userpass('username', 'password')
      
   .. note::
      
      To take username and password just send a request email to **OpenSRANE@Gmail.com** and your username and password will be sent for you. For any question or problem call Bijan SayyafZadeh: B.Sayyaf@yahoo.com, +989168046144