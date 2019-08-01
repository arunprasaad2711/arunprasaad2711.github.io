# Processing Test 2 - Rose Curves

<!-- TOC -->

- [Processing Test 2 - Rose Curves](#processing-test-2---rose-curves)
  - [Animation](#animation)
  - [What is this?](#what-is-this)
  - [Issue](#issue)

<!-- /TOC -->

## Animation

<div class="box", id="p5js__sketch"></div>

<div class="slidecontainer">
<p>Move the sliders below to adjust the numerator $n$ and the denominator $d$ of the $k$ term. Where, $k = \displaystyle{\frac{n}{d}}$.<br/>Numerator ($n$):<span id="numerator"></span>   [Min = 0, Default = 2, Max = 10]</p>
<input type="range" min="0" max="10" value="2" class="slider" id="numeratorRange">
<p>Denominator ($d$):<span id="denominator"> </span>   [Min = 0, Default = 2, Max = 10]</p>
<input type="range" min="0" max="10" value="2" class="slider" id="denominatorRange">
</div>

<script>
let time = 0;
let wave = [];
let border = [];

function setup() {
    var canvas = createCanvas(displayWidth*0.84, displayHeight*0.5);
    canvas.parent('p5js__sketch');
}

function draw() {

    background(225);
    strokeWeight(1);
    translate(200, 200);

    // code for external slider to work
    var slider_n = document.getElementById("numeratorRange");
    var slider_d = document.getElementById("denominatorRange");
    var numerator = document.getElementById("numerator");
    var denominator = document.getElementById("denominator");
    numerator.innerHTML = slider_n.value;
    denominator.innerHTML = slider_d.value;

    slider_n.oninput = function() {
        numerator.innerHTML = this.value;
    }
    
    slider_d.oninput = function() {
        denominator.innerHTML = this.value;
    }
    
    const n = slider_n.value;
    const d = slider_d.value;
    const k = n/d;
    const radius = 20;

    fill(25);
    stroke(0);
    text('hello', 250, -280);
    text('Rose Curves or Rhodonea Curves', 250, -180);
    text('Numerator = '+n+'; Denominator = '+d+'; k = n/d = '+k, 225, -160);
    text('Move the slider below to adjust the numerator and denonimator.', 185, -140);

    translate(350, 0);

    let x = 0;
    let y = 0;
    let prev_x = 0;
    let prev_y = 0;

    fill(255, 0, 0);
    circle(x, y, 10);

    // while (true)
    //{
        prev_x = x;
        prev_y = y;
        
        x += radius * cos(k * time)*sin(time);
        y += radius * sin(k * time)*sin(time);

        fill(0, 0, 255);
        stroke(0, 0, 255);
        line(prev_x, prev_y, x, y);

        time += 0.05;
    // }
}
</script>

## What is this?
This is a ``p5JS`` animation of [rose curves](https://en.wikipedia.org/wiki/Rose_(mathematics)).

## Issue
Work in Progress. Stuck with the array and tracing.