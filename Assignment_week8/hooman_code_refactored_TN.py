from matplotlib.widgets import Button
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

class Animation:
    """
    Animation class for the creation of a dynamic plot.

    -----------------
    Arguments:
                consuming_class (obj): instance of a consuming class
                column_number (int): used to calulate row numbers(?)

    """
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
        """
        Create subplots for the animation

        -----------------

        Returns:
                fig (Figure): Figure object
                axes (list): list with axis objects
                line (list): list with (subplot) line objects
        """
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
        """
        Initialized data_dict

        ----------------
        Returns:
                data_dict (dict): dictionary that contains x and y data keys
                                  and lists as values.
        """
        data_dict = {'xdata':[]}
        for number in range(self.consuming_class.average_number):
            data_dict[f'y{number}data'] = []
        return data_dict
    
    def animation_initializer(self):
        """
        Initializes the starting state of the animation

        ----------------
        Returns:
                line (object): 
        """
        for ax in self.axes:
            ax.set_ylim(-1., 1.1)
            ax.set_xlim(1880, 1930)
            ax.grid()
        #del self.xdata[:]
        #del self.ydata[:]
        #self.line.set_data(self.xdata, self.ydata)
        #return self.line,

    def run(self, data):
        """
        Runs animation

        --------------
        Returns:
                self.line (obj): updated plot object 
        """
        if not self.paused:
            x_axis, y_axis = data
            self.data_dict['xdata'].append(x_axis)
            for counter, y_i_data in enumerate(list(self.data_dict.values())[1:]):
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
        """
        toggles the pause state of the animation
        -------------
        """
        self.paused = not self.paused
        if self.paused:
            self.pause_button.label.set_text('Resume')
        else:
            self.pause_button.label.set_text('Pause')