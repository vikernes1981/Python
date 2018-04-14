#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  ArduinoOut.py
#  
from bokeh.plotting import figure,output_file,show
import serial

serial_port = '/dev/ttyACM1'; # path of serial port
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
name_of_txt = "ArduinoOutput.txt"; # name of file to be created to store values

a = [] # counter list
b = [] # list that'll get file values
i = 0 # counter
ser = serial.Serial(serial_port, baud_rate)

while True:
	f = open(name_of_txt, "w+"); #open file to write
	while len(a) < 300:
		lines = ser.readline();
		lines = lines.decode("utf-8") #ser.readline returns a binary, convert to string
		a.append(i) # counter list
		f.write(lines);
		i += 1

	f.close() #close file if above code has looped 100 times

	if len(a) == 300: #if above code has looped 100 times...
		
		f = open(name_of_txt,'r') #...open file to read

		for linie in f:
			b.append(linie.strip()) #append file values in list
				
		plot = figure(plot_width=1200,plot_height=600,title="Light Sensor") # create plot
		plot.xaxis.axis_label = "Seconds" # x axis label
		plot.yaxis.axis_label = "Light Sensor Values" # y axis label
		plot.line([i for i in range(len(b))],b,line_width=1,color='red',alpha=0.5) # use list values to create the actual plot
		output_file("Scatter_plotting.html") # create html file to see the plot
		show(plot) # show plot on browser
		
	f.close() # close file

	while len(a) > 0 and len(b) > 0: # empty both a and b list
		a.pop()
		b.pop()
				
    i = 0 # counter is 0 again
