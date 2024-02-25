0x09. Web infrastructure design

Let's consider a simplified diagram for the infrastructure:

```
User
 |
Load Balancer
 | \
Web Server 1 Web Server 2
 |         |
Database Server
```

**Explanation of Each Component:**

1. **User:**
   - Represents the end-users accessing the website through their browsers.

2. **Load Balancer:**
   - Distributes incoming web traffic across multiple web servers to ensure even distribution and prevent overloading a single server.

3. **Web Servers (Web Server 1, Web Server 2):**
   - Hosts the website and processes user requests. In a redundant setup, multiple web servers share the load, improving performance and providing failover in case one server fails.

4. **Database Server:**
   - Stores and manages the website's data. In a redundant setup, there might be measures like database replication or clustering to ensure data availability and reliability.

**System Redundancy:**

- **Web Server Redundancy:**
  - Multiple web servers (Web Server 1, Web Server 2) ensure that if one server goes down, the other can handle the traffic, reducing the risk of a Single Point of Failure (SPOF) for the web application.

- **Load Balancer Redundancy:**
  - If the primary load balancer fails, a secondary one can take over, ensuring continuous distribution of traffic and preventing disruptions.

- **Database Redundancy:**
  - Measures like database replication or clustering can be implemented for the database server. This ensures that if one database server fails, another can take over, minimizing downtime and data loss.

**Acronyms:**

1. **LAMP:**
   - Acronym for Linux, Apache, MySQL, and PHP/Python/Perl. It represents a common web development stack where Linux is the operating system, Apache is the web server, MySQL is the database, and PHP/Python/Perl is the programming language.

2. **SPOF:**
   - Acronym for Single Point of Failure. It refers to a component in a system that, if it fails, can lead to the entire system's failure.

3. **QPS:**
   - Acronym for Queries Per Second. It measures the number of queries (requests) processed by a system in one second, indicating the system's performance.i
