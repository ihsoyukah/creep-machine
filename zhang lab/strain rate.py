import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# create figures
strain_rate_fig = plt.figure()
line, = plt.plot([], [])  # Create an empty line object

# you choose the limits of your plot
def init_strain_rate():
    plt.xlim(0, 10)
    plt.ylim(0, 1)  # Adjusted ylim to match the range of the derivative of sqrt(x)
    return line,

def update_strain_rate(frame):
    x = np.linspace(0, frame/5, 100)
    y = np.sqrt(x)
    dy_dx = np.gradient(y, x)  # Calculate the derivative using np.gradient
    line.set_data(x, dy_dx)  # Update the data of the line object with the derivative
    return line,

plt.xlabel('Time [units]')
plt.ylabel('Strain Rate [units]')
plt.title('Strain Rate vs Time')

# animation object
strain_rate_ani = FuncAnimation(strain_rate_fig, update_strain_rate, frames=range(1, 100), init_func=init_strain_rate, blit=True)

# save a gif (wont run on tk??)
strain_rate_ani.save('Strain.gif', writer='pillow')