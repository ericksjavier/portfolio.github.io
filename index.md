---
layout: default
---

# **Hello!**
My name is Erick Javier, I am a Cybersecurity professional since 2024 and these are my current projects.

# [Port Scanner Tool](https://github.com/ericksjavier/portfolio.github.io/blob/main/C23C12.py)

Developed a Python script to perform port scanning and identify network vulnerabilities, enabling further security analysis and mitigation. This project showcases skills in Python programming, network security, and data analysis.

There should be whitespace between paragraphs.

Microsoft Azure SIEM using Microsoft Sentinel
![image](https://github.com/user-attachments/assets/d0d854e9-7f18-4b54-98a3-cc7935268e9e)


There should be whitespace between paragraphs. We recommend including a README, or a file with information about your project.

# Header 1

This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

## Header 2

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.

### Header 3

```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l)
  return true;
}
```
Port Scanner Tool
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

#### Header 4

*   This is an unordered list following a header.
*   This is an unordered list following a header.
*   This is an unordered list following a header.

##### Header 5

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### Header 6

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

### There's a horizontal rule below this.

* * *

### Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

### And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

### And a nested list:

- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item

### Small image

![Octocat](https://github.githubassets.com/images/icons/emoji/octocat.png)

### Large image

![Branching](https://guides.github.com/activities/hello-world/branching.png)


### Definition lists can be used with HTML syntax.

<dl>
<dt>Name</dt>
<dd>Godzilla</dd>
<dt>Born</dt>
<dd>1952</dd>
<dt>Birthplace</dt>
<dd>Japan</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

```
The final element.
```
