# CNC-Pen-Plotter
A Computer Numerical Controlled machine that translates G-code to drawings on paper by moving a pen along the X and y axes

## Why I chose this project?
I chose to build a CNC pen plotter because it combines electronics and mechanical movement while also helping me develop my PCB and CAD design.
## Schematic
<img width="787" height="644" alt="image" src="https://github.com/user-attachments/assets/4fe346d2-c5bc-400e-a42f-20d36ca39cc2" />

## PCB
<img width="1205" height="695" alt="image" src="https://github.com/user-attachments/assets/f3cbb9aa-34ab-4ee7-8bf7-470b3672640a" />
<img width="771" height="453" alt="image" src="https://github.com/user-attachments/assets/2df1d783-fb18-4251-a103-8d8d0b9d67cd" />
<img width="937" height="554" alt="image" src="https://github.com/user-attachments/assets/e9776357-497e-4d15-bf22-9e98d13b9967" />

## 3D Model
<img width="1132" height="603" alt="image" src="https://github.com/user-attachments/assets/d47aa933-9022-49a3-a46f-66504452860d" />
<img width="1339" height="573" alt="image" src="https://github.com/user-attachments/assets/d96e7a8f-1e7a-4609-bb0d-ec2b6953af48" />
<img width="1010" height="373" alt="image" src="https://github.com/user-attachments/assets/61528976-96bc-4e75-b564-0524bc1cf8ff" />
<img width="943" height="463" alt="image" src="https://github.com/user-attachments/assets/114b8d8d-8373-4513-9f1c-72718bba651a" />
<img width="890" height="770" alt="image" src="https://github.com/user-attachments/assets/86e1dbd9-e65d-4708-9ce8-ad0e08e5af04" />

## BOM
| Item                       | Qty (Project) | Packs | Unit Price (£) | Total (£) | Link                                                                               |
| -------------------------- | ------------- | ----- | -------------- | --------- | ---------------------------------------------------------------------------------- |
| 600mm Aluminium Extrusion  | 3             | 1     | 11.85          | 47.37     | [Al extrusion 600mm (4pcs)](https://www.aliexpress.com/item/1005007282374511.html) |
| V Wheels                   | 12            | 1     | 0.44           | 10.54     | [V Wheels set (24pcs)](https://www.aliexpress.com/item/1005004275676552.html)      |
| Limit Switches             | 4             | 1     | 0.30           | 1.48      | [Limit switches (5pcs)](https://www.aliexpress.com/item/1005001834200980.html)     |
| NEMA 17 Stepper Motor      | 2             | 1     | 7.18           | 21.53     | [NEMA 17](https://www.aliexpress.com/item/1005005067991574.html)                   |
| Timing Belt 6mm            | 3m            | 1     | 4.14           | 4.14      | [Timing belt 6mm](https://www.aliexpress.com/item/32921042288.html)                |
| Belt Pulley                | 2             | 1     | 1.00           | 5.00      | [Belt pulley](https://www.aliexpress.com/item/1005010636842055.html)               |
| Belt Idler                 | 2             | 1     | 2.40           | 4.79      | [Idler pulley](https://www.aliexpress.com/item/1005008518751026.html)              |
| ESP32 DevKit v1 (30-pin)   | 1             | 1     | 3.88           | 3.88      | [ESP32 DevKit](https://www.aliexpress.com/item/1005006140560853.html)              |
| A4988 Motor Driver         | 2             | 2     | 1.17           | 2.34      | [A4988](https://www.aliexpress.com/item/1005009489182283.html)                     |
| JST XH 3-pin Connectors    | 2             | 1     | 0.10           | 1.02      | [JST 3-pin (10pcs)](https://www.aliexpress.com/item/1005007080333485.html)         |
| JST XH 4-pin Connectors    | 2             | 1     | 0.12           | 1.23      | [JST 4-pin (10pcs)](https://www.aliexpress.com/item/1005007080333485.html)         |
| JST Wire Connectors        | 2             | 1     | 0.15           | 1.48      | [JST wire set](https://www.aliexpress.com/item/1005009245405182.html)              |
| 8-pin Socket               | 4             | 1     | 0.10           | 1.02      | [8-pin socket (10pcs)](https://www.aliexpress.com/item/4001198421663.html)         |
| DC Barrel Jack (5.5×2.1mm) | 1             | 1     | 0.12           | 1.21      | [DC barrel jack](https://www.aliexpress.com/item/1005001688314286.html)            |
| 7805 Voltage Regulator     | 1             | 1     | 0.10           | 1.04      | [7805 5V](https://www.aliexpress.com/item/1005010018816049.html)                   |
| 100µF Capacitor            | 3             | 1     | 0.10           | 2.08      | [100µF capacitor](https://www.aliexpress.com/item/4001044838305.html)              |
| 1µF Capacitor              | 1             | 1     | 0.12           | 2.34      | [1µF capacitor](https://www.aliexpress.com/item/1005005665288337.html)             |
| 15-pin Socket              | 2             | 1     | 0.12           | 1.24      | [15-pin socket](https://www.aliexpress.com/item/4001198421663.html)                |
| Breakaway Pin Headers      | 10            | 1     | 0.34           | 3.39      | [Pin headers](https://www.aliexpress.com/item/1005007564228387.html)               |
| 12V 3A Power Supply        | 1             | 1     | 4.51           | 4.51      | [12V 3A PSU](https://www.aliexpress.com/item/4000494270389.html)                   |
| SG90 Servo                 | 1             | 1     | 1.23           | 1.23      | [SG90 servo](https://www.aliexpress.com/item/1005006501322490.html)                |
| 5mm × 45mm Shaft           | 2             | 1     | 0.37           | 2.59      | [5mm shaft](https://www.aliexpress.com/item/1005007023343232.html)                 |
| 10mm Spring (ID 5mm)       | 2             | 1     | 0.10           | 1.04      | [10mm spring](https://www.aliexpress.com/item/1005009966338820.html)               |
| M5 Spacer (6mm)            | 25            | 3     | 0.04           | 1.14      | [M5 spacer](https://www.aliexpress.com/item/1005005477773699.html)                 |
| M5 Sliding Nuts            | 12            | 1     | 0.09           | 1.79      | [M5 sliding nuts](https://www.aliexpress.com/item/32859918655.html)                |
| PCB                        | -             | -     |  -             | 5.00      |                                                                                    |
| AliExpress Shipping        | -             | -     |  -             | 17.86     |                                                                                    |
|TOTAL                                       | GBP 185.03             | USD 251.73                                                                                     |
