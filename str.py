import numpy as np

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.plotting import figure, output_file, show

#set up data
c= 30000000
v= 200000
m = v/c
x = np.linspace(0, 100, 1000)
xn = m*x
yn = x/m

#set up plots
output_file = "plot.html"
TOOLS = "crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
p = figure(plot_height=400, plot_width=400,
            tools=  TOOLS, title="Minkowski Doagram",
            x_axis_label="x", y_axis_label="ct")
p.line(x, xn, legend_label="x'", line_color="red", line_dash="4 4")
p.line(x, yn, legend_label="ct'",line_color="red", line_dash="4 4")
show(p)

#set up widgets


#set up call back

#set up layout

