from rtlsdr import RtlSdr

# List of detected device serial numbers 
serial_numbers = RtlSdr.get_device_serial_addresses()

# Find device index for given serial number
device_index = RtlSdr.get_device_index_by_seril('0000001')

print(serial_numbers)
print(device_index)