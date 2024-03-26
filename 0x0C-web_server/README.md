0x0C. Web server

1. **Main Role of a Web Server:**
   A web server is like a waiter at a restaurant for websites. Its main job is to serve web pages to users when they request them through their web browsers. When you type a website's address (like www.example.com) into your browser, the web server fetches the requested webpage and sends it back to your browser so you can see it.

2. **Child Process:**
   Imagine you're playing a video game on your computer, and suddenly you need to check your email. You might open another program while the game is still running. That new program is like a child process. It's a separate task or program that runs independently of the main program.

3. **Parent and Child Processes in Web Servers:**
   Web servers often have a parent process and child processes because they handle multiple requests at the same time. The parent process is like the manager, and the child processes are like the workers. The parent process supervises and manages the child processes, making sure they're doing their jobs properly and handling incoming requests efficiently.

4. **Main HTTP Requests:**
   HTTP (Hypertext Transfer Protocol) is the protocol used for transferring data on the web. The main HTTP requests are:
   - GET: Used to request data from a specified resource.
   - POST: Used to submit data to be processed to a specified resource.
   - PUT: Used to update a resource.
   - DELETE: Used to delete a specified resource.

5. **DNS:**
   DNS stands for Domain Name System. It's like the internet's phonebook. When you type a website's name (like www.example.com) into your browser, DNS translates that human-readable name into the unique numerical IP address that identifies the website's server on the internet.

6. **Main Role of DNS:**
   The main role of DNS is to translate domain names (like www.example.com) into IP addresses, which are needed to locate and communicate with the correct server on the internet.

7. **DNS Record Types:**
   - A (Address): Maps a domain name to an IP address.
   - CNAME (Canonical Name): Allows a domain to be an alias of another domain.
   - TXT (Text): Used to store text information, often for verification purposes.
   - MX (Mail Exchange): Specifies the mail server responsible for receiving email on behalf of a domain.
