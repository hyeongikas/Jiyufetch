import platform
import subprocess
import os
from ascii_art import AsciiArt

###### ANSI escape codes for colors ######
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    END = '\033[0m'

def get_cpu_info():
    try:
        if platform.system() == "Linux":
            cpu_info = subprocess.check_output(['lscpu']).decode('utf-8')
            for line in cpu_info.split('\n'):
                if line.startswith("Model name:"):
                    return line.split(":")[1].strip()
        elif platform.system() == "macOS":  #Darwin
            cpu_info = subprocess.check_output(['sysctl', '-n', 'machdep.cpu.brand_string']).decode('utf-8').strip()
            return cpu_info
        elif platform.system() == "Windows":
            cpu_info = subprocess.check_output(['wmic', 'cpu', 'get', 'Name']).decode('utf-8').strip().split('\n')[1]
            return cpu_info
    except Exception as e:
        return f"Error retrieving CPU info: {e}"

def get_linux_distribution():
    try:
        if os.path.exists('/etc/os-release'):
            with open('/etc/os-release') as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith('NAME'):
                        return line.split('=')[1].strip().strip('"')
        elif os.path.exists('/etc/lsb-release'):
            with open('/etc/lsb-release') as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith('DISTRIB_DESCRIPTION'):
                        return line.split('=')[1].strip().strip('"')
        elif os.path.exists('/etc/debian_version'):
            debian_version = open('/etc/debian_version').read().strip()
            return "Debian " + debian_version
        elif os.path.exists('/etc/redhat-release'):
            return open('/etc/redhat-release').read().strip()
        else:
            distro_info = subprocess.check_output(['lsb_release', '-ds']).decode('utf-8').strip()
            return distro_info
    except Exception as e:
        return f"Error retrieving distribution info: {e}"

def get_os_info():
    os_info = {
        "System": platform.system(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": get_cpu_info(),
    }
    if platform.system() == "Linux":
        os_info["Distribution"] = get_linux_distribution()
    return os_info

def main():
    os_info = get_os_info()

    system = os_info["System"]
    distribution = os_info.get("Distribution", "").lower()
    
    if system == "Linux":
        if "arcolinux" in distribution:
            os_ascii = AsciiArt.ARCOLINUX
        elif "arch" in distribution:
            os_ascii = AsciiArt.ARCH
        elif "ubuntu" in distribution:
            os_ascii = AsciiArt.UBUNTU
        else:
            os_ascii = AsciiArt.LINUX
    else:
        os_ascii = getattr(AsciiArt, system.upper(), None)

    os_info_text = [
        f"System: {os_info['System']}",
        f"Release: {os_info['Release']}",
        f"Version: {os_info['Version']}",
        f"Machine: {os_info['Machine']}",
        f"Processor: {os_info['Processor']}"
    ]
    if 'Distribution' in os_info and os_info['Distribution']:
        os_info_text.insert(1, f"Distribution: {os_info['Distribution']}")

    if os_ascii:
        ascii_lines = os_ascii.strip().split('\n')
        longest_ascii_line = max(len(line) for line in ascii_lines)
        
        for i, line in enumerate(ascii_lines):
            if i < len(os_info_text):
                print(f"{line.ljust(longest_ascii_line)}  {os_info_text[i]}")
            else:
                print(line)

    print(colors.CYAN + "\nCPU Information:" + colors.END)
    print(os_info['Processor'])

if __name__ == "__main__":
    main()
