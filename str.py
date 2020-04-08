import numpy as np

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.plotting import figure, output_file, show

#set up data
c= 30000000
v= 200000
m = v/c
xd = 20000
x = np.linspace(0, xd, xd)
xn = m*x
yn = x/m

#set up plots

#output_file = "plot.html"

TOOLS = "crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"

p = figure(plot_height=400, plot_width=400,
            tools=  TOOLS, title="Minkowski Doagram",
            x_axis_label="x", y_axis_label="ct")
p.line(x, xn, legend_label="x'", line_color="red", line_dash="4 4")
p.line(x, yn, legend_label="ct'",line_color="blue", line_dash="4 4")


#set up widgets
velocity = Slider(title="velocity", value=200000, start=-29999999, end=29999999, step=500)
x_ra = Slider(title="X Range", value=xd, start=100, end=100000, step = 100)


#set up call back

#set up layout
inputs = column(velocity, x_ra)

curdoc().add_root(row(inputs, p, width=800))
curdoc().title = "Interactive Minkowski Diagram"

