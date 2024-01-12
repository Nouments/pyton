# info.py

import platform
import socket

def main():
    print("System Information:")
    print(f'System: {platform.system()}')
    print(f'Node Name: {platform.node()}')
    print(f'Release: {platform.release()}')
    print(f'Version: {platform.version()}')
    print(f'Machine: {platform.machine()}')
    print(f'Processor: {platform.processor()}')
    print(f'Hostname: {socket.gethostname()}')
    print(f'IP Address: {socket.gethostbyname(socket.gethostname())}')

if __name__ == "__main__":
    main()
