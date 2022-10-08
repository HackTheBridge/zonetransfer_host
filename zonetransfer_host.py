#!/usr/bin/env python3
import os

domain = input("Please input a domain name: ")

# Creates a file of identified name servers to read from.
NS_file = os.system("host -t NS " + domain + " | awk '{print $4}' | sed 's/\.$//' > " + domain + "_NS.txt")

# Reads the file line by line and attempts a zone transfer for each nameserver.
f = open((domain + "_NS.txt"), "r")
for line in f:
	print("")
	print("#" * 50)
	print("")
	print("Attempting zone transfer for " + line)
	print("#" * 50)
	os.system("host -l " + domain + " " + line)
f.close()
	
	
