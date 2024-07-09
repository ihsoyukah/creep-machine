import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# create figures
fig = plt.figure()
line, = plt.plot([], [])  # Create an empty line object

# you choose the limits of your plot
def init_strain():
    plt.xlim(0, 10)
    plt.ylim(0, 4)
    return line,

def update_strain(frame):
    x = np.linspace(0, frame/5, 100) #frame / number lets you decide how fast to animate
    y = np.sqrt(x)
    line.set_data(x, y)  # Update the data of the line object
    return line,

plt.xlabel('Time [units]')
plt.ylabel('Strain [units]')
plt.title('Strain vs Time')

# animation object
strain_ani = FuncAnimation(fig, update_strain, frames=range(1, 100), init_func=init_strain, blit=True)

# save a gif (wont run on spyder??)
strain_ani.save('Strain.gif', writer='pillow')

