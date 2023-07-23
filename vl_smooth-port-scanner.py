#!/usr/bin/env python3
import nmap
import re

def print_banner():
    print(r"""
    ____   ____      .__       .__            ____  __.
    \   \ /   /____  |__| _____|  |__ _____  |    |/ _|
     \   Y   /\__  \ |  |/  ___/  |  \\__  \ |      <  
      \     /  / __ \|  |\___ \|   Y  \/ __ \|    |  \ 
       \___/  (____  /__/____  >___|  (____  /____|__ \
                   \/        \/     \/     \/        \/
                   """)
    print("\n****************************************************************")
    print("\n* https://github.com/vaisx05                                   *")
    print("\n****************************************************************")

def get_valid_ip_address():
    ip_add_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    while True:
        ip_add_entered = input("\nPlease enter the IP address that you want to scan: ")
        if ip_add_pattern.search(ip_add_entered):
            print(f"{ip_add_entered} is a valid IP address")
            return ip_add_entered
        else:
            print("Invalid IP address format. Please try again.")

def get_valid_port_range():
    port_range_pattern = re.compile(r"(\d+)-(\d+)")
    port_min = 0
    port_max = 65535
    while True:
        port_range = input("Please enter the range of ports you want to scan (format: <int>-<int>, e.g., 60-120): ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            if 0 <= port_min <= port_max <= 65535:
                return port_min, port_max
        print("Invalid port range. Please try again.")

def scan_ports(ip_address, port_min, port_max):
    nm = nmap.PortScanner()
    open_ports = []
    for port in range(port_min, port_max + 1):
        try:
            result = nm.scan(ip_address, str(port))
            port_status = result['scan'][ip_address]['tcp'][port]['state']
            print(f"Port {port} is {port_status}")
            if port_status == 'open':
                open_ports.append(port)
        except Exception as e:
            print(f"Error while scanning port {port}: {str(e)}")
    
    return open_ports

def main():
    print_banner()
    ip_address = get_valid_ip_address()
    port_min, port_max = get_valid_port_range()
    open_ports = scan_ports(ip_address, port_min, port_max)
    print("Open ports:", open_ports)

if __name__ == "__main__":
    main()
