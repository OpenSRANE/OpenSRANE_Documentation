.. _Connectors:

Connectors Subpackage
*********************

Connectors are used to connect some models to their following models with a probability distribution. It is assumed that there more than one following event that could happen after current event, so by this type of definition user can define one or more than one following model that increase the flexibility of the program.

.. note::
   **Important Point**: Users should attention that defined tags for all objects or models of this subpackage should be unique. For example, if user defined DS_LOC connectors with tags 1 and 2 then to define Out_Physic connectors, the tags should be continued from 3.

The available commands of this subpackage are described in the following:
 

.. toctree::
   :caption: Connectors subpackage commands
   :maxdepth: 1

   Connectors-SPK/DS_LOC
   Connectors-SPK/Out_Physic
   Connectors-SPK/Pb_LOC
   