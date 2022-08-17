import serial
from serial.tools import list_ports

device_list = list_ports.comports()

for x in device_list:
	if x.pid == 60441 and x.vid == 1240:
		print(x.product)
		ser = serial.Serial(x.device, 115200)
		r = ser.read(26)
		
		print("Packet Header: \t", 'Valid' if (r[0] + r[1]) == 20 else 'Invalid')       # Should be 20 or 0x0a0a
		print("Packet Footer: \t", 'Valid' if (r[24] + r[25]) == 22 else 'Invalid')     # Should be 22 or 0x0b0b

		sensor_types = {1: 'UV Sensor', 4: 'Conductivity Sensor', 6: 'Air Quality Sensor', 7: 'Humidity Sensor', 9: 'Temperature Sensor', 11: 'UV Sensor', 10: 'Heartrate Sensor'}
		print("Sensor Type: \t", sensor_types[r[2]])

		if r[2] == 1:
			pass
		elif r[2] == 4:
			pass
		elif r[2] == 6:
			pass
		elif r[2] == 7:
			print((r[6] | (r[7] << 8)) / 100)
		elif r[2] == 9:
			pass
		elif r[2] == 11:
			pass
		elif r[2] == 10:
			for i in range(6, 23, 1):
				print(r[i])
		
		
