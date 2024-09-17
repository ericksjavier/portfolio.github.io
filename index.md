---
layout: default
---

# **Hello!**
My name is Erick Javier, I am a Cybersecurity professional since 2024 and this is a showcase of my current projects!

## Project 1: Creating a Secure Virtual Network

## Project 2: Microsoft Azure SIEM using Microsoft Sentinel

Created a Security Operations Center (SOC) environment using Azure and threat intelligence feeds to capture network traffic and security events ingested by the Log Analytics workspace. Implemented Microsoft Sentinel for centralized monitoring and analysis, demonstrating proficiency in cloud security, threat intelligence, and SIEM solutions.

![image](https://github.com/user-attachments/assets/d0d854e9-7f18-4b54-98a3-cc7935268e9e)

## Project 3: [Port Scanner Tool](https://github.com/ericksjavier/portfolio.github.io/blob/main/C23C12.py)

Developed a Python script to perform port scanning and identify network vulnerabilities, enabling further security analysis and mitigation. This project showcases skills in Python programming, network security, and data analysis.

```python
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
```
## Project 4: Ethical Hacking

## Project 5: Firewall and IDS configuration

Integrated Snort (IDPS) into the pfSense firewall to bolster network security. The integration process involved installing Snort via the pfSense package manager, configuring it to monitor specific network interfaces, and customizing its rule sets to detect and respond to potential threats. This setup included selecting and applying relevant rule sets, managing updates to keep threat definitions current, and adjusting preprocessor settings to optimize detection capabilities.

In addition, Snort’s logging and alerting mechanisms were configured to ensure effective notification of detected threats and suspicious activities, with logs being directed to appropriate storage locations and thresholds set for alerts. The configuration was tested to validate its functionality, ensuring Snort’s effectiveness in identifying and addressing network threats. As a result, Snort now actively enhances network security by providing real-time insights and alerts, contributing to a more secure and resilient network environment.



<dl>
<dt>Name</dt>
<dd>Erick</dd>
<dt>Born</dt>
<dd>2000</dd>
<dt>Birthplace</dt>
<dd>United States</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>

```
Life is all about love.
```
