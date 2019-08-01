# Processing Test 1 - Fourier Series Demo

## Animation

<div class="box", id="p5js__sketch"></div>

<div class="slidecontainer">
<p>Move the slider value below to adjust the number of terms. [Min = 0, Default = 10, Max = 200] <span>Number of terms: <span id="demo"></span> </span></p>
<input type="range" min="1" max="200" value="10" class="slider" id="myRange">
</div>

<script>
let time = 0;
let wave = [];
let border = [];
var slider;
var p5slider;

// var ABS_position = getOffset( document.getElementById('p5js__sketch') );

function setup() {
    var canvas = createCanvas(displayWidth*0.84, displayHeight*0.5);
    canvas.parent('p5js__sketch');

    // code for internal (problematic) slider to work
    // p5slider = createSlider(0, 200, 10);
    // p5slider.position(width*0.3, 400);
    // p5slider.style('width', '80px');
}

    function draw() {

    background(0);
    translate(200, 200);

    // code for external slider to work
    var slider = document.getElementById("myRange");
    var output = document.getElementById("demo");
    output.innerHTML = slider.value;

    slider.oninput = function() {
        output.innerHTML = this.value;
    }
    const n1 = slider.value;
    
    // code for internal (problematic) slider to work
    // var val = p5slider.value();
    // const n1 = val;

    fill(255);
    text('hello', 250, -280);
    text('Fourier Series Representation of a Square Wave', 250, -180);
    text('number of terms = '+n1, 325, -160);
    text('Move the slider below to adjust the number of terms in the fourier series.', 185, -140);
    // text(ABS_position, 400 -180);

    let x = 0;
    let y = 0;

    for (let i = 0; i < n1; i++){
        
        prev_x = x;
        prev_y = y;
        
        let n = 2 * i + 1;
        let radius = 60 * (4 /(n * PI));
        x += radius * cos(n * time);
        y += radius * sin(n * time);

        stroke(255, 100);
        noFill();
        ellipse(prev_x, prev_y, radius*2);
        
        fill(255);
        stroke(255);
        line(prev_x, prev_y, x, y);
        // point(prev_x, prev_y);
    }
    wave.unshift(y);
    border.unshift(y);

    fill(255, 255, 255);
    stroke(255);
    // ellipse(x, y, 8);

    translate(200, 0);
    line(x-200, y, 0, wave[0]);

    beginShape();
    noFill();
    for (let i = 0; i < wave.length; i++){
        vertex(i, wave[i]);
    }
    endShape();

    time += 0.05;

    if (wave.length > 1500){
        wave.pop();
    }
}
</script>

<!-- TOC -->

- [Processing Test 1 - Fourier Series Demo](#processing-test-1---fourier-series-demo)
  - [Animation](#animation)
  - [What is this?](#what-is-this)
  - [References](#references)
  - [Formula](#formula)
  - [Source Code](#source-code)
  - [Status](#status)
  - [Acknowledgement](#acknowledgement)

<!-- /TOC -->

## What is this?
This is a test page for checking out ``processingJS`` animation. Here, the fourier series summation of a square wave is tested.

## References
* [Coding Challenge #125: Fourier Series video on YouTube by Daniel Shiffman](https://www.youtube.com/watch?v=Mm2eYfj0SgA)
* [W3Schools tutorial on creating slider](https://www.w3schools.com/howto/howto_js_rangeslider.asp)

## Formula

The square wave defined here $f(t)$ is a periodic function defined between the period $0 < t < 2\pi$. It's definition is

$$ f(t) = \begin{cases} 
               60  & 0 < t < \pi\\
               -60  & \pi < t < 2\pi
          \end{cases} $$

The Fourier series representation of this is given by

$$
\begin{align*}
    f(t) &= 60 \times \frac{4}{\pi} \sum_{n=1}^{\infty} \frac{\sin(2\pi(2k - 1)ft)}{2k - 1}\\
         &= 60 \times \frac{4}{\pi} \left( \sin(\omega t) + \frac{1}{3} \sin(3\omega t) + \frac{1}{5} \sin(5\omega t) + \dots \right) \hspace{1 cm} \text{where } \omega = 2\pi f\\
\end{align*}
$$

## Source Code

```html
<script>
let time = 0;
let wave = [];
let border = [];
var slider;
var p5slider;

// var ABS_position = getOffset( document.getElementById('p5js__sketch') );

function setup() {
    var canvas = createCanvas(displayWidth*0.84, displayHeight*0.5);
    canvas.parent('p5js__sketch');

    // code for internal (problematic) slider to work
    // p5slider = createSlider(0, 200, 10);
    // p5slider.position(width*0.3, 400);
    // p5slider.style('width', '80px');
}

    function draw() {

    background(0);
    translate(200, 200);

    // code for external slider to work
    var slider = document.getElementById("myRange");
    var output = document.getElementById("demo");
    output.innerHTML = slider.value;

    slider.oninput = function() {
        output.innerHTML = this.value;
    }
    const n1 = slider.value;
    
    // code for internal (problematic) slider to work
    // var val = p5slider.value();
    // const n1 = val;

    fill(255);
    text('hello', 250, -280);
    text('Fourier Series Representation of a Square Wave', 250, -180);
    text('number of terms = '+n1, 325, -160);
    text('Move the slider below to adjust the number of terms in the fourier series.', 185, -140);
    // text(ABS_position, 400 -180);

    let x = 0;
    let y = 0;

    for (let i = 0; i < n1; i++){
        
        prev_x = x;
        prev_y = y;
        
        let n = 2 * i + 1;
        let radius = 60 * (4 /(n * PI));
        x += radius * cos(n * time);
        y += radius * sin(n * time);

        stroke(255, 100);
        noFill();
        ellipse(prev_x, prev_y, radius*2);
        
        fill(255);
        stroke(255);
        line(prev_x, prev_y, x, y);
        // point(prev_x, prev_y);
    }
    wave.unshift(y);
    border.unshift(y);

    fill(255, 255, 255);
    stroke(255);
    // ellipse(x, y, 8);

    translate(200, 0);
    line(x-200, y, 0, wave[0]);

    beginShape();
    noFill();
    for (let i = 0; i < wave.length; i++){
        vertex(i, wave[i]);
    }
    endShape();

    time += 0.05;

    if (wave.length > 1500){
        wave.pop();
    }
}
</script>
```

## Status

It works! The slider has some issues as the default ``p5.js`` slider is not working. So, added a custom slider. One minor tweak is that the shape of the outer ring is not coming properly. Will try to bring that in a future edit. For reference, it looks like this [d3js program on fourier series](https://bl.ocks.org/jinroh/7524988).

## Acknowledgement

Special thanks to [Daniel Shiffman](https://shiffman.net/) for his phenomenal enthusiasm in getting interested in ``p5.js``. This code is a slightly tweaked version of the same code Daniel used to teach the tutorial in his YouTube Channel - [The Coding Train](https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw) and in his website - [The Coding Train](https://thecodingtrain.com/)