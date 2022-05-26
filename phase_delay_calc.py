from rtlsdr import RtlSdr
import csv

# Read in sdr1 data
with open('/home/pi/work/sdr_1_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    sdr_1_data = row[0]

# Read in sdr2 data
with open('/home/pi/work/sdr_2_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    sdr_2_data = row[0]
    
(angle(self.phase_amplitude_corrections[chan])/pi*180)