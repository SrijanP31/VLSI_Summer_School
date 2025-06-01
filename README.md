# VLSI Summer School '25

Circuits designed as part of VLSI Summer School '25, conducted by IIT KGP. All circuits are designed using University of Minnesota's 65nm bulk Predictive Transistor Model(PTM)\
<u>Software used</u>: LTSpice

## Setup required

1. Install [LTSpice](https://www.analog.com/en/resources/design-tools-and-calculators/ltspice-simulator.html)
2. Download the '65nm_bulk.pm' file from [University of Minnesota](https://mec.umn.edu/ptm)
3. Change the file extension from ```'.pm'``` to ```'.mos'``` and save it in ```C:\Users\<user_name>\AppData\Local\LTspice\lib\cmp```. (or wherever LTSpice stores your models and subcircuits)
4. To run these files, in the ```'65nm_bulk.mos'``` file, change the names of the models from ```NMOS``` to ```n_65``` and ```PMOS``` to ```p_65.``` 

## Circuits designed

1. CMOS Inverter
2. 3T Active Pixel Sensor(APS)
3. 4T Active Pixel Sensor(APS)
4. Single-ended Cascode Amplifier with wide-swing current mirror biasing.
5. Current Transimpedance Amplifer(CTIA)
