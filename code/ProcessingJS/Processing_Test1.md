# Processing Test 1

<!-- TOC -->

- [Processing Test 1](#processing-test-1)
  - [What is this?](#what-is-this)
  - [References](#references)
  - [Formula](#formula)
  - [Source Code](#source-code)
  - [Animation](#animation)
  - [Status](#status)

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
<div class="box" id="p5js__sketch">
</div>

<div class="slidecontainer">
<p>Move the slider value below to adjust the number of terms. [Min = 0, Default = 10, Max = 200] <span>Number of terms: <span id="demo"></span> </span></p>
<input type="range" min="1" max="200" value="10" class="slider" id="myRange">
</div>

<script>
    let time = 0;
    let wave = [];
    let border = [];

    function setup() {
        var canvas = createCanvas(1150, 400);
        canvas.parent('p5js__sketch');
    //  wSlider = createSlider(0, 200, 10);
    //  wSlider.position(30, 30);
    //  wSlider.style('width', '80px');
    }

    function draw() {

        background(0);
        translate(200, 200);
        
        // const n1 = wSlider.value();
        var slider = document.getElementById("myRange");
        var output = document.getElementById("demo");
        output.innerHTML = slider.value;

        slider.oninput = function() {
        output.innerHTML = this.value;
        }
        const n1 = slider.value;

        fill(255);
        text('Fourier Series Representation of a Square Wave', 250, -180);
        text('number of terms = '+n1, 325, -160);
        
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

## Animation
<div class="box" id="p5js__sketch">
</div>

<div class="slidecontainer">
<p>Move the slider value below to adjust the number of terms. [Min = 0, Default = 10, Max = 200] <span>Number of terms: <span id="demo"></span> </span></p>
<input type="range" min="1" max="200" value="10" class="slider" id="myRange">
</div>

<script>
    let time = 0;
    let wave = [];
    let border = [];

    function setup() {
        var canvas = createCanvas(1150, 400);
        canvas.parent('p5js__sketch');
    //  wSlider = createSlider(0, 200, 10);
    //  wSlider.position(30, 30);
    //  wSlider.style('width', '80px');
    }

    function draw() {

        background(0);
        translate(200, 200);
        
        // const n1 = wSlider.value();
        var slider = document.getElementById("myRange");
        var output = document.getElementById("demo");
        output.innerHTML = slider.value;

        slider.oninput = function() {
        output.innerHTML = this.value;
        }
        const n1 = slider.value;

        fill(255);
        text('Fourier Series Representation of a Square Wave', 250, -180);
        text('number of terms = '+n1, 325, -160);
        
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

## Status

It works! The slider has some issues as the default ``p5.js`` slider is not working. So, added a custom slider. One minor tweak is that the shape of the outer ring is not coming properly. Will try to bring that in a future edit. For reference, it looks like this [d3js program on fourier series](https://bl.ocks.org/jinroh/7524988).