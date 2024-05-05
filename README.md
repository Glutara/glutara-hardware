<br>
<div align="center">
    <div >
        <img height="150px" src="https://firebasestorage.googleapis.com/v0/b/upheld-acumen-420202.appspot.com/o/readme-assets%2FGlutara.png?alt=media&token=77d4dd88-6cca-4e4d-94f2-321124c20a61" alt=""/>
    </div>
    <div>
            <h3><b>Glutara</b></h3>
            <p><i>A Key to Your Diabetes Journey</i></p>
    </div>      
</div>
<br>
<h1 align="center">Glutara Hardware</h1>

The beating heart: This repository houses the hardware blueprints for the Arduino and ESP32 devices that power Glutara, serving as the vital link between sensor data and the cloud, enabling real-time monitoring and seamless data exchange. This repository code development is based on [this reference](https://github.com/oxullo/Arduino-MAX30100).

## 👨🏻‍💻 &nbsp;Technology Stack

<div align="center">

<a href="https://www.arduino.cc/">
<kbd>
<img src="https://firebasestorage.googleapis.com/v0/b/upheld-acumen-420202.appspot.com/o/readme-assets%2Ficons%2FArduino.png?alt=media&token=534f1f06-02bc-42ef-a8c8-6bfbb612142f" height="60" />
</kbd>
</a>

<a href="https://www.espressif.com/en/products/socs/esp32">
<kbd>
<img src="https://firebasestorage.googleapis.com/v0/b/upheld-acumen-420202.appspot.com/o/readme-assets%2Ficons%2FESP32.png?alt=media&token=908b5047-2893-4785-bb5a-acb1d5aa7ab4" height="60" />
</kbd>
</a>

</div>
<div align="center">
<h4>Arduino | ESP32</h4>
</div>

## Getting Started
Make sure you already have these components before following the 'how to run' steps
1. MAX30100 Sensor Arduino
2. Install Arduino IDE on your computer
3. Appropriate board (e.g., ESP32)
4. USB Cable

## ⚙️ &nbsp;How to Run
Clone this repository from terminal using this following command
``` bash
$ git clone https://github.com/Glutara/glutara-hardware.git
```

### Hardware Setup
1. **Sensor Connection**:
   - Connect the MAX30100 sensor to an Arduino board (e.g., ESP32). Ensure the VCC, GND, SDA, and SCL pins of the sensor are correctly connected to the corresponding pins on the Arduino.
2. **Computer Connection**:
   - Connect the Arduino board to your computer via a USB cable.

### Hardware Setup
1. **Arduino IDE**:
   - Install the Arduino IDE if it is not already installed on your computer.
2. **Library Installation**:
   - Install the `MAX30100_PulseOximeter` library via the Library Manager in the Arduino IDE or download it from GitHub if available.

### Uploading the Code
1. **Open the Sketch**:
   - Open the `MAX30100_Debug.ino` file in the Arduino IDE.
2. **Board and Port Selection**:
   - Select the appropriate board (e.g., ESP32) and the correct port in the Arduino IDE.
3. **Upload**:
   - Upload the code to the Arduino by clicking the "Upload" button in the Arduino IDE.

## Monitoring the Output
1. **Open Serial Monitor**:
   - Open the Serial Monitor in the Arduino IDE after the code has been successfully uploaded.
2. **Set Baud Rate**:
   - Set the baud rate of the Serial Monitor to 115200 bps to match the configuration in the code (`Serial.begin(115200);`).

## Saving Data to CSV

1. **Serial Data Logging**:
   - Data will be displayed on the Serial Monitor at specified intervals (e.g., every 1000 ms).

2. **Python Script for CSV**:
   - Use a Python script with the pyserial library to read data from the Serial Monitor and write it to a CSV file. Here is an example script:

   ```python
   import serial
   import csv
   import time

   ser = serial.Serial('COM_PORT', 115200)  # Replace 'COM_PORT' with the appropriate COM port
   with open('data.csv', 'w', newline='') as file:
       writer = csv.writer(file)
       while True:
           line = ser.readline().decode('utf-8').rstrip()
           if line.startswith('H:') or line.startswith('O:'):
               writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), line])
    ```
    You can also use available python scripts [here](https://github.com/Glutara/glutara-hardware/blob/main/Serread.py).
    
## 🛠️ &nbsp;Hardware Development Documentation
<img src="https://firebasestorage.googleapis.com/v0/b/upheld-acumen-420202.appspot.com/o/readme-assets%2Fhardware%2FHardware2.jpg?alt=media&token=9f3f8a0e-ac2a-4fea-b056-4f7ce8de673e" />

> Arduino MAX30100

<img src="https://firebasestorage.googleapis.com/v0/b/upheld-acumen-420202.appspot.com/o/readme-assets%2Fhardware%2FHardware1.jpg?alt=media&token=6139d7d4-a231-4970-acd9-9d8d70cbd6ff" />

> Under Development Board


## 👥 &nbsp;Contributors

| <a href="https://github.com/mikeleo03"><img width="180px" height="180px" src="https://firebasestorage.googleapis.com/v0/b/upheld-acumen-420202.appspot.com/o/readme-assets%2Fpicprof%2FLeon.png?alt=media&token=0ea1884a-32ca-471b-a3af-bf3995bbc605" alt=""/></a> | <a href="https://github.com/GoDillonAudris512"><img width="180px" height="180px" src="https://firebasestorage.googleapis.com/v0/b/upheld-acumen-420202.appspot.com/o/readme-assets%2Fpicprof%2FDillon.png?alt=media&token=bc76cc6b-5606-4351-8472-9c243c8b9da3" alt=""/></a> | <a href="https://github.com/margarethaolivia"><img width="180px" height="180px" src="https://firebasestorage.googleapis.com/v0/b/upheld-acumen-420202.appspot.com/o/readme-assets%2Fpicprof%2FOlivia.png?alt=media&token=d53f9cfd-e1e1-41b6-a28c-440904df29b8" alt=""/></a> | <a href="https://github.com/AustinPardosi"><img width="180px" height="180px" src="https://firebasestorage.googleapis.com/v0/b/upheld-acumen-420202.appspot.com/o/readme-assets%2Fpicprof%2FAustin.png?alt=media&token=f520a334-4aeb-4efe-9437-669451b6dca6" alt=""/></a> |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <div align="center"><h3><b><a href="https://github.com/mikeleo03">Michael Leon Putra Widhi</a></b></h3><i><p>Bandung Institute of Technology</i></p></div>                                                                               | <div align="center"><h3><b><a href="https://github.com/GoDillonAudris512">Go Dillon Audris</a></b></h3></a><p><i>Bandung Institute of Technology</i></p></div>                                                                          | <div align="center"><h3><b><a href="https://github.com/margarethaolivia">Margaretha Olivia Haryono</a></b></h3></a><p><i>Bandung Institute of Technology</i></p></div>                                                               | <div align="center"><h3><b><a href="https://github.com/AustinPardosi">Austin Gabriel Pardosi</a></b></h3></a><p><i>Bandung Institute of Technology</i></p></div>                                                                            |
