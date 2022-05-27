from rtlsdr import RtlSdr
from gnuradio import blocks
from threading import Lock
from gnuradio import gr
from gnuradio.filter import firdes
from grc_gnuradio import blks2
from pylab import *
from math import log,ceil
from scipy import signal as sgn
import csv
import numpy as np
import osmosdr
import time
import multi_rtl
import threading

# Read in sdr1 data
with open('/home/pi/work/sdr_1_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    sdr_1_data = row[0]

# Read in sdr2 data
with open('/home/pi/work/sdr_2_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    sdr_2_data = row[0]
    
# Declare phase delay list
phase_delays = []

# Calculate correlation and delay in data
for i in sdr_1_data:
    index = sdr_1_data.index(i)
    sdr_1 = sdr_1_data[index]
    sdr_2 = sdr_2_data[index]
    correlation = sgn.correlate(sdr_1-np.mean(sdr_1), sdr_2 - np.mean(sdr_2), mode="full")
    delays = sgn.correlation_lags(len(sdr_1), len(sdr_2), mode="full")
    delay = delays[np.argmax(abs(correlation))]
    phase_delays.append(delay)

# Create and write data to file
with open('phase_delays.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(phase_delays)