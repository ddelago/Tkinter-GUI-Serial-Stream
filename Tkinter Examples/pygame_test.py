import pygame
import serial
ser = serial.Serial('/dev/pts/21')
ser.baudrate = 9600
print(ser.name)
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputing the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    

pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
    
# Get ready to print
textPrint = TextPrint()

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

 
    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # For each 
    joystick = pygame.joystick.Joystick(4)
    joystick.init()
        
    textPrint.print(screen, "Joystick {}".format(4) )
    textPrint.indent()
        
    # Get the name from the OS for the controller/joystick
    name = joystick.get_name()
    textPrint.print(screen, "Joystick name: {}".format(name) )
            
    #for i in range( axes ):
    axis0 = joystick.get_axis( 0 )+1
    axis3 = (joystick.get_axis( 3 )+1)/2
    axis4 = (joystick.get_axis( 4 )+1)/2
    
    button = str(joystick.get_button(1))
    button6 = str(joystick.get_button(6))
    button7 = str(joystick.get_button(7))
    
    textPrint.print(screen, "Axis {} value: {:>6.3f}".format(0, axis0) )
    textPrint.print(screen, "Axis {} value: {:>6.3f}".format(3, axis3) ) #-1 to 1 ; -1 is resting
    textPrint.print(screen, "Axis {} value: {:>6.3f}".format(4, axis4) )
    axis0 =("%.3f" % axis0)
    axis3 =("%.3f" % axis3)
    axis4 =("%.3f" % axis4)
    
    axis = axis3+","+axis4+","+ axis0 + "," + button + "," + button6 + "," + button7 + "/"
    ser.write(axis.encode()) 

    textPrint.unindent()
                
    textPrint.unindent()

    
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(20)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
