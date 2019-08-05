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
This is a test page for checking out ``p5.js`` animation. This is the 5th javascript export version of ``processing`` programming language. Here, the fourier series summation of a square wave is tested.

## References
* [Coding Challenge #125: Fourier Series video on YouTube by Daniel Shiffman](https://www.youtube.com/watch?v=Mm2eYfj0SgA)
* [d3js program on fourier series](https://bl.ocks.org/jinroh/7524988)

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
var p5slider;

function setup() {
    var canvas = createCanvas(1280, 400);
  
    // Slider variables
    p5slider = createSlider(0, 100, 10);
    p5slider.position(250, 25);
    p5slider.style('width', '200px');
}

    function draw() {

    background(245);
    translate(200, 200);
    
    // Lines to extract the slider value to the program
    var val = p5slider.value();
    const n1 = val;

    // Text info
    stroke(50,50,50);
    strokeWeight(1);
    fill(50);
    text('Fourier Series Representation of a Square Wave', -100, -180);
    text('number of terms = '+n1, -100, -160);
    text('Move the slider above to adjust the number of terms in the fourier series.', -100, -140);
      
    let x = 0;
    let y = 0;

    for (let i = 0; i < n1; i++){
        
        prev_x = x;
        prev_y = y;
        
        let n = 2 * i + 1;
        let radius = 60 * (4 /(n * PI));
        x += radius * cos(n * time);
        y += radius * sin(n * time);

        stroke(60,79,118);
        strokeWeight(1);
        noFill();
        ellipse(prev_x, prev_y, radius*2);
        
        fill(255);
        stroke(171,159,157);
        strokeWeight(2);
        line(prev_x, prev_y, x, y);
    }
    wave.unshift(y);
    border.unshift(x);
      
    beginShape();
    strokeWeight(0.5);
    stroke(0,0,128);
    noFill();
    for (let i = 0; i < border.length; i++){
        vertex(border[i], wave[i]);
    }
    endShape();

    fill(255, 255, 255);
    stroke(0,0,0); 

    translate(200, 0);
    line(x-200, y, 0, wave[0]);

    stroke(128,0,0);
    strokeWeight(2);
    beginShape();
    noFill();
    for (let i = 0; i < wave.length; i++){
        vertex(i, wave[i]);
    }
    endShape();
    
    time += 0.05;

    if (wave.length > 600){
        wave.pop();
        border.pop();
    }
}
```

## Status

It works like a charm! The embedding method used sorts out the slider issue quite well! Even the locus of the last point was brought out quite well due to a slight tweak to the code.

## Acknowledgement

Special thanks to [Daniel Shiffman](https://shiffman.net/) for his phenomenal enthusiasm in getting me interested in ``p5.js``. This code is a slightly tweaked version of the same code Daniel used to teach the tutorial in his YouTube Channel - [The Coding Train](https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw) and in his website - [The Coding Train](https://thecodingtrain.com/)