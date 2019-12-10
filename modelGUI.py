import fullModel

root = tkinter.Tk() 
root.title('Agent Based Model')
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Options", menu=model_menu)
model_menu.add_command(label="Run model", command=run)  
#model_menu.add_command(label="Set Parameters", command=run)
#model_menu.add_command(label="Exit", command=root.quit)  
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
tkinter.mainloop()