#!/usr/bin/env python3

import os


print("""\

 █████   █████          ████             █████     ███  ████   ███   █████              
░░███   ░░███          ░░███            ░░███     ░░░  ░░███  ░░░   ░░███               
 ░███    ░███   ██████  ░███   ██████   ███████   ████  ░███  ████  ███████   █████ ████
 ░███    ░███  ███░░███ ░███  ░░░░░███ ░░░███░   ░░███  ░███ ░░███ ░░░███░   ░░███ ░███ 
 ░░███   ███  ░███ ░███ ░███   ███████   ░███     ░███  ░███  ░███   ░███     ░███ ░███ 
  ░░░█████░   ░███ ░███ ░███  ███░░███   ░███ ███ ░███  ░███  ░███   ░███ ███ ░███ ░███ 
	░░███     ░░██████  █████░░████████  ░░█████  █████ █████ █████  ░░█████  ░░███████ 
	 ░░░       ░░░░░░  ░░░░░  ░░░░░░░░    ░░░░░  ░░░░░ ░░░░░ ░░░░░    ░░░░░    ░░░░░███ 
																			   ███ ░███ 
																			  ░░██████  
																			   ░░░░░░   
						   █████████                                                    
						  ███░░░░░███                                                   
						 ███     ░░░  █████ ████ ████████  █████ ████                   
						░███         ░░███ ░███ ░░███░░███░░███ ░███                    
						░███    █████ ░███ ░███  ░███ ░░░  ░███ ░███                    
						░░███  ░░███  ░███ ░███  ░███      ░███ ░███                    
						 ░░█████████  ░░████████ █████     ░░████████                   
						  ░░░░░░░░░    ░░░░░░░░ ░░░░░       ░░░░░░░░                    
																						
																						
																	  

""")



pcap = input("Path to memory: ");
print(pcap)

print("1. Install ")

command = input("Select Option:");


if command == "1":
	os.system('sudo apt update && sudo apt install -y docker.io && sudo systemctl enable docker --now && sudo usermod -aG docker $USER')
	os.system('docker pull phocean/volatility')
	os.system('echo \'\nfunction volatility() {\n\tdocker run --rm --user=$(id -u):$(id -g) -v "$(pwd)":/dumps:ro,Z -ti phocean/volatility $@\n}\' >> ~/.zshrc')
	
	
	
	
	
