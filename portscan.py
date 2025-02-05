import socket
import threading
import argparse

# List to store scan results
open_ports = []

# Port scanning function
def scan_port(target_ip, port):
    try:
        # Create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to 1 second
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
            open_ports.append(port)
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Main function
def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("target_ip", help="Target IP address to scan")
    parser.add_argument("start_port", type=int, help="Start port number")
    parser.add_argument("end_port", type=int, help="End port number")
    args = parser.parse_args()

    target_ip = args.target_ip
    start_port = args.start_port
    end_port = args.end_port

    threads = []

    # Create and start a thread for each port
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Print open ports
    print("Open ports:", open_ports)

if __name__ == "__main__":
    main()
