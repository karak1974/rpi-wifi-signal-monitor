# RPI Wi-Fi Signal Monitor  
Wi-Fi signal monitor for Rapsberry Pi

## Wiring  

|  GPIO  | Resistor |  LED |
| ------ | -------- | ---- |
| GPIO18 |   1kOHM  | LED1 |
| GPIO23 |   1kOHM  | LED2 |
| GPIO24 |   1kOHM  | LED3 |
| GPIO25 |   1kOHM  | LED4 |

Every resistor is connected to the negative rail on the breadboard.  
The rail is connected directly to the GND.  

## Using  
On the Raspberry Pi go to the `src` folder and run `python3 wifi_signal_monitor.py`  
It works now and show Wi-Fi signal strength with 4 LED
