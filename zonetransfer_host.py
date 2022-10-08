#!/usr/bin/env python3
import os

domain = input("Please input a domain name: ")

NS_file = os.system("host -t NS " + domain + " | awk '{print $4}' | sed 's/\.$//' > " + domain + "_NS.txt")

f = open((domain + "_NS.txt"), "r")

for line in f:
	print("")
	print("#" * 50)
	print("")
	print("Attempting zone transfer for " + line)
	print("#" * 50)
	os.system("host -l " + domain + " " + line)
	
	
