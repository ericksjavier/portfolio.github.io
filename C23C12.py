import socket
import datetime

def scanports(host, port_range):
    open_ports = []
    error_log = []
    start_time = datetime.datetime.now()
    end_time = datetime.datetime.now()
    total_time = end_time - start_time

    print(f"Scanning host: {host}")
    print(f"Scanning ports: {port_range}")

    try:
        with open('scan_results.txt', 'a') as file:  # appends
            file.write(f"Scan started at: {start_time}\n")
            file.write(f"Scan ended at: {end_time}\n")
            file.write(f"Total scan time: {total_time}\n")
            file.write("Open ports:\n")
            file.flush()

            for port in open_ports:
                file.write(f"Port {port} is open\n")
            for error in error_log:
                file.write("Error occurred.\n")
                file.write(f"{error}\n")

        for port in port_range:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((host, port))
                if result == 0:
                    open_ports.append(port)
                    file.write(f"Port {port} is open.\n")
                    file.flush()
                sock.close()
            except socket.error as e:
                error_log.append(f"Error connecting to port {port}: {e}")
                file.write(f"Error connecting to port {port}: {e}\n")
                file.flush()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Scan Finished. Results have been saved to scan_results.txt")

if __name__ == "__main__":
    host = input("Enter a host to scan: ")
    port_range = range(1, 1025)

    try:
        ip_address = socket.gethostbyname(host)
        print(f"Starting scan on host: {host} ({ip_address})")
        scanports(ip_address, port_range)
    except socket.gaierror as e:
        print(f"Error: Host name could not be resolved. {e}")
    except socket.error as e:
        print(f"Error: Could not connect to server. {e}")
    except KeyboardInterrupt:
        print("Scan aborted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
