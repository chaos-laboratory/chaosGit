import serial
import time
import datetime
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
serial_port = '/dev/cu.usbmodem14301'
baud_rate = 115200
write_to_file_path= str(st) + 'testoutput.txt'

output_file = open(write_to_file_path, "w+");

ser = serial.Serial(serial_port, baud_rate)

while True:
	line = ser.readline();
	line = line.decode('utf-8');
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	tw = str(st)+line
	print(tw);
	output_file.write(tw);
