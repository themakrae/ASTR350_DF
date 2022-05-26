from rtlsdr import RtlSdr
import csv

sdr_2 = RtlSdr()

sdr_2.sample_rate = 240000 #Hz
sdr_2.center_freq = 90.9e6 #Hz
sdr_2.freq_correction = 60 #PPM
sdr_2.gain = 10

with open('/home/pi/work/sdr_2_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(sdr_2.read_samples(512))