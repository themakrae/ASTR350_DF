from rtlsdr import RtlSdr
from scipy import signal as sgn
import csv
import numpy as np

# Read in sdr1 data
with open('/home/pi/work/sdr_1_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    sdr_1_data = row[0]

# Read in sdr2 data
with open('/home/pi/work/sdr_2_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    sdr_2_data = row[0]
    
# Declarations
phase_delays = []
num_samp = len(sdr_1_data)/512
x = 0

# Calculate correlation and delay in data
for i in range(num_samp):
    sdr_1 = sdr_1_data[x:512+x]
    sdr_2 = sdr_2_data[x:512+x]
    correlation = sgn.correlate(sdr_1-np.mean(sdr_1), sdr_2 - np.mean(sdr_2), mode="full")
    delays = sgn.correlation_lags(len(sdr_1), len(sdr_2), mode="full")
    delay = delays[np.argmax(abs(correlation))]
    phase_delays.append(delay)
    x+=512

# Create and write data to file
with open('phase_delays.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(phase_delays)