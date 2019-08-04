# Processing Test 2 - Rose Curves

<!-- TOC -->

- [Processing Test 2 - Rose Curves](#processing-test-2---rose-curves)
  - [Animation](#animation)
  - [What is this?](#what-is-this)
  - [Source Code](#source-code)
  - [Issue](#issue)

<!-- /TOC -->

## Animation

<iframe src="https://editor.p5js.org/arunprasaad2711/embed/cbzzwsqj1" width="100%" height="400px" style="border:0px;"></iframe>

## What is this?
This is a ``p5js`` animation of [rose curves](https://en.wikipedia.org/wiki/Rose_(mathematics)).

## Source Code

```javascript
let time = 0;
let wave_x = [];
let wave_y = [];
var slider_n;
var slider_d;

function setup() {
    
    var canvas = createCanvas(600, 400);
    var button = createButton("reset");
    button.mousePressed(resetSketch);
    button.position(35, 35);

  
    // Numerator Slider variables
    slider_n = createSlider(0, 10, 2);
    slider_n.position(100, 25);
    slider_n.style('width', '80px');
  
    // Denominator Slider variables
    slider_d = createSlider(0, 10, 1);
    slider_d.position(100, 50);
    slider_d.style('width', '80px');
}

function draw() {

    background(125);
    strokeWeight(1);
    translate(200, 200);
  
    const n = slider_n.value();
    const d = slider_d.value();
    const k = n/d;
    const radius = 100;

    fill(25);
    stroke(0);
    text('Rose Curves or Rhodonea Curves', 0, -180);
    text('Numerator, n = '+ n +'; Denominator, d = '+ d +'; k = n/d = '+k, 0, -160);
    text('Move the sliders on the left to adjust the numerator and denonimator.', 0, -140);
    text('Press the reset button when the slider value changes.', 0, -120);

    let x = 0;
    let y = 0;
    let ox = 0;
    let oy = 0;

    fill(255, 0, 0);
    circle(x, y, 10);
    noFill();
    circle(x, y, 2*radius);
  
    let phase = 0.0*HALF_PI;
    
    x += radius * cos(k * time - phase)*cos(time - phase);
    y += radius * cos(k * time - phase)*sin(time - phase);

    wave_x.push(x);
    wave_y.push(y);
  
    var last = wave_x.length - 1;
    
    fill(0, 0, 255);
    stroke(0, 0, 255);
    fill(0, 255, 0);
    line(ox, oy, x, y);
    circle(wave_x[last], wave_y[last], 10);

    beginShape();
    noFill();
    for (let i = 0; i < wave_x.length; i++){
        vertex(wave_x[i], wave_y[i]);
    }
    endShape();

    time += 0.05;

    if (wave_x.length > 2000){
        resetSketch();
    }
}

function resetSketch() {
    wave_x = [];
    wave_y = [];
}
```

## Issue
Work in Progress. Stuck with the array and tracing.