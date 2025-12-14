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

I began producing a rough design of the outcome in Solidworks. First, I produced the components I will use seperately. I produced a 2020 aluminium extrusion. These will create the two axes: the X-axis and the Y-axis. Then I created the V-Wheels that will glide along the rails. The V-Wheels were then nestled between two plates using 5mm spacers. On this plate, the X-axis will be attached. I repeated this combination for the Y-axis where the plates will be attached to the pen holder. I then created an assembly of both the X-axis and Y-axis. 
<img width="876" height="650" alt="image" src="https://github.com/user-attachments/assets/554adb8c-d271-4725-b48f-2d4c6d0467a9" />
<img width="208" height="236" alt="image" src="https://github.com/user-attachments/assets/03c0775b-2863-41ff-a61e-2f9c689bacbb" />
<img width="298" height="284" alt="image" src="https://github.com/user-attachments/assets/ca0bed33-709e-40f2-84bb-35b0892439d8" />
<img width="1093" height="567" alt="image" src="https://github.com/user-attachments/assets/c058f005-6d7f-4a78-98a2-c95afad3a420" />
<img width="1268" height="561" alt="image" src="https://github.com/user-attachments/assets/bc4c3a06-404b-45b4-9307-ceccf80e3cf7" />
<img width="1219" height="639" alt="image" src="https://github.com/user-attachments/assets/0e181f84-7235-44ac-826f-3a5eaa06292d" />
Once I had created the separate axes, I created the full assembly.
<img width="1057" height="461" alt="image" src="https://github.com/user-attachments/assets/e8138b61-7ab0-43b6-baba-bdadcb905f8d" />

Hours Spent: 6Hrs

## 11/12/25

I noticed that the V-Wheels were too deep within the extrusion so I had to recreate the separate axes assmeblies an then the full axes assembly.
<img width="814" height="545" alt="image" src="https://github.com/user-attachments/assets/1c0b7bcd-27ae-41ae-a974-d88a343f08f8" />
<img width="994" height="520" alt="image" src="https://github.com/user-attachments/assets/2664cbd2-881d-447f-a63a-2df63bff9a1e" />
<img width="806" height="462" alt="image" src="https://github.com/user-attachments/assets/9bc4ccad-4c9b-4e14-a3b6-bc75a83ae9b0" />
<img width="683" height="426" alt="image" src="https://github.com/user-attachments/assets/4ce4efd7-6249-44b7-b390-3771bbd4fdf2" />
<img width="1182" height="380" alt="image" src="https://github.com/user-attachments/assets/34911872-c684-4e42-a1be-2b0b1e292e2d" />
<img width="425" height="491" alt="image" src="https://github.com/user-attachments/assets/8cecc299-6d5d-4374-9cbe-6a9854f05bb6" />
<img width="662" height="426" alt="image" src="https://github.com/user-attachments/assets/131de40e-e6ff-4af8-b0b7-35ca3698560e" />

Hours Spent: 5Hrs
