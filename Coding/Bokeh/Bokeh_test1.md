# Bokeh Test 1

<!-- TOC -->

- [Bokeh Test 1](#bokeh-test-1)
  - [What is this?](#what-is-this)
  - [Source Code](#source-code)
  - [Output](#output)
  - [Status](#status)

<!-- /TOC -->

## What is this?
This is a test blog to check for statically hosted plots using ``bokeh``. Using ``bokeh`` library in python, to make a plot that renders well in a webserver. Then, the contents of the script and the div tags in the webpage are extracted and placed in the markdown file. Now, using pandoc, the markdown file is converted into a full-fledged html that is then used by python ``Jinja2`` to make a webpage. Testing Plots in Bokeh implemented in HTML.

## Source Code

```python
import numpy as np
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.embed import components

# Set up data
N = 200
x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)
source = ColumnDataSource(data=dict(x=x, y=y))

# Set up plot
plot = figure(plot_height=400, plot_width=400, title="my sine wave",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[0, 4*np.pi], y_range=[-2.5, 2.5])

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

show(plot)
script, div = components(plot)

print(div)
print(script)
# html = file_html(plot, CDN, "my plot")
```

## Output

```html
<script type="text/javascript">
  (function() {
    var fn = function() {
      Bokeh.safely(function() {
        (function(root) {
          function embed_document(root) {
            
          var docs_json = '{"37d7bad3-68c1-414e-b758-d720567f3e22":{"roots":{"references":[{"attributes":
        {"ticker":{"id":"1014","type":"BasicTicker"}},"id":"1017","type":"Grid"},{"attributes":{},
          "id":"1041","type":"BasicTickFormatter"},{"attributes":{},"id":"1026","type":"SaveTool"},
          {"attributes":{"formatter":{"id":"1041","type":"BasicTickFormatter"},"ticker":{"id":"1019",
          "type":"BasicTicker"}},"id":"1018","type":"LinearAxis"},{"attributes":{},"id":"1043",
          "type":"BasicTickFormatter"},{"attributes":{},"id":"1027","type":"WheelZoomTool"},{"attributes":
          {"below":[{"id":"1013","type":"LinearAxis"}],"center":[{"id":"1017","type":"Grid"},{"id":"1022",
          "type":"Grid"}],"left":[{"id":"1018","type":"LinearAxis"}],"plot_height":400,"plot_width":400,
          "renderers":[{"id":"1037","type":"GlyphRenderer"}],"title":{"id":"1003","type":"Title"},"toolbar":
          {"id":"1028","type":"Toolbar"},"x_range":{"id":"1005","type":"Range1d"},"x_scale":{"id":"1009",
          "type":"LinearScale"},"y_range":{"id":"1007","type":"Range1d"},"y_scale":{"id":"1011",
          "type":"LinearScale"}},"id":"1002","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"1019",
          "type":"BasicTicker"},{"attributes":{"text":"my sine wave"},"id":"1003","type":"Title"},
          {"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,
          "active_scroll":"auto","active_tap":"auto","tools":[{"id":"1023","type":"CrosshairTool"},
          {"id":"1024","type":"PanTool"},{"id":"1025","type":"ResetTool"},{"id":"1026","type":"SaveTool"},
          {"id":"1027","type":"WheelZoomTool"}]},"id":"1028","type":"Toolbar"},{"attributes":{},"id":"1044",
          "type":"UnionRenderers"},{"attributes":{"dimension":1,"ticker":{"id":"1019","type":"BasicTicker"}},
          "id":"1022","type":"Grid"},{"attributes":{"callback":null,"end":12.566370614359172},"id":"1005",
          "type":"Range1d"},{"attributes":{},"id":"1045","type":"Selection"},{"attributes":{"data_source":
          {"id":"1001","type":"ColumnDataSource"},"glyph":{"id":"1035","type":"Line"},"hover_glyph":null,
          "muted_glyph":null,"nonselection_glyph":{"id":"1036","type":"Line"},"selection_glyph":null,"view":
          {"id":"1038","type":"CDSView"}},"id":"1037","type":"GlyphRenderer"},{"attributes":{"callback":null,
          "end":2.5,"start":-2.5},"id":"1007","type":"Range1d"},{"attributes":{},"id":"1023",
          "type":"CrosshairTool"},{"attributes":{"source":{"id":"1001","type":"ColumnDataSource"}},
          "id":"1038","type":"CDSView"},{"attributes":{},"id":"1009","type":"LinearScale"},{"attributes":
          {"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"x"},"y":{"field":"y"}},
          "id":"1036","type":"Line"},{"attributes":{},"id":"1011","type":"LinearScale"},{"attributes":{},
          "id":"1024","type":"PanTool"},{"attributes":{"formatter":{"id":"1043","type":"BasicTickFormatter"},
          "ticker":{"id":"1014","type":"BasicTicker"}},"id":"1013","type":"LinearAxis"},{"attributes":
          {"line_alpha":0.6,"line_color":"#1f77b4","line_width":3,"x":{"field":"x"},"y":{"field":"y"}},
          "id":"1035","type":"Line"},{"attributes":{},"id":"1025","type":"ResetTool"},{"attributes":{},
          "id":"1014","type":"BasicTicker"},{"attributes":{"callback":null,"data":{"x":
          {"__ndarray__":"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","dtype":"float64","shape":[200]},
          "y":{"__ndarray__":"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","dtype":"float64","shape":[200]}},
          "selected":{"id":"1045","type":"Selection"},"selection_policy":{"id":"1044",
          "type":"UnionRenderers"}},"id":"1001","type":"ColumnDataSource"}],"root_ids":["1002"]},
          "title":"Bokeh Application","version":"1.2.0"}}';
          var render_items = [{"docid":"37d7bad3-68c1-414e-b758-d720567f3e22","roots":
          {"1002":"f7e2854c-5286-4729-a2ce-5c13e9ac7a77"}}];
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

<div class="bk-root" id="f7e2854c-5286-4729-a2ce-5c13e9ac7a77" data-root-id="1002"></div>
```

<script type="text/javascript">
  (function() {
    var fn = function() {
      Bokeh.safely(function() {
        (function(root) {
          function embed_document(root) {

          var docs_json = '{"37d7bad3-68c1-414e-b758-d720567f3e22":{"roots":{"references":[{"attributes":{"ticker":{"id":"1014","type":"BasicTicker"}},"id":"1017","type":"Grid"},{"attributes":{},"id":"1041","type":"BasicTickFormatter"},{"attributes":{},"id":"1026","type":"SaveTool"},{"attributes":{"formatter":{"id":"1041","type":"BasicTickFormatter"},"ticker":{"id":"1019","type":"BasicTicker"}},"id":"1018","type":"LinearAxis"},{"attributes":{},"id":"1043","type":"BasicTickFormatter"},{"attributes":{},"id":"1027","type":"WheelZoomTool"},{"attributes":{"below":[{"id":"1013","type":"LinearAxis"}],"center":[{"id":"1017","type":"Grid"},{"id":"1022","type":"Grid"}],"left":[{"id":"1018","type":"LinearAxis"}],"plot_height":400,"plot_width":400,"renderers":[{"id":"1037","type":"GlyphRenderer"}],"title":{"id":"1003","type":"Title"},"toolbar":{"id":"1028","type":"Toolbar"},"x_range":{"id":"1005","type":"Range1d"},"x_scale":{"id":"1009","type":"LinearScale"},"y_range":{"id":"1007","type":"Range1d"},"y_scale":{"id":"1011","type":"LinearScale"}},"id":"1002","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"1019","type":"BasicTicker"},{"attributes":{"text":"my sine wave"},"id":"1003","type":"Title"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"1023","type":"CrosshairTool"},{"id":"1024","type":"PanTool"},{"id":"1025","type":"ResetTool"},{"id":"1026","type":"SaveTool"},{"id":"1027","type":"WheelZoomTool"}]},"id":"1028","type":"Toolbar"},{"attributes":{},"id":"1044","type":"UnionRenderers"},{"attributes":{"dimension":1,"ticker":{"id":"1019","type":"BasicTicker"}},"id":"1022","type":"Grid"},{"attributes":{"callback":null,"end":12.566370614359172},"id":"1005","type":"Range1d"},{"attributes":{},"id":"1045","type":"Selection"},{"attributes":{"data_source":{"id":"1001","type":"ColumnDataSource"},"glyph":{"id":"1035","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1036","type":"Line"},"selection_glyph":null,"view":{"id":"1038","type":"CDSView"}},"id":"1037","type":"GlyphRenderer"},{"attributes":{"callback":null,"end":2.5,"start":-2.5},"id":"1007","type":"Range1d"},{"attributes":{},"id":"1023","type":"CrosshairTool"},{"attributes":{"source":{"id":"1001","type":"ColumnDataSource"}},"id":"1038","type":"CDSView"},{"attributes":{},"id":"1009","type":"LinearScale"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"x"},"y":{"field":"y"}},"id":"1036","type":"Line"},{"attributes":{},"id":"1011","type":"LinearScale"},{"attributes":{},"id":"1024","type":"PanTool"},{"attributes":{"formatter":{"id":"1043","type":"BasicTickFormatter"},"ticker":{"id":"1014","type":"BasicTicker"}},"id":"1013","type":"LinearAxis"},{"attributes":{"line_alpha":0.6,"line_color":"#1f77b4","line_width":3,"x":{"field":"x"},"y":{"field":"y"}},"id":"1035","type":"Line"},{"attributes":{},"id":"1025","type":"ResetTool"},{"attributes":{},"id":"1014","type":"BasicTicker"},{"attributes":{"callback":null,"data":{"x":{"__ndarray__":"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","dtype":"float64","shape":[200]},"y":{"__ndarray__":"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","dtype":"float64","shape":[200]}},"selected":{"id":"1045","type":"Selection"},"selection_policy":{"id":"1044","type":"UnionRenderers"}},"id":"1001","type":"ColumnDataSource"}],"root_ids":["1002"]},"title":"Bokeh Application","version":"1.2.0"}}';
          var render_items = [{"docid":"37d7bad3-68c1-414e-b758-d720567f3e22","roots":{"1002":"f7e2854c-5286-4729-a2ce-5c13e9ac7a77"}}];
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

## Rendered Output

<div class="bk-root" id="f7e2854c-5286-4729-a2ce-5c13e9ac7a77" data-root-id="1002"></div>

<!-- BokehJS-->
<link rel="stylesheet" href="https://cdn.pydata.org/bokeh/release/bokeh-1.3.0.min.css" type="text/css" />
<script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-1.3.0.min.js"></script>
<script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-widgets-1.3.0.min.js"></script>
<script type="text/javascript">
    Bokeh.set_log_level("info");
</script>

## Status
It works! A static plot works!