from rtlsdr import RtlSdr
import csv

# Replace index value with respective dongle's index
sdr_1 = RtlSdr()

# Change parameters as desired
sdr_1.sample_rate = 240000 #Hz
sdr_1.center_freq = 90.9e6 #Hz
sdr_1.freq_correction = 60 #PPM
sdr_1.gain = 10

# Change path to where you want the CSV file located
with open('sdr_1_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(sdr_1.read_samples(512))
