#Description code TN:
# This code contains a Animation class
# its purpose is create an Animation in Matplotlib, it fetches x and y data and stores
# it in self.data -> a dictionary with x_data and multiple y_data keys and lists as values.  
# The animation initializer seems to initialize the 'starting' state
# of the animation. The run method receives data (x, y) for updating the data but returns the self.line when
# self.pause is active/True. 
#There are print statements added for debugging, as well as some functions commented out. 


## Overall comments TN:
# Class takes care of more than just updating the plot, it also initializes data,
# creates and controls the widget and distributes to the consumers?
# In the end this creates a bloated __init__.

# I had the same observations 😎🤔

# The lack of comments and descriptions makes it hard to understand what is going on

# The use that the pause status will be checked could prove problematic if it breaks
# the code would keep on running if it has not the status False. Wouldn't it be better
# to flip the logic and check whether the Animation is active? self.active or something?

# There are a lot of FOR ax in axes: but I can only see the creation of one axis. 
# Isn't the line the thing you want to add to the axes?

from matplotlib.widgets import Button
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

class Animation(): # () is not necessary if the class has no super
    def __init__(self, consuming_class, column_number):
        self.consuming_class = consuming_class
        self.column_number = column_number
        self.fig, self.axes, self.line = self.subplot_maker()
        self.data_dict = self.data_initializer()
        # repeat does not work
        self.ani = animation.FuncAnimation(self.fig, self.run,
                                           self.consuming_class.temp_average_maker,
                                           init_func=self.animation_initializer,
                                           interval=200, repeat=False, repeat_delay=1000)

        self.paused = False
        self.pause_button_ax = plt.axes([0.8, 0.9, 0.1, 0.05])
        self.pause_button = Button(self.pause_button_ax, 'Pause')
        self.pause_button.on_clicked(self.toggle_pause)
        plt.show()

    def subplot_maker(self):
        # How does average number relate to plot_numbers?
        plot_numbers = self.consuming_class.average_number
        row_numbers = math.ceil(plot_numbers / self.column_number) # unused? 
        fig, axes = plt.subplots(1,1)
        for counter, ax in enumerate(axes):
            # but axes is always exactly one right?
            if counter >= plot_numbers:
                ax.remove()
        line = []
        for ax in axes:
            sub_line, = ax.plot([], [], lw=2)
            line.append(sub_line)
        return fig, axes, line

    def data_initializer(self):
        data_dict = {}
        data_dict['xdata'] = [] # could be one line
        for number in range(self.consuming_class.average_number):
            data_dict[f'y{number}data'] = []
        return data_dict
    
    def animation_initializer(self):
        for ax in self.axes:
            ax.set_ylim(-1., 1.1)
            ax.set_xlim(1880, 1930)
            ax.grid()
        #del self.xdata[:]
        #del self.ydata[:]
        #self.line.set_data(self.xdata, self.ydata)
        #return self.line,

    def run(self, data):
        ## Comments TN: 
        # Double return, one could be sufficient, e.g. IF NOT self.paused: the function.
        if self.paused:
            return self.line,  # Return the line without updating the data
        x_axis, y_axis = data
        self.data_dict['xdata'].append(x_axis)
        for counter, y_i_data in enumerate(list(self.data_dict.values())[1:]):
            # This one is difficult to comprehend but I guess it works.
            y_i_data.append(y_axis[counter])
        for ax in self.axes:
            xmin, xmax = ax.get_xlim()
            if x_axis >= xmax:
                ax.set_xlim(xmin, xmax + 50)
                ax.figure.canvas.draw()
        print(self.line)
        for counter, line_i in enumerate(self.line):
            print(counter, line_i)
            line_i.set_data(self.data_dict['xdata'], self.data_dict[f'y{counter}data'])
        return self.line

    def toggle_pause(self, *args, **kwargs):
        self.paused = not self.paused
        if self.paused:
            self.pause_button.label.set_text('Resume')
        else:
            self.pause_button.label.set_text('Pause')