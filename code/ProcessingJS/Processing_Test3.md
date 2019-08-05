# Processing Test 3 - Fourier Transformation Demo

## Animation

<iframe src="https://editor.p5js.org/arunprasaad2711/embed/0mXXIEAvE" width="100%" height="800px" style="border:0px;"></iframe>

## Table of Contents
<!-- TOC -->

- [Processing Test 3 - Fourier Transformation Demo](#processing-test-3---fourier-transformation-demo)
  - [Animation](#animation)
  - [Table of Contents](#table-of-contents)
  - [What is this?](#what-is-this)
  - [References](#references)
  - [How is this done?](#how-is-this-done)
    - [Step 1 : Extract the points using Python OpenCV](#step-1--extract-the-points-using-python-opencv)
    - [Step 2 - Write the DFT function using ``p5.js``](#step-2---write-the-dft-function-using-p5js)
    - [Step 3 - Write the main code](#step-3---write-the-main-code)
  - [Status](#status)
  - [Acknowledgement](#acknowledgement)

<!-- /TOC -->

## What is this?
This is a test page for checking out ``p5.js`` animation. This is the 5th javascript export version of ``processing`` programming language. Here, the fourier transformation of the boundary points of the eight note is taken and using the discrete fourier transformation of the $x$ and $y$ coordinates, a set of epicycles is used to recreate the figure.

## References
* [Coding Challenge #130.1: Drawing with Fourier Transform and Epicycles video on YouTube by Daniel Shiffman](https://www.youtube.com/watch?v=MY4luNgGfms)
* Random google search

## How is this done?

This is the image

<div class="box align-center">![Eight Note](eight_note.jpg)</div>

### Step 1 : Extract the points using Python OpenCV

```python
import cv2
import numpy as np

# Load the image
image = cv2.imread('eight_note.jpg')

# make it grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 30, 200)

# Finding Contours
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Remove extra array axes
new_contours = np.squeeze(contours)

# Extract the points
points = []
for point in new_contours:
	temp = {'x': point[0], 'y': point[1]}
	points.append(temp)

# Print them for viewing
# print(points)

# Write the points as a javascript file.
file_path = "logo.js" ## your path variable
with open(file_path, 'w') as f:
	f.write("%s\n" % 'let drawing = [')
	for item in points:
		f.write("%s,\n" % item)
	f.write("%s\n" % '];')
```

The ``logo.js`` file will look like this:

```javascript
let drawing = [
{'x': 197, 'y': 21},
{'x': 196, 'y': 22},
{'x': 195, 'y': 22},
{'x': 195, 'y': 23},
{'x': 195, 'y': 24},
{'x': 195, 'y': 25},
.....
{'x': 200, 'y': 21},
{'x': 199, 'y': 21},
{'x': 198, 'y': 21},
];
```

### Step 2 - Write the DFT function using ``p5.js``

The Discrete Fourier Transform (DFT) of $N$ complex numbers $\{x_n\} := x_0, x_1, \dots, x_{n-1}$ is another sequence of $N$ complex numbers $\{X_n\} := X_0, X_1, \dots, X_{n-1}$ given by

$$
\begin{align*}
X_k &= \sum_{n=0}^{N-1}x_n.e^{-\frac{i2\pi}{N}kn}\\
    &= \sum_{n=0}^{N-1}x_n.[cos(2\pi kn/N) - i.sin(2\pi kn/N)]
\end{align*}
$$

The equivalent source code is written in the file ``fourier.js``.

```javascript
function dft(x)
{
    
    let X = [];
    const N = x.length;
  
    for (let k = 0; k < N; k++)
    {
        let re = 0;
        let im = 0;
        for (let n = 0; n < N; n++)
        {
            const phi = (TWO_PI * k * n) / N;
            re += x[n] * cos(phi);
            im -= x[n] * sin(phi);
        }
      
        re = re / N;
        im = im / N;
      
        let freq = k;
        let amp = sqrt(re * re + im * im);
        let phase = atan2(im, re);
        
        X[k] = {re, im, freq, amp, phase};
    }
    return X;
}
```
### Step 3 - Write the main code

```javascript
let x = [];
let y = [];
let fourierX = [];
let fourierY = [];
let time = 0;
let path = [];

function setup() {
  createCanvas(800, 800);
  const skip = 1;
  for(let i = 0; i < drawing.length; i+= skip){
    x[i] = drawing[i].x;
    y[i] = drawing[i].y;
  }
  
  // for(let i = 0; i < 100; i+= skip){
  //   x[i] = i;
  //   y[i] = i;
  // }
  
  fourierX = dft(x);
  fourierY = dft(y);
  
  fourierX.sort((a, b) => b.amp - a.amp);
  fourierY.sort((a, b) => b.amp - a.amp);
}

function epiCycle(x, y, rotation, fourier)
{
  for (let i = 0; i < fourierY.length; i++)
  {
    let prev_x = x;
    let prev_y = y;
    
    let freq = fourier[i].freq;
    let radius = fourier[i].amp;
    let angle = rotation + freq * time + fourier[i].phase;
    x += radius * cos(angle);
    y += radius * sin(angle);
    
    stroke(255, 100);
    noFill();
    ellipse(prev_x, prev_y, radius * 2);
    stroke(255);
    line(prev_x, prev_y, x, y);
  }
  return createVector(x, y);
}

function draw() {
  background(0);
  
  let vx = epiCycle(300, 50, 0, fourierX);
  let vy = epiCycle(50, 200, HALF_PI, fourierY);
  let v = createVector(vx.x, vy.y);
  
  path.unshift(v);
  
  // translate(200, 0);
  line(vx.x, vx.y, v.x, v.y);
  line(vy.x, vy.y, v.x, v.y);
  beginShape();
  noFill();
  for (let i = 0; i < path.length; i++) {
    vertex(path[i].x, path[i].y);
  }
  endShape();
  
  const dt = TWO_PI / fourierY.length;
  time += dt;
  
  if (time > TWO_PI)
  {
    time = 0;
    path.pop();
  }
}
```

## Status

It works pretty slowly! The code is quite slow as it calculates more than 1700 components for $x$ coordinates and another 1700+ components for $y$ coordinates respectively.

## Acknowledgement

Special thanks to [Daniel Shiffman](https://shiffman.net/) for his phenomenal enthusiasm in getting me interested in ``p5.js``. This code is a slightly tweaked version of the same code Daniel used to teach the tutorial in his YouTube Channel - [The Coding Train](https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw) and in his website - [The Coding Train](https://thecodingtrain.com/)