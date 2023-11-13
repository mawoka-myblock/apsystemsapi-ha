# APsystems API for EZ1-M
Getting the data of the inverter using APsystem's cloud

## Installation
Add this integration using Hacs by clicking on the three dots in the upper right corner and clicking "Add custom repository".

## Configuration
Just add the following to your config file.
```yaml
sensor:
  - platform: apsystemsapi
    username: YOUR_USERNAME
    password: YOUR_PASSWORD
```
