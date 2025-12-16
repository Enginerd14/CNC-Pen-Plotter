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

I began producing a rough design of the outcome in Solidworks. First, I produced the components I will use seperately. I produced a 2020 aluminium extrusion. These will create the two axes: the X-axis and the Y-axis. Then I found 3D models of the V-Wheels that will glide along the rails. The V-Wheels were then nestled between two plates using 5mm spacers. On this plate, the X-axis will be attached. I repeated this combination for the Y-axis where the plates will be attached to the pen holder. I then created an assembly of both the X-axis and Y-axis. 
<img width="876" height="650" alt="image" src="https://github.com/user-attachments/assets/554adb8c-d271-4725-b48f-2d4c6d0467a9" />
<img width="208" height="236" alt="image" src="https://github.com/user-attachments/assets/03c0775b-2863-41ff-a61e-2f9c689bacbb" />
<img width="298" height="284" alt="image" src="https://github.com/user-attachments/assets/ca0bed33-709e-40f2-84bb-35b0892439d8" />
<img width="1093" height="567" alt="image" src="https://github.com/user-attachments/assets/c058f005-6d7f-4a78-98a2-c95afad3a420" />
<img width="1268" height="561" alt="image" src="https://github.com/user-attachments/assets/bc4c3a06-404b-45b4-9307-ceccf80e3cf7" />
<img width="1219" height="639" alt="image" src="https://github.com/user-attachments/assets/0e181f84-7235-44ac-826f-3a5eaa06292d" />
Once I had created the separate axes, I created the full assembly. I created Sliding nuts to fix the componets onto the aluminium extrusion.
<img width="961" height="580" alt="image" src="https://github.com/user-attachments/assets/1b1e0352-2e7c-4315-8906-c0593c5b5438" />
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

## 12/12/25

I found 3D models of the NEMA 17 motors and the Pulley and Idlers used. I created bases for the Y axis extrusion to sit on and the mechanical componets to attach to. 
<img width="498" height="468" alt="image" src="https://github.com/user-attachments/assets/f8f0a9a6-0666-4f3f-8611-249aaf96d2a7" />
<img width="390" height="350" alt="image" src="https://github.com/user-attachments/assets/6c3e3aac-0303-4d13-8d75-20750ce831dc" />
<img width="519" height="451" alt="image" src="https://github.com/user-attachments/assets/684b2550-76ea-4ed6-b073-021d56cc262f" />
<img width="648" height="495" alt="image" src="https://github.com/user-attachments/assets/192da798-2705-4fad-8ea4-a67a4f976757" />
<img width="764" height="583" alt="image" src="https://github.com/user-attachments/assets/f5697040-69e7-4b76-89ca-8b2bfd2afb8e" />


Hours Spent: 4.5Hrs

## 13/12/25

I began creating the plates to connect the motor and pulley system to the X axis.
<img width="717" height="293" alt="image" src="https://github.com/user-attachments/assets/ec235bb0-a282-4061-aeef-665ef8aa3f0d" />
<img width="709" height="240" alt="image" src="https://github.com/user-attachments/assets/02ee5108-a7b0-41ee-b11c-508d55d90a1d" />

Hours Spent: 3Hrs

## 14/12/25

Today, I began assembling the entire project. 
<img width="911" height="542" alt="image" src="https://github.com/user-attachments/assets/60ef3d5a-e08a-4f69-8b93-4fc67ff1f45d" />
<img width="843" height="441" alt="image" src="https://github.com/user-attachments/assets/112b69cb-90ac-4896-92cc-98800abe2501" />
<img width="738" height="807" alt="image" src="https://github.com/user-attachments/assets/22b30b95-aaab-4edd-b66a-a0b6b9168a8a" />

Hours Spent: 6.5Hrs

## 15/12/25

I added in Limit switches and began thinking abot the design of the Pen holder. 
<img width="1056" height="786" alt="image" src="https://github.com/user-attachments/assets/0b0d29a7-fa4b-474e-bde2-5964c7915e10" />
<img width="551" height="470" alt="image" src="https://github.com/user-attachments/assets/21d379b3-7d4b-4670-8fac-ef01f689bf17" />


Hours Spent: 2.5Hrs

## 16/12/25

I created the different parts of the Pen holder mechanism. I decided that I would make it attachable to the existing plate on the X-axis.
- Existing Plate <img width="931" height="810" alt="image" src="https://github.com/user-attachments/assets/6412d1bb-7c07-491d-8f38-068767899ff1" />
  
- Pen Holder <img width="616" height="537" alt="image" src="https://github.com/user-attachments/assets/ff65d8aa-e382-477d-8316-c3aa1590e42f" /> 
  
- Pen holder Guide <img width="626" height="758" alt="image" src="https://github.com/user-attachments/assets/3e91de73-a8c9-40d6-bcb7-2ae935f46519" />
  
- shaft pen holder will glide along <img width="181" height="397" alt="image" src="https://github.com/user-attachments/assets/59e8377a-538d-41cd-8cf5-20194ad89944" />
  
- Full Assembly with servo motor <img width="828" height="705" alt="image" src="https://github.com/user-attachments/assets/ddb77105-e679-47f1-ad94-ad995f07c972" />
  
- Attached to axis <img width="1104" height="807" alt="image" src="https://github.com/user-attachments/assets/b0101cce-9ead-4e88-a48f-fe5e6cc2c015" />

- Full Model so far <img width="1232" height="599" alt="image" src="https://github.com/user-attachments/assets/c4fd88d9-c4a5-4c5e-961e-4a32292a8b0d" />
  <img width="1364" height="609" alt="image" src="https://github.com/user-attachments/assets/f835b6bf-841a-4a76-88d2-50c1b3bf3e9e" />

Hours Spent: 6Hrs
