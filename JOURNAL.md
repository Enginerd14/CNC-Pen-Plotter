This is where I will document the process of building my **CNC pen plotter**
## 08/12/25


## 09/12/25

Today, I began considering the Circuit components required for this project.
There are 5 parts to this circuit.
- Microcontroller - I decided on the ESP 32 WROOM 32 due to its versatility, multiple GPIO pins and also the opportunity for WiFi and Bluetooth support
- Stepper motors - I chose the NEMA 17, probably the most common stepper motor used in low cost 3D printers and CNC machinery
- Stepper motor drivers - I descided on the TMC2209, a smooth, low noise alternative to the common A4988 and DRV8825 modules
- Limit switches
- Servo motor - I am using the SG90 due to its compatibility and lightweight

  However, there are some issues. The motors and the motor drivers need a 12V supply whereas the servo only uses 5V and the ESP32 only uses 3.3V. Therefore, I will use a buck regualtor, the LM2596 to step down the 12V to 5V and 3.3V. 

Hours Spent: 2Hrs
## 10/12/25

I began producing a rough design of the outcome in Solidworks. First, I produced the components I will use seperately. I produced a 2020 aluminium extrusion. These will create the two axes: the X-axis and the Y-axis. Then I created the V-WHeels that will glide along the rails. The V-Wheels were then nestled between two plates using 5mm spacers. On this plate, the X-axis will be attached. I repeated this combination for the Y-axis where the plates will be attached to the pen holder. I then created an assembly of both the X-axis and Y-axis. 


Hours Spent: 5Hrs
