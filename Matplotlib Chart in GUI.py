from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Matplotlib GUI")
root.geometry("400x400")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50) #plot info from house_prices on a histogram    
    plt.show()


graph_button = Button(root, text = "Create Graph", command = graph)
graph_button.pack()

root.mainloop()


