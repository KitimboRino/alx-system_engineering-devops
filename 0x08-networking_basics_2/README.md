0x08. Networking basics #1

localhost/127.0.0.1:

localhost: It is a hostname that refers to the current device used to access it.
In networking, localhost is often used to access the network services that are running on the host via the loopback network interface.
It is commonly associated with the IP address 127.0.0.1.
127.0.0.1: This is the loopback address, also known as the localhost address.
It is used to establish network connections with the same host (your own machine) via the loopback interface.
0.0.0.0:

In networking, 0.0.0.0 is a special IP address that usually means "any address" or "all addresses." 
When a service is bound to 0.0.0.0, it is listening on all available network interfaces, allowing it to accept connections from any IP address.


/etc/hosts:
/etc/hosts is a plain text file on Unix-based operating systems (like Linux) that maps IP addresses to hostnames.
It is a local DNS (Domain Name System) equivalent, and it is used to resolve domain names to IP addresses locally, bypassing the need to query external DNS servers.
You can manually edit this file to define custom mappings.


Displaying Active Network Interfaces:
To display active network interfaces on your machine, you can use various commands depending on your operating system.
 Here are examples for common systems:

On Linux:
bash
Copy code
ifconfig

# or
ip a
On macOS:

bash
ifconfig
# or
ipconfig getifaddr en0  # en0 is an example, replace with your interface name


On Windows:

cmd
ipconfig
These commands will show information about your machine's active network interfaces, including details such as IP addresses, MAC addresses, and more.
