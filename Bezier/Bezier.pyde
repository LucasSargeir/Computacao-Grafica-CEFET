MOUSE_SIDE = LEFT
SHOW_LINES = False
TEXT_SIZE = 20
p1 = (100, 700)  
p2 = (700, 700)
p3 = (100, 700)  
p4 = (700, 700)

def setup():
  size(800,800)
  frameRate(60)
  textSize(TEXT_SIZE)
  stroke(0)

def draw():
  global p1,p2, p3, p4, SHOW_LINES  
  background(128);

  p3, p4 = mouse_handle(20)
  
  for_range = [x * 0.1 for x in range(0, 11)]
  
  beginShape()
  vertex(p1);
  
  for t in for_range:
    a_p3 = find_point(p1, p3, t)
    b_p3 = find_point(p3, p4, t)
    c_p3 = find_point(a_p3, b_p3, t)
    
    a_p4 = find_point(p3, p4, t)
    b_p4 = find_point(p4, p2, t)
    c_p4 = find_point(a_p4, b_p4, t)
    
    d = find_point(c_p3, c_p4, t)
    
    vertex(d)


  if SHOW_LINES: 
    draw_lines()
  
  vertex(p2)
  endShape(CLOSE)
  
#-------------------------- MY FUNCTIONS ------------------------

def mouse_handle(diameter):
    global MOUSE_SIDE, SHOW_LINES, p3, p4
    
    new_p3 = p3
    new_p4 = p4
    
    mouse_bkp = MOUSE_SIDE
    if mousePressed:
        MOUSE_SIDE = mouseButton

    if MOUSE_SIDE == CENTER:
        MOUSE_SIDE = mouse_bkp
        SHOW_LINES = not SHOW_LINES
        
    if MOUSE_SIDE == LEFT:
        new_p3 = (mouseX, mouseY)
        fill(255,255,0)
        text("Left", diameter + 10, TEXT_SIZE + 4) 
    elif MOUSE_SIDE == RIGHT:
        new_p4 = (mouseX, mouseY)
        fill(0,255,255)
        text("Right", diameter + 10, TEXT_SIZE + 4) 
    
    circle((diameter/2) + 5, (diameter/2) + 5, diameter)
    fill(255)
    
    return new_p3, new_p4
    
def draw_lines():
    global p1, p2, p3, p4
  
    line(p1[0], p1[1], p3[0], p3[1])
    line(p2[0], p2[1], p4[0], p4[1])
    line(p3[0], p3[1], p4[0], p4[1])
    
def find_point(p1, p2, t):
    x = p1[0] + t*(p2[0] - p1[0])
    y = p1[1] + t*(p2[1] - p1[1])
    
    return x, y
  
  
