# Processing Test 2

<!-- TOC -->

- [Processing Test 2](#processing-test-2)
  - [What is this?](#what-is-this)
  - [Animation](#animation)
  - [Issue](#issue)

<!-- /TOC -->

## What is this?
This is a test page for checking out ``processingJS`` animation. Here, the fourier series summation of a square wave is tested.

## Animation

<div id="container" class=""></div>
<div id="p5js__sketch" class=""></div>
<script>
//     let sketch = function(p) 
//     {
//         var slider;
//         p.setup = function()
//         {
//             canvas = createCanvas(200, 200);
//             slider = createSlider(0, 255, 250);
//             slider.position(20, 200);
//             slider.style('width', '80px');
//         }
//         p.draw() = function()
//         {
//             var val = slider.value();
//             background(val);
//         }
//     };
//   new p5(sketch, 'container');
    var slider;
    function setup() {
        var canvas = createCanvas(windowHeight, windowHeight);
        canvas.parent("p5js__sketch");
        slider = createSlider(0, 255, 250);
        slider.position(200, 200);
        slider.style('width', '80px');
    }
    function draw() {
        var val = slider.value();
        background(val);
    }
</script>

## Issue
While animation **can** work, the slider is pushed to the top of the page. It has absolute position.