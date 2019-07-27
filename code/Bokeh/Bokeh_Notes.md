# Bokeh Notes

<!-- TOC -->

- [Bokeh Notes](#bokeh-notes)
  - [What is it?](#what-is-it)
  - [Installation](#installation)
  - [Getting started](#getting-started)
    - [Simple example](#simple-example)
    - [Bar graph with ``pandas``](#bar-graph-with-pandas)
  - [Advanced settings](#advanced-settings)
    - [Tweaking plot tools](#tweaking-plot-tools)
    - [Using column data](#using-column-data)
    - [Save command](#save-command)
    - [Tool tips](#tool-tips)
    - [Colour maps](#colour-maps)
    - [Legend for Plots](#legend-for-plots)
    - [Components](#components)
  - [Full program with all advanced details](#full-program-with-all-advanced-details)
  - [Output of the final program](#output-of-the-final-program)

<!-- /TOC -->

## What is it?

Bokeh is a python library useful for plotting and data visualisation. Unlike other libraries, bokeh creates the plot in a webpage. So, one of the main advantages of bokeh is that you can make plots that can be displayed on a website. This tutorial is taken from [Brad Traversy video on bokeh][1] from YouTube.

## Installation

Installing bokeh is quite easy. All you need is the ``pip`` installer of python.

```bash
pip install bokeh
```

## Getting started

### Simple example

```python
# Import figure - to create a figure object
# Import output_file - to create a html file
# Import show - to render the plot
from bokeh.plotting import figure, output_file, show

# Import numpy for creating data sets
import numpy as np

# Create a dataset for plot
x = np.linspace(0, 2.0*np.pi, 201)
y = 3.0*np.sin(x) + 4

# Create an output html to render the plot.
output_file("Figure_sample1.html")

# Make a figure object
plot = figure(
	title="Sine curve",
    x_axis_label="Angle in Radian",
    y_axis_label="Magnitude",
)

# Render the plot
plot.line(x, y, legend='Sine Curve', line_width=2)

# Show results
show(plot)
```

### Bar graph with ``pandas``

In this example, we’ll use pandas to extract data from ``csv`` files and make a bar chart. The ``csv`` file is called ``cars.csv`` and the data in it is this:

```csv
Car,Horsepower,Price,Image
Hennessey Venom F5,1600,$1.6M,https://autowise.com/wp-content/uploads/2018/06/Hennessey-Venom-F5-15.jpg
Koenigsegg Regera,1500,$2M,https://autowise.com/wp-content/uploads/2018/06/Regera_front_banner2.jpg
Bugatti Chiron,1479, $3.4M,https://autowise.com/wp-content/uploads/2018/06/chiron-768x320.webp
NIO EP9,1341,1.48M,https://autowise.com/wp-content/uploads/2018/06/nio-ep9-1.webp
Rimac Concept One,1224,$1M,https://autowise.com/wp-content/uploads/2018/06/rimac.webp
Aston Martin Valkyrie,1130,$3.2M,https://autowise.com/wp-content/uploads/2018/06/aston-martin-valkyrie-9-720x720.webp
McLaren P1 LM,986,$3.7M,https://autowise.com/wp-content/uploads/2018/06/lanzante-p1-gtr-mclaren-2017-4.webp
Ferrari LaFerrari,950,$1M,https://autowise.com/wp-content/uploads/2018/06/Ferrari-LaFerrari-three-quarter-1260x570.webp
```

Let’s open this file and plot it.

```python
# Import figure - to create a figure object
# Import output_file - to create a html file
# Import show - to render the plot
from bokeh.plotting import figure, output_file, show

# Import numpy and pandas for creating data sets
import numpy as np
import pandas as pd

# Read in CSV
df = pd.read_csv('cars.csv')
car = df['Car']
hp = df['Horsepower']
price = df['Price']

# Create an output html to render the plot.
output_file("Figure_sample2.html")

# Make a figure object
plot = figure(
	title="Price of Cars with Horsepower",
    y_range=car,
    plot_width=800,
    plot_height=600,
    x_axis_label="Horse power",
    y_axis_label="Car name",
    tools="" # this will remove all accessory features in the tool
)

# Render the plot
plot.hbar(y=car, right=hp, left=0, height=0.4, color='orange', fill_alpha=0.5)

# Show results
show(plot)
```

## Advanced settings

### Tweaking plot tools

If you want only some tools in the graph, you can tweak them in the tools option.

```python
plot = figure(
    tools="pan,box_select,zoom_in,zoom_out,save,reset"
)
```

### Using column data

``Column Data`` is a method that converts data into column format. Once data is converted into this format, you can directly use it in the figure object with minor tweaks. This is quite useful to pass data to tool-tips.

```python
from bokeh.plotting import ColumnDataSource
source = ColumnDataSource(df)

car_list = source.data['Car'].tolist() 
# this is needed as y_range in figure accepts list or arrays.
# Make a figure object
plot = figure(
	title="Price of Cars with Horsepower",
    y_range=car_list,
    plot_width=800,
    plot_height=600,
    x_axis_label="Horse power",
    y_axis_label="Car name",
)

# note that instead of the variable "car", now you are using the column 'Car' from 
# the variable "source". Same with 'Horsepower'
plot.hbar(y='Car', right='Horsepower', left=0, height=0.4, 
          color='orange', fill_alpha=0.5, source=source)
# For comparison, this is the old line
# plot.hbar(y=car, right=hp, left=0, height=0.4, color='orange', fill_alpha=0.5)
```

### Save command

This command is used to save the data to the same ``html`` file. This way, the output instead of displaying on the screen will store in the ``html`` file. And if the ``html`` file is in a live server, the page will be instantly updated.

```python
from bokeh.plotting import save
# This command will save the data to the html file.
save(plot)
```

### Tool tips

This feature uses the column data source values to make content appear on the graph when the mouse cursor moves over.

```python
from bokeh.models.tools import HoverTool
hover = HoverTool()
hover.tooltips = """
<div>
	<h3>@Car</h3>
	<div><strong>Price:</strong>@Price</div>
	<div><strong>Horse Power:</strong>@Horsepower</div>
	<div><img src="@Image" alt="" width="200"/></div>
</div>
"""

plot.add_tools(hover)
```

Alternatively, you can tweak the same tool tip as

```python
hover.tooltips = [
    ("Car", "@Car"),
    ("HP", "@Horsepower"),
    ("Price", "@Price"), 
    ("Image", "<div><img src=\"@Image\" alt=\"\" width=\"200\"/></div>"),
]
```

For more tool-tips and plot tools, you can refer to [bokeh plot tools page][3]

### Colour maps

You can introduce colour maps/palettes in your file too. For more colour palettes, you can refer to [bokeh colour palettes page][4]

```python
# This is used to implement colourmaps based on certain factors.
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8 # A sample blue palette

plot.hbar(y='Car', right='Horsepower', left=0, height=0.4, 
          fill_color=factor_cmap('Car', palette=Blues8, factors=car_list), 
          fill_alpha=0.5, source=source)
```

### Legend for Plots

To add legend, there is a legend method. 

* First, you need to specify the legend details.

```python
plot.legend.orientation = "vertical"
plot.legend.location = "top_right"
plot.legend.label_text_font_size = "10px"
```

* Second, you need to specify the legend in the ``plot`` command.

```python
plot.hbar(y='Car', right='Horsepower', left=0, height=0.4, 
          fill_color=factor_cmap('Car', palette=Blues8, factors=car_list), 
          fill_alpha=0.5, source=source, legend='Car')
```

### Components

This is useful to extract the ``script`` and ``div`` components from the ``html`` file. With these data stored in variables, you can use them to export/embed the values into other files.

```python
# This is used to extract script and div components
from bokeh.embed import components

# Extract components
script, div = components(plot)
print(script)
print(div)
```

## Full program with all advanced details

```python
# Import figure - to create a figure object
# Import output_file - to create a html file
# Import show - to render the plot
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
# This is used to implement colourmaps based on certain factors.
from bokeh.transform import factor_cmap
#  A sample blue palette
from bokeh.palettes import Blues8
# This is used to extract script and div components
from bokeh.embed import components

# Import numpy and pandas for creating data sets
import numpy as np
import pandas as pd

# Read in CSV
df = pd.read_csv('cars.csv')
source = ColumnDataSource(df)

car_list = source.data['Car'].tolist()
# this is needed as y_range in figure accepts list or arrays.
# Make a figure object
plot = figure(
	title="Price of Cars with Horsepower",
	y_range=car_list,
	plot_width=800,
	plot_height=600,
	x_axis_label="Horse power",
	y_axis_label="Car name",
)

# Create an output html to render the plot.
output_file("Figure_sample2.html")

# note that instead of the variable "car", now you are using the column 'Car' from
# the variable "source". Same with 'Horsepower'
plot.hbar(y='Car', right='Horsepower', left=0, height=0.4,
			fill_color=factor_cmap('Car', palette=Blues8, factors=car_list),
			fill_alpha=0.9, source=source, legend='Car')
# For comparison, this is the old line
# plot.hbar(y=car, right=hp, left=0, height=0.4, color='orange', fill_alpha=0.5)

# Add hover details to the tool-tip
hover = HoverTool()
hover.tooltips = [
	("Car", "@Car"),
	("HP", "@Horsepower"),
	("Price", "@Price"),
	("Image", "<div><img src=\"@Image\" alt=\"\" width=\"200\"/></div>"),
]
# hover.tooltips = """
# <div>
# 	<h3>@Car</h3>
# 	<div><strong>Price:</strong>@Price</div>
# 	<div><strong>Horse Power:</strong>@Horsepower</div>
# 	<div><img src="@Image" alt="" width="200"/></div>
# </div>
# """
plot.add_tools(hover)

# Show results
show(plot)

# Save results
save(plot)

# Extract components
script, div = components(plot)
print(script)
print(div)
```

For more details, you can refer [Bokeh Online Reference][2]

## Output of the final program

```html
<script type="text/javascript">
  (function() {
    var fn = function() {
      Bokeh.safely(function() {
        (function(root) {
          function embed_document(root) {
            
          var docs_json = '{"7b2a4bed-8ba5-403d-a5cd-7374babc8bc2":{"roots":{"references":[{"attributes":{"factors":["Hennessey Venom F5","Koenigsegg Regera","Bugatti Chiron","NIO EP9","Rimac Concept One","Aston Martin Valkyrie","McLaren P1 LM","Ferrari LaFerrari"],"palette":["#084594","#2171b5","#4292c6","#6baed6","#9ecae1","#c6dbef","#deebf7","#f7fbff"]},"id":"1035","type":"CategoricalColorMapper"},{"attributes":{"below":[{"id":"1013","type":"LinearAxis"}],"center":[{"id":"1017","type":"Grid"},{"id":"1021","type":"Grid"},{"id":"1047","type":"Legend"}],"left":[{"id":"1018","type":"CategoricalAxis"}],"plot_width":800,"renderers":[{"id":"1039","type":"GlyphRenderer"}],"title":{"id":"1003","type":"Title"},"toolbar":{"id":"1028","type":"Toolbar"},"x_range":{"id":"1005","type":"DataRange1d"},"x_scale":{"id":"1009","type":"LinearScale"},"y_range":{"id":"1007","type":"FactorRange"},"y_scale":{"id":"1011","type":"CategoricalScale"}},"id":"1002","subtype":"Figure","type":"Plot"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"1046","type":"BoxAnnotation"},{"attributes":{},"id":"1022","type":"PanTool"},{"attributes":{},"id":"1058","type":"Selection"},{"attributes":{},"id":"1023","type":"WheelZoomTool"},{"attributes":{"overlay":{"id":"1046","type":"BoxAnnotation"}},"id":"1024","type":"BoxZoomTool"},{"attributes":{},"id":"1043","type":"BasicTickFormatter"},{"attributes":{},"id":"1025","type":"SaveTool"},{"attributes":{},"id":"1026","type":"ResetTool"},{"attributes":{"text":"Price of Cars with Horsepower"},"id":"1003","type":"Title"},{"attributes":{},"id":"1027","type":"HelpTool"},{"attributes":{},"id":"1009","type":"LinearScale"},{"attributes":{"callback":null,"data":{"Car":["Hennessey Venom F5","Koenigsegg Regera","Bugatti Chiron","NIO EP9","Rimac Concept One","Aston Martin Valkyrie","McLaren P1 LM","Ferrari LaFerrari"],"Horsepower":[1600,1500,1479,1341,1224,1130,986,950],"Image":["https://autowise.com/wp-content/uploads/2018/06/Hennessey-Venom-F5-15.jpg","https://autowise.com/wp-content/uploads/2018/06/Regera_front_banner2.jpg","https://autowise.com/wp-content/uploads/2018/06/chiron-768x320.webp","https://autowise.com/wp-content/uploads/2018/06/nio-ep9-1.webp","https://autowise.com/wp-content/uploads/2018/06/rimac.webp","https://autowise.com/wp-content/uploads/2018/06/aston-martin-valkyrie-9-720x720.webp","https://autowise.com/wp-content/uploads/2018/06/lanzante-p1-gtr-mclaren-2017-4.webp","https://autowise.com/wp-content/uploads/2018/06/Ferrari-LaFerrari-three-quarter-1260x570.webp"],"Price":["$1.6M","$2M"," $3.4M","$1.48M","$1M","$3.2M","$3.7M","$1M"],"index":[0,1,2,3,4,5,6,7]},"selected":{"id":"1058","type":"Selection"},"selection_policy":{"id":"1057","type":"UnionRenderers"}},"id":"1001","type":"ColumnDataSource"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"1022","type":"PanTool"},{"id":"1023","type":"WheelZoomTool"},{"id":"1024","type":"BoxZoomTool"},{"id":"1025","type":"SaveTool"},{"id":"1026","type":"ResetTool"},{"id":"1027","type":"HelpTool"},{"id":"1049","type":"HoverTool"}]},"id":"1028","type":"Toolbar"},{"attributes":{"callback":null,"factors":["Hennessey Venom F5","Koenigsegg Regera","Bugatti Chiron","NIO EP9","Rimac Concept One","Aston Martin Valkyrie","McLaren P1 LM","Ferrari LaFerrari"]},"id":"1007","type":"FactorRange"},{"attributes":{"fill_alpha":{"value":0.9},"fill_color":{"field":"Car","transform":{"id":"1035","type":"CategoricalColorMapper"}},"height":{"value":0.4},"line_color":{"value":"#1f77b4"},"right":{"field":"Horsepower"},"y":{"field":"Car"}},"id":"1037","type":"HBar"},{"attributes":{},"id":"1057","type":"UnionRenderers"},{"attributes":{},"id":"1011","type":"CategoricalScale"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"height":{"value":0.4},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"right":{"field":"Horsepower"},"y":{"field":"Car"}},"id":"1038","type":"HBar"},{"attributes":{"axis_label":"Horse power","formatter":{"id":"1043","type":"BasicTickFormatter"},"ticker":{"id":"1014","type":"BasicTicker"}},"id":"1013","type":"LinearAxis"},{"attributes":{"data_source":{"id":"1001","type":"ColumnDataSource"},"glyph":{"id":"1037","type":"HBar"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1038","type":"HBar"},"selection_glyph":null,"view":{"id":"1040","type":"CDSView"}},"id":"1039","type":"GlyphRenderer"},{"attributes":{},"id":"1014","type":"BasicTicker"},{"attributes":{"source":{"id":"1001","type":"ColumnDataSource"}},"id":"1040","type":"CDSView"},{"attributes":{"ticker":{"id":"1014","type":"BasicTicker"}},"id":"1017","type":"Grid"},{"attributes":{},"id":"1045","type":"CategoricalTickFormatter"},{"attributes":{"axis_label":"Car name","formatter":{"id":"1045","type":"CategoricalTickFormatter"},"ticker":{"id":"1019","type":"CategoricalTicker"}},"id":"1018","type":"CategoricalAxis"},{"attributes":{"items":[{"id":"1048","type":"LegendItem"}]},"id":"1047","type":"Legend"},{"attributes":{"callback":null},"id":"1005","type":"DataRange1d"},{"attributes":{},"id":"1019","type":"CategoricalTicker"},{"attributes":{"label":{"field":"Car"},"renderers":[{"id":"1039","type":"GlyphRenderer"}]},"id":"1048","type":"LegendItem"},{"attributes":{"dimension":1,"ticker":{"id":"1019","type":"CategoricalTicker"}},"id":"1021","type":"Grid"},{"attributes":{"callback":null,"tooltips":[["Car","@Car"],["HP","@Horsepower"],["Price","@Price"],["Image","&lt;div&gt;&lt;img src=\\"@Image\\" alt=\\"\\" width=\\"200\\"/&gt;&lt;/div&gt;"]]},"id":"1049","type":"HoverTool"}],"root_ids":["1002"]},"title":"Bokeh Application","version":"1.3.0"}}';
          var render_items = [{"docid":"7b2a4bed-8ba5-403d-a5cd-7374babc8bc2","roots":{"1002":"4d4da52e-a4a4-4c80-ada2-34f05752165e"}}];
          root.Bokeh.embed.embed_items(docs_json, render_items);
        
          }
          if (root.Bokeh !== undefined) {
            embed_document(root);
          } else {
            var attempts = 0;
            var timer = setInterval(function(root) {
              if (root.Bokeh !== undefined) {
                embed_document(root);
                clearInterval(timer);
              }
              attempts++;
              if (attempts > 100) {
                console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
                clearInterval(timer);
              }
            }, 10, root)
          }
        })(window);
      });
    };
    if (document.readyState != "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  })();
</script>

<div class="bk-root" id="4d4da52e-a4a4-4c80-ada2-34f05752165e" data-root-id="1002"></div>
```

![](bokeh_plot.png)

[1]: https://www.youtube.com/watch?v=2TR_6VaVSOs
[2]: https://bokeh.pydata.org/en/latest/docs/reference.html
[3]: https://bokeh.pydata.org/en/latest/docs/user_guide/tools.html
[4]: https://bokeh.pydata.org/en/latest/docs/reference/palettes.html



