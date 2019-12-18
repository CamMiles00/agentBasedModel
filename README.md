Agent Based Model
=======

The files in this repository form an Agent based model, the output of practical work for module GEOG5990M. The model siumaltes the movement of sheep through an environment. Their initial start point is random and so is their movement.

It is possible to adjust the number of sheep and the number of days the model simulates using the numOfAgents and numOfIterations variables. The default values are 25 sheep and 150 days.

The model uses an agent class that includes several functions that the sheep follow. These include:

The model runs through a GUI using the tkinter module. The user can run the model and exit the model using the options tab in the model window.

Files indluded in model
-------
* modelFramework
* agentFramework
* in.txt

modelFramework
-------
The main code of the model, this includes the functions of the model such as the creations and location of the agents as well as the GUI setup. This is the main run file of the model.

agentFramework
-------
This file contains the agent class and all of the actions that the agents go through for each iteration of the model. These include:

* random movement
* eating from the environment
* sharing food between sheep who are located close to on another
* random chance of disease 
* the spread of disease between nearby sheep
* starvation if disease persists

in.txt
-------
This is a text file that contains the environment data that the sheep move across and consume.
