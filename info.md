### Set up only when the device is online!!!

## Setup
1. **ensure that the device is online** and download this integration.
2. Add the following to your `configuration.yaml`:
```yaml
sensor:
  - platform: apsystemsapi
    username: YOUR_USERNAME
    password: YOUR_PASSWORD
```
3. Restart Home Assistant

## Usage
Under `devices` -> `entities` you can search for "apsystems" and 2 entities should show up: "APsystems Solar Power" and "APsystems Solar All-Time Production".
The first one returns the current (as in time) production of the inverter and the second one keeps track of the amount produced since it was connected to the cloud. 

Note: The all-time sensor just pulls the data from the cloud and doesn't store it locally.

### Energy Dashboard
The "APsystems Solar All-Time Production" can be used as a sensor for the solar production in the **Energy dashboard**.
You can ignore the warning (If you know how to get rid of it, please open an issue)