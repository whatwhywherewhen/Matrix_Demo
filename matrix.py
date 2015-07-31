import simplegui
import math
from random import randrange as r
from random import choice as c

message=[""]
R,G,B = 0,180,10

val = lambda v:v
inc = lambda x: x==1 and val(r(2,6)) \
                or x<12 and x \
                or val(r(2,6))

        
def timer_handler():
    global message
    message = [''.join([c([chr(r(32,127)),'0','0','1']) for i in xrange( inc(len(message[j])+1) )]) for j in xrange(len(message))]
    if len(message) <= 22: message.extend(["",""]) 


# Handler to draw on canvas
def draw(canvas):
    for m in xrange(len(message)):
        k = r(19,23)
        [canvas.draw_text(message[m][i], [50+m*22,112+22*i], k, "White" if r(50)==1 else ("rgb(%s,%s,%s)"%(R,G,B)), 'monospace') for i in xrange(len(message[m]))]
                         
                         
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 620, 567)
frame.set_canvas_background('#171717')
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
timer.start()