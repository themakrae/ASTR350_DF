from rtlsdr import RtlSdr
import csv

sdr_1 = RtlSdr()

sdr_1.sample_rate = 240000 #Hz
sdr_1.center_freq = 90.9e6 #Hz
sdr_1.freq_correction = 60 #PPM
sdr_1.gain = 10

with open('/home/pi/work/sdr_1_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(sdr_1.read_samples(512))