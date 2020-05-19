from flask import Flask, render_template_string, request 
from time import sleep
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

#define GPIO pins
GPIO_pins = (14, 15, 18) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction= 20       # Direction -> GPIO Pin
step = 21      # Step -> GPIO Pin

# Declare an named instance of class pass GPIO pins numbers
mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")

app = Flask(__name__)

#HTML Code 

TPL = '''
<html>
     
    <head><title>Web Page Controlled Stepper</title></head>
    <body>
    <h2> Web Page to Control Stepper</h2>
        <form method="POST" action="test">
            <h5> Use the slider to rotate Stepper Clockwise & Counter-Clockwise  </h5>
            <p>Slider   <input type="range" min="1" max="20" name="slider" /> </p>
            <input type="submit" value="submit" />
        </form>
    </body>
</html>


'''
 
@app.route("/")
def home():

    return render_template_string(TPL)
 
@app.route("/test", methods=["POST"])
def test():
    # Get slider Values
    slider = request.form["slider"]
    print(int(slider))
  
    if (int(slider)>10):
       #mymotortest.motor_go(True, "1/16" , 3200,int(slider)*.0004, True, .05)
        mymotortest.motor_go(True, "Full" , 200,.05, True, .05)
        print("Rotating Clockwise>")
    
    if (int(slider)<10):
       mymotortest.motor_go(False, "Full" , 200,int(slider)*.0001, True, .05)
       print("Rotating Anti-Clockwise> "+str(int(slider)*.0001))

    
    return render_template_string(TPL)
 
# Run the app on the local development server
if __name__ == "__main__":
    app.run()