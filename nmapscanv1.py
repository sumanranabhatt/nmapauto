#!/usr/bin/python3

import subprocess
import sys
import os.path
from colorama import Fore, Back, Style
#import pathlib

def bash(command):
	return	subprocess.check_output(['bash','-c',command])

def nmap_scan(ip):
	print("\nNORMAL SCAN")
	print("scanning TCP port on %s" %ip)
        ports=bash("nmap -p- -Pn --min-rate=1000 -T4 %s | grep ^[0-9] | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//"%ip)
	print('Open ports are $ports :'+ports)
#	print(path)
	try:
		res = bash('nmap -T4 -sV -Pn  -sC -p%s %s --min-rate 10000 -oA %s+vuln '%(ports,ip,ip))
		print(res)
	except Exception:
		pass
		
def nmap_scanv(ip):
	print("\nVULNERABLE SCAN")
	print("scanning TCP port on %s" %ip)
        ports=bash("nmap -p- -Pn --min-rate=1000 -T4 %s | grep ^[0-9] | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//"%ip)
	print('Open ports are $ports :'+ports)
#	print(path)
	try:
		res = bash('nmap -T4 -sV -Pn --script vuln -sC -p%s %s --min-rate 10000 -oA %s+vuln'%(ports,ip,ip))
		print(res)
	except Exception:
		pass
	
#result = subprocess.check_output(['bash', '-c' ,'ifconfig | grep "broadcast"'])
#result = 'suman'
#print(result)
print(Fore.RED +"\n1.Enter the Target IP range")
print(Fore.GREEN+"2.Enter the Filename containing the Target IPs")


choice = input(Fore.BLUE+"Choose the type of input you want to provide? : " )
print(choice)

print(Fore.GREEN+"\nDo you want a Normal Scan of vulnerable(--script vuln) scan?")
print(Fore.BLUE+"1.Normal Scan"+Fore.RED+"\n2.Vulnerable Scan")
print(Style.RESET_ALL)
Stype=input()
if(choice == 1):
	ips=raw_input("\nEnter the Range of ip : ")
	print('your ip range is : '+ips)
	out=bash('nmap -sn %s -n --min-rate 10000 -T4 | grep "report" | cut -d " " -f5'%ips).splitlines()
elif(choice ==2 ):
	fname=raw_input(Style.DIM+'\nEnter the filename : ')
	with open(fname) as f:
	 out=f.read().splitlines()
else:
	print("Invalid Input,Fuck off")
	exit()
	
	
#directory='/home/kali/'
#path=directory + raw_input('Enter the path to save the output : ')
#print(path)


#print(out)
#with open(fname, 'a') as sys.stdout:
 #   print(out)
    
#nextstep = out.splitlines()
#print(nextstep)



#print(lines.splitlines())
print(out)

for i in range(0, len(out)):
	ip = out[i]
	print(ip)
	

if(Stype==1):
   for i in range(0, len(out)):
	nmap_scan(out[i])
elif(Stype==2):
   for i in range(0, len(out)):
	nmap_scanv(out[i])
else:
   print("Error in the scan type input")
   exit()

