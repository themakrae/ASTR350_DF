from rtlsdr import RtlSdr
import csv

# Replace index value with respective dongle's index
sdr_2 = RtlSdr()

# Change parameters as desired
sdr_2.sample_rate = 240000 #Hz
sdr_2.center_freq = 90.9e6 #Hz
sdr_2.freq_correction = 60 #PPM
sdr_2.gain = 10

# Change path to where you want the CSV file located
with open('sdr_2_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(sdr_2.read_samples(512))
