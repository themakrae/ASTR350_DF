# ASTR 350 - Phase Delay

The files in this repository are drafts of Python scripts for calculating the phase delay between two RTL-SDR channels in an attempt to create a multi-channel direction finding system. 

`identify_index.py` - This script identifies the index values of all of the detected RTL-SDR dongles. Knowing these values allows you to work with more than one dongle.

`sdr_1_data.py` - This script collects data from one of the connected RTL-SDR dongles and stores it in a CSV file of the same name.

`sdr_2_data.py` - This script serves the same function as above but for the second dongle. The scripts are identical with the exception of the dongle number. 

**Note: Regardless of the number of dongles you are working with, all of the data collection scripts must be run *in parallel*. This can be done through the following example command:**

  python script1.py &
  python script2.py &

`phase_delay_calc.py` - This script uses concepts from the Multi-RTL block and other correlation techniques to calculate the phase delay between receivers. It takes in the data CSV files as an input and outputs the phase delay values from throughout the data collection period.

## Installations

All that is needed to run these scripts is `pyrtlsdr`, which is a Python wrapper for working with SDR dongles. `librtlsdr` is a dependency. 
