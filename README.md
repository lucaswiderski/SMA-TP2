# P5 
p5.py is a python library for creative coding, with a focus on making coding accessible for  beginners, and anyone else! p5.py is free and open-source because I believe software, and the tools to learn it, should be accessible to everyone.

Using the metaphor of a sketch, p5.py has a full set of drawing functionality. However, you’re not limited to your drawing canvas. You can use every python thinks text, input, video, webcam, and sound...

P5.ps is based on pygame (opengl) graphic lib and is inspired by p5.js and other systems like arduino and prossessing.

# Get Started

## install
You must configure a project with the pygame dependency. In your terminal :
```bash
python -m venv venv 
venv\Scripts\activate
pip install pygame
```

## First sketch

in your favorite editor, start main.py :
```python
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    print("Setup END-----------")


def run():
    core.cleanScreen()

core.main(setup, run)

```
end run
```bash
python main.py
```
You get a black screen of 400x400 pixel.

## First draw
Draw a white circle center in 200x200
in your favorite editor, start main.py :
```python
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    print("Setup END-----------")


def run():
    core.cleanScreen()
	core.Draw.circle((255,255,255),(200,200),10)

core.main(setup, run)

```
end run
```bash
python main.py
```
You get a black screen of 400x400 pixel with a white circle.
### the useful functions for the drawing are : 
- core.Draw.rect(color,rect,width)
- core.Draw.cricle(color, center, radius, width)
- core.Draw.polyline(color, points, width)
- core.Draw. line(color, start_position, end_position, width)
- core.Draw.ellipse(color,rect,width)
- core.Draw.arc(color, rect, start_angle, stop_angle, width)
- core.Draw.lines(color, closed, points, width)
- core.Draw.polygon(color, points, width)
- core.Draw.text(color, text, position, size, font)

### Color :
colors are defined by tuples of 3 or 4 elements : (R,G,B) or (R,G,B,A)


## Variables
You can use python variables and their operations. However, if you want to keep data over time and between frames, you must use global variables. 

To make it easier to understand the code and to manipulate data, P5 provides a way to keep data as dictionary:
```python
core.memory(key,value)
```
Example :
Draw a circle in 200x200 store in P5 memory
```python
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
	core.memory("position",(200,200))
    print("Setup END-----------")


def run():
    core.cleanScreen()
	core.Draw.circle((255,255,255),core.memory("position"),10)

core.main(setup, run)

```

## Input
### Keybord
it is possible to detect the typing of one or more keys on the keyboard.
- press:

```python
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    print("Setup END-----------")


def run():
    core.cleanScreen()
    if core.getKeyPressList("SPACE"):
	core.Draw.circle((255,255,255),(200,200),10)

core.main(setup, run)

```

- release:

```python
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    print("Setup END-----------")


def run():
    core.cleanScreen()
    if core.getKeyReleaseList("SPACE"):
        core.Draw.circle((255,255,255),(200,200),10)

core.main(setup, run)

```
### Mouse
It is possible to interact with the mouse:
```python
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    core.memory("Center", Vector2(200,200))
    print("Setup END-----------")


def run():
    core.cleanScreen()
    if core.getMouseLeftClick():
        core.memory("Centre",Vector2(core.getMouseLeftClick()))
    
    core.Draw.circle((255,255,255),core.memory("Center"), 10)
	
core.main(setup, run)

```



## Texture
It is possible to display textures and its box.
The following example displays the image "soleil.png". 

```python
from pygame.math import Vector2
import core

def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [400, 400]
    core.memory("texture",core.Texture("./soleil.png",Vector2(200,200)))
    print("Setup END-----------")


def run():
    core.cleanScreen()
    if not core.memory("texture").ready:
        core.memory("texture").load()
		
    core.memory("texture").box = True #Display box
    core.memory("texture").show()

core.main(setup, run)

```

# Example 
## Salesperson
The travelling salesman problem (also called the travelling salesperson problem or TSP) asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once.

- mouse click : add new point
- "r" : restart

## Boids

![image](https://user-images.githubusercontent.com/941908/201973506-a714eae7-6bef-4711-913b-c45101a95f73.png)


Boids is an artificial life program, developed by Craig Reynolds in 1986, which simulates the flocking behaviour of birds. His paper on this topic was published in 1987 in the proceedings of the ACM SIGGRAPH conference. The name "boid" corresponds to a shortened version of "bird-oid object", which refers to a bird-like object. "Boid" is also a New York Metropolitan dialect pronunciation for "bird." 
- mouse left click : replustion
- mouse right click : attraction
- "r" : restart

## Game of life 

![image](https://user-images.githubusercontent.com/941908/201973583-1938fa6c-7fa3-4afd-94d4-6dc5b7add1f6.png)

The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.It is a zero-player game meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine. 
- "r" : restart
- SPACE : start / pause


## Minesweeper

![image](https://user-images.githubusercontent.com/941908/201973696-1d4e7046-3a38-41e3-ad9e-09eedb2f12a9.png)

Minesweeper is a logic puzzle video game genre generally played on personal computers. The game features a grid of clickable squares, with hidden "mines" scattered throughout the board. The objective is to clear the board without detonating any mines, with help from clues about the number of neighboring mines in each field.
- left click : reveal case
- right click : mark as mine

## Quadtree

![image](https://user-images.githubusercontent.com/941908/201973893-c95e82bf-f6c1-4185-94bd-ab30fd18ddde.png)

A quadtree is a tree data structure in which each internal node has exactly four children. Quadtrees are the two-dimensional analog of octrees and are most often used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions. The data associated with a leaf cell varies by application, but the leaf cell represents a "unit of interesting spatial information". 
- left click : add point
- right click : select area


## Other
Feel free to explore other examples


