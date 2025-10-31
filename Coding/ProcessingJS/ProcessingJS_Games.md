# ProcessingJS Games, and Simulations

ProcessingJS can be used for making games and visualizations. And as a consequence, you can make illustrations as well!

## Sources:
* Khan Academy computer programming course on Advanced JS: Games and Visualizations, and Advanced JS: Natural Simulations

## Scenes and buttons
Scenes are snapshots in a game. 

* You can use functions to generate scenes and call them one by one by using ``if`` statement logics and mouse pressed keywords.
* Creating buttons and clicking them can generate function calls.
	* For buttons to work, create a button and use logics to see if the mouse click happens on the mouse region. If true, invoke a function call.
	* If possible, make the buttons generic so that they can be produced from a function given with an input object. This makes the creation easier.
* Interactive scenes can be made by creating functions and executing them whenever a mouse is pressed or a button is pressed.

## Randomness

A random walker code:
```JavaScript

// Adapted from Dan Shiffman, natureofcode.com

var Walker = function() {
    this.x = width/2;
    this.y = height/2;
};

Walker.prototype.display = function() {
    stroke(0, 0, 0);
    point(this.x, this.y);
};

// Randomly move up, down, left, right, or stay in one place
Walker.prototype.walk = function() {
    var choice = floor(random(4));
    if (choice === 0) {
        this.x++;
    } else if (choice === 1) {
        this.x--;
    } else if (choice === 2) {
        this.y++;
    } else {
        this.y--;
    } 
};

var w = new Walker();

var draw = function() {
    w.walk();
    w.display();
};

```


