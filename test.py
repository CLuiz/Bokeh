from bokeh.plotting import figure, output_file, show

output_file('test.html')
x = range(1,6)
y = [10,5,7,1,6]

plot = figure(title='Line example', x_axis_label='x')
plot = figure(title='Line example', x_axis_label='x', y_axis_label='y')
plot.line(x,y,legend='Test', line_width=4)

show(plot)
