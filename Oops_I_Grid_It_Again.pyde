x = 0
y = 0
xGrid = int(random(5, 40)) # this variable generates a random variable between 5 and 50 for the x value of the grid size
yGrid = int(random(10, 100)) # this variable generates a random variable between 10 and 100 for the y value of the grid size
a = 0
a_ = 0

def setup():
    size(800, 800)
    frameRate(5)
    
def draw():
    global x, y, a, a_
    background(203, 86, 203)
    strokeCap(CORNER)
    strokeWeight(xGrid)
    num = int((width / xGrid) * (height / yGrid)) # number of rectangles in grid
    
    n = 0
    while n < num:
        stroke(100 - 50 * tan(radians(a)), 150 - 50 * cos(radians(a)), 150 - 100 * sin(radians(a)), 255 - 255 * sin(radians(a)))
        # the colour of the stroke/grid uses trigonometric functions to create movement in the artwork
        line(x, y, x, y + yGrid) # the y-coordinate of the second point in the line is determined by the random integer generated
        x += xGrid # repeat grid along the x-axis
        if x > width: 
            x = xGrid/2 # contains the grid within the size parameters
            y += yGrid # repeat grid along the y-axis
        if y >= height:
            y = 0 # contains the grid within the size parameters
            a = 0 # allows the trigonometric movement of colours to remain as a looped pattern, rather than a constantly evolving movement
                
        n += 1 # allows the loop to repeat
        a += a_ # applies the colour to the grid
        
        a_ += 0.1 # allows pattern to be uniform
   
def mouseClicked():
    # when clicking the mouse, the size of the grids double
    global xGrid, yGrid
    xGrid = xGrid * 2
    yGrid = yGrid * 2
    
def keyPressed():
    # when pressing any key on the keyboard, the grid size will decrease by half
    global xGrid, yGrid
    xGrid = xGrid / 2
    yGrid = yGrid / 2
