import matplotlib
import matplotlib.pyplot
import matplotlib.animation
import agentFramework as afw
import csv
import tkinter
from tkinter import * 
matplotlib.use('TkAgg')

#Read and plot environment data
environment = []
dataset = open('in.txt')
reader = csv.reader(dataset)
for line in dataset:
    parsed_line = str.split(line, ',')
    rowlist = []
    for value in parsed_line: 
        rowlist.append(float(value))
    environment.append(rowlist)
matplotlib.pyplot.imshow(environment)
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_autoscale_on(False)

#Set model parameters   
numOfAgents = 25
numOfIterations = 150
neighbourhood = 20
infectDist = 10

#Create the agents
agents = []
for i in range(numOfAgents):
    agents.append(afw.Agent(environment, agents))

carry_on = True

def update(frame_number):
    fig.clear()
    global carry_on
    
#Agent movement loop
    for i in range(numOfAgents):
        if agents[i].starvation == 0:
            agents[i].move()
            agents[i].eat()
            agents[i].shareWithNeighbours(neighbourhood)
            agents[i].disease(infectDist)
            if agents[i].infection == 0:
                matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'white')
            else:
                matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'red')
        else:
            matplotlib.pyplot.scatter(agents[i].x,agents[i].y, marker = 'x', color = 'black')
        matplotlib.pyplot.xlim(0, len(environment))
        matplotlib.pyplot.ylim(0, len(environment))
        matplotlib.pyplot.imshow(environment)
    #if random.random() < 0.1:
        #carry_on = False
        #print("stopping condition")

#Animate model            
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < numOfIterations) & (carry_on) :
        yield a			
        a += 1
        
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
    pass

#GUI setup
root = tkinter.Tk() 
root.title('Agent Based Model')
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label = "Options", menu=model_menu)
model_menu.add_command(label = "Run model", command=run)  
model_menu.add_command(label = "Exit Model", command = root.destroy)
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
tkinter.mainloop()
