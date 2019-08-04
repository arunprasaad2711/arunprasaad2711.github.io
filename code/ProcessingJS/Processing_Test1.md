# Processing Test 1 - Fourier Series Demo

## Animation

<iframe src="https://editor.p5js.org/arunprasaad2711/embed/e2nYXOn5p" width="100%" height="400px" style="border:0px;"></iframe>


## Table of Contents
<!-- TOC -->

- [Processing Test 1 - Fourier Series Demo](#processing-test-1---fourier-series-demo)
  - [Animation](#animation)
  - [Table of Contents](#table-of-contents)
  - [What is this?](#what-is-this)
  - [References](#references)
  - [Formula](#formula)
  - [How is this done?](#how-is-this-done)
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

## How is this done?

In an earlier method, I extracted the canvas elements, the javascript code and directly pasted them here. In the earlier method, the ``p5.js`` files were necessary.

In the latest method, I am writing the code in the online ``p5.js editor`` and embedding the file iframe in the webpage. Also, to make the embedding fit nicely, I added the width, height, and border attributes to the iframe. In this method, I don't need the ``p5.js`` files linked here as they are run separately.

## Source Code

```javascript
// Some variables
let time = 0;
let wave = [];
let border = [];
var slider;
var p5slider;

function setup() {
    var canvas = createCanvas(1280, 400);
  
    // Slider variables
    p5slider = createSlider(0, 100, 10);
    p5slider.position(250, 25);
    p5slider.style('width', '80px');
}

    function draw() {

    background(0);
    translate(200, 200);
    
    // Lines to extract the slider value to the program
    var val = p5slider.value();
    const n1 = val;

    // Text info
    fill(255);
    text('Fourier Series Representation of a Square Wave', -100, -180);
    text('number of terms = '+n1, -100, -160);
    text('Move the slider below to adjust the number of terms in the fourier series.', -100, -140);
      
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
```

## Status

It works like a charm! The embedding method used sorts out the slider issue quite well!

One minor development to be added is to plot the shape of the locus of the last point.

Will try to bring that in a future edit. For reference, it looks like this [d3js program on fourier series](https://bl.ocks.org/jinroh/7524988).

## Acknowledgement

Special thanks to [Daniel Shiffman](https://shiffman.net/) for his phenomenal enthusiasm in getting interested in ``p5.js``. This code is a slightly tweaked version of the same code Daniel used to teach the tutorial in his YouTube Channel - [The Coding Train](https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw) and in his website - [The Coding Train](https://thecodingtrain.com/)