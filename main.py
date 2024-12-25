import requests
import sys
from colorama import Fore, Style, init
init(autoreset=True)
def display_logo():
    logo = f"""
{Fore.CYAN}*********************************************
*{Fore.GREEN}         IP TRACKER TOOL                   {Fore.CYAN}*
*{Fore.YELLOW}         Instagram: {Fore.MAGENTA}@x0jb | @amiinee.bou{Fore.YELLOW}   {Fore.CYAN}*
{Fore.CYAN}*********************************************
"""
    print(logo)

def get_ip_info(ip=None):
    try:
        url = f"https://ipinfo.io/{ip if ip else ''}/json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "IP": data.get("ip", "N/A"),
                "Hostname": data.get("hostname", "N/A"),
                "City": data.get("city", "N/A"),
                "Region": data.get("region", "N/A"),
                "Country": data.get("country", "N/A"),
                "Location": data.get("loc", "N/A"),
                "Organization": data.get("org", "N/A"),
                "Postal Code": data.get("postal", "N/A"),
            }
        else:
            print(f"{Fore.RED}Error: Unable to fetch information. Please check the IP.")
    except requests.RequestException as e:
        print(f"{Fore.RED}Error: {e}")

# Function to display IP information
def display_info(info):
    if info:
        print(f"{Fore.CYAN}IP Information:")
        for key, value in info.items():
            print(f"{Fore.YELLOW}{key}: {Fore.GREEN}{value}")

# Main function
def main():
    while True:
        display_logo()
        print(f"{Fore.BLUE}1. {Fore.WHITE}Get my IP and info")
        print(f"{Fore.BLUE}2. {Fore.WHITE}Track a given IP")
        print(f"{Fore.BLUE}3. {Fore.WHITE}Exit")
        choice = input(f"{Fore.CYAN}Enter your choice: {Fore.WHITE}")

        if choice == "1":
            print(f"{Fore.GREEN}Fetching your IP and info...")
            info = get_ip_info()
            display_info(info)
        elif choice == "2":
            ip = input(f"{Fore.CYAN}Enter the IP to track: {Fore.WHITE}")
            if ip:
                print(f"{Fore.GREEN}Tracking IP {ip}...")
                info = get_ip_info(ip)
                display_info(info)
            else:
                print(f"{Fore.RED}Invalid IP entered.")
        elif choice == "3":
            print(f"{Fore.MAGENTA}Exiting the tool. Have a great day!")
            sys.exit(0)
        else:
            print(f"{Fore.RED}Invalid choice. Please select 1, 2, or 3.")
        
        exit()

if __name__ == "__main__":
    main()
