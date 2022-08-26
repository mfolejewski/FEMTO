Femto - Raspberry Pi RP2040 12x12mm PCB module

Femto is a ultra compact Raspberry Pi RP2040 module, which has features, as following:
- small footprint 12x12mm,
- all 30 GPIO pins connected,
- stamp form factor,
- 4-layer PCB board,
- onboard: QSPI Flash (USON8 package), 12MHz oscillator, PWR LED,
- fully open source project (OSHW).

Here you can find:
- \Photos: a few pictures of the assembled PCB boards
- \Python: simple script do test Femto module using Femto Tester board (use Thonny IDE)
- \manufacturing_files: all the production files for ordering PCB and assembly at JLCPCB (Gerber files, Pick & Place, BOM, etc.)
- \source_files: source files in Kicad and Altium Designer format

The main goal and reason to create this project was attempt to design as smallest as possible, and fully functional RP2040 module. Please note, that RP2040 MCU nas 7x7mm package, and Femto module has only a bit more, 12x12mm. In comparision, closer competitiors, such as Raspberry Pi Pico or RP2040 Stamp (Solder Party) have appropriately 51x21mm and 25x25mm.

The project consists of 3 parts:
- Module (mainboard)
- frame (solder frame)
- tester (testbench, only for functional verification)

Project published as Open Source Hardware (OSHW) under CERN OHL v1.2 (Open Hardware Licence).

![Screenshot](oshw_facts.png)

Raspberry Pico and Femto Module v1:
![Screenshot](Photos/Femto_Module_Raspberry_Pico_01.png)

Femto Module:
![Screenshot](Photos/Femto_module_06.png)

Femto Frame:
![Screenshot](Photos/Femto_frame_01.png)

Femto Tester:
![Screenshot](Photos/Femto_tester_05.png)
