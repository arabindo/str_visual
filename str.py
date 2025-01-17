import numpy as np

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.plotting import figure, output_file, show

#set up data
m = 0.2
x = np.array([i for i in range(-150,150,1)])
xn = m*x
yn = x/m
dp = ColumnDataSource(data=dict(x=x, y1=xn, y2=yn))

#set up plots

#output_file = "plot.html"

TOOLS = "crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"

p = figure(plot_height=400, plot_width=400,
            tools=  TOOLS, title="Minkowski Doagram",
            x_range=[-150,150], y_range=[-150,150],
            x_axis_label="x", y_axis_label="ct")
p.line(x='x', y='y1', source=dp, legend_label="x'", line_color="red", line_dash="4 4")
p.line(x='x', y='y2', source=dp, legend_label="ct'",line_color="blue", line_dash="4 4")


#set up widgets
velocity = Slider(title="velocity(c)", value=0.2, start=-0.99, end=0.99, step=0.01)


#set up call back
def update(attrname, old, new):
    
    #get currennt values
    vy = velocity.value
    
    #generate new x' and ct'
    if vy == 0:
        yd=np.array([i*0 for i in range(-150,150,1)])
        dp.data=dict(x=x, y1=yd, y2=yd)
    else:
        m = vy
        xn = m*x
        yn = x/m
        
        dp.data=dict(x=x, y1=xn, y2= yn)
        
        
velocity.on_change('value', update)
    

#set up layout
inputs = column(velocity)

curdoc().add_root(row(inputs, p, width=800))
curdoc().title = "Interactive Minkowski Diagram"

