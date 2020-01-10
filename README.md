Agent Based Model - Last Sheep Standing
=======

The files in this repository form an Agent based model, the output of practical work for module GEOG5990M. The model simulates the movement of agents (sheep) through an environment. Their initial start point and direction of movement is randomly generated. Whilst moving about the environment they have a small chance of contracting a deadly disease. Once they are infected it is only a matter of time before they die. All the sheep start as white dots moving around the landscape and turn red when they become infected eventually becoming a black x when they die.

It is possible to adjust the number of sheep and the number of days the model simulates using the numOfAgents and numOfIterations variables. The default values are 25 sheep and 50 days.

The model uses an agent class found within the agentFramework that includes several functions that the sheep follow. The model runs through a GUI using the tkinter module. The user can run the model and exit the model using the options tab in the model window.

![](Model_GUI.PNG)

Model Files Location
------
The following links take you to the raw code required for the model:

* [modelFramework](https://raw.githubusercontent.com/CamMiles00/agentBasedModel/master/modelFramework.py)
* [agentFramework](https://raw.githubusercontent.com/CamMiles00/agentBasedModel/master/agentFramework.py)
* [Enironment Data](https://raw.githubusercontent.com/CamMiles00/agentBasedModel/master/in.txt)

The files can also be downloaded from GitHub [here](https://github.com/CamMiles00/agentBasedModel)

Description of files included in model
=======

modelFramework
-------
The main code of the model, this includes the functions of the model such as the creation and location of the agents as well as the GUI setup. This is the main run file of the model.

agentFramework
-------
This file contains the agent class and all of the actions that the agents go through for each iteration of the model. These include:

* random movement
* eating from the environment
* sharing food between sheep who are located close to on another
* greedy sheep who eat too much have to start again from zero food
* random chance of disease 
* starvation if disease persists

in.txt
-------
This is a text file that contains the environmental data over which the sheep move and consume food.

**References**

Website theme used: Jekyll Tactile theme
