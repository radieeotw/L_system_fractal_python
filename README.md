L-System Fractal Architect

This project is a small graphical application written in Python that generates fractal patterns using L-Systems. It uses Tkinter for the GUI and Turtle graphics for drawing the fractals inside the window.
The idea behind the project is to show how simple string-rewriting rules can be expanded recursively and then visualized as geometric patterns.

What this project does
Takes an axiom (starting string) from the user
Applies L-system production rules for a given number of iterations
Converts the final string into turtle drawing commands
Displays the generated fractal inside a Tkinter window
The project supports branching using square brackets, which allows tree-like structures to be created.

Features
Simple Tkinter-based interface
Embedded turtle canvas (no separate turtle window)
Recursive L-system expansion
Support for F, +, -, [, and ] symbols
Optimized drawing using tracer() for better performance
Clean dark-themed control panel with a white drawing canvas

Tech used
Python
Tkinter
Turtle Graphics
No external libraries or frameworks are used.

How it works
The user enters the axiom, rule, angle, and number of iterations.
The L-system engine expands the axiom by applying the rules repeatedly.
The resulting string is interpreted as turtle commands.
The turtle draws the fractal on the canvas.
