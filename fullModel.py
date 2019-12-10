import matplotlib
import matplotlib.pyplot
import matplotlib.animation
import agentFramework as afw
import csv
import tkinter
from tkinter import Tk, Frame, Menu
matplotlib.use('TkAgg')

environment = []
dataset = open('in.txt')
reader = csv.reader(dataset)
for line in dataset:
    parsed_line = str.split(line, ',')
    rowlist = []
    for value in parsed_line: 
        rowlist.append(float(value))
    environment.append(rowlist)

    
num_of_agents = 25
num_of_iterations = 150
neighbourhood = 20
infect = 10
agents = []

matplotlib.pyplot.imshow(environment)

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

ax.set_autoscale_on(False)

#Make the agents
for i in range(num_of_agents):
    agents.append(afw.Agent(environment, agents))

    
carry_on = True

def update(frame_number):
    fig.clear()
    global carry_on
# Move the agents loop
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        agents[i].disease(infect)
        if agents[i].infection==0:
            matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'white')
        else:
            matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'red')
        matplotlib.pyplot.xlim(0, len(environment))
        matplotlib.pyplot.ylim(0, len(environment))
        matplotlib.pyplot.imshow(environment)
    #for i in range(num_of_agents):
        #matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'white')
    #if random.random() < 0.1:
        #carry_on = False
        #print("stopping condition")
            
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    #canvas.show()
    canvas.draw()
    pass

"""
root = tkinter.Tk() 
root.title('Agent Based Model')
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Options", menu=model_menu)
model_menu.add_command(label="Run model", command=run)  
model_menu.add_command(label="Set Parameters", command=run)
model_menu.add_command(label="Exit", command=root.quit)  
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
tkinter.mainloop()
"""