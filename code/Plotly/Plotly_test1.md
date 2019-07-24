# Plotly

<!-- TOC -->

- [Plotly](#plotly)
  - [What is it?](#what-is-it)
  - [How to get started?](#how-to-get-started)
  - [To remember](#to-remember)
  - [How to Plot using plotly](#how-to-plot-using-plotly)

<!-- /TOC -->

## What is it?
It is a plotting library made for python for making interactive plots in python displayed in html files.

## How to get started?
Install plotly using ``pip``.

```bash
pip install plotly
```

You can also use ``conda`` as well.
```bash
conda install -c conda-forge plotly
```

## To remember
Plotly has two variants:

* An offline variant
* An online variant

Both of them are used for making plots. The difference is that the offline version does not the data to be stored in the plotly account.

## How to Plot using plotly
```python
# Imports
import numpy as np
import plotly.graph_objs as go
import plotly.offline as ply

# Sample data to plot
n = 201
x = np.linspace(0, 2.0*np.pi, n)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = y1 + y2

## Plotly steps begin.

### Step 1: Create Traces
trace1 = go.Scatter(
	x = x,
	y = y1,
	name = "sine curve",
	line = dict(
		color = ("green"),
		width = 4,
		dash = 'dot'
	)
)

trace2 = go.Scatter(
	x = x,
	y = y2,
	name = "cosine curve",
	line = dict(
		color = ("red"),
		width = 4,
		dash = 'dash'
	)
)

trace3 = go.Scatter(
	x = x,
	y = y3,
	name = "sine + cosine curve",
	line = dict(
		color = ("blue"),
		width = 4,
		dash = 'dashdot'
	)
)

### Step 2: Create information / layout dictionary
layout = dict(
	title = "Sine Curves",
	xaxis = dict(title = "Angle in Radian"),
	yaxis = dict(title = "Angle in Radian")
)

### Pack all the traces to get a data list
data = [trace1, trace2, trace3]

### Create a figure dictionary
fig = dict(data = data, layout = layout)

### Plot the figure in a html file
ply.plot(data, filename="plotly_test1.html")
```