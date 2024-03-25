0x0B. SSH

1. **What is a server:**
   A server is a computer or a program that provides functionality, data, or services to other computers, known as clients, over a network. Servers can fulfill various roles such as hosting websites, storing files, managing databases, or providing access to resources.

2. **Where servers usually live:**
   Servers typically reside in data centers or server rooms equipped with proper cooling, power supply, and security measures. They can also be hosted remotely in the cloud, providing scalability and accessibility to users from anywhere with an internet connection.

3. **What is SSH:**
   SSH (Secure Shell) is a cryptographic network protocol that allows secure communication and data transfer between two devices, typically a client and a server, over an insecure network. It provides encrypted authentication and secure access to remote systems, commonly used for remote administration and accessing command-line interfaces.

4. **How to create an SSH RSA key pair:**
   To create an SSH RSA key pair, you can use the `ssh-keygen` command-line tool. Here's how you can do it:
   ```
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   This command generates an RSA key pair with a specified length of 4096 bits. Replace `"your_email@example.com"` with your email address.

5. **How to connect to a remote host using an SSH RSA key pair:**
   Once you have generated your SSH key pair, you can connect to a remote host by adding your public key to the `authorized_keys` file on the remote server. Then, you can use the following command to connect:
   ```
   ssh -i /path/to/private_key username@remote_host
   ```
   Replace `/path/to/private_key` with the path to your private key file, `username` with your username on the remote server, and `remote_host` with the hostname or IP address of the remote server.

6. **The advantage of using #!/usr/bin/env bash instead of /bin/bash:**
   Using `#!/usr/bin/env bash` as the shebang line at the beginning of a Bash script allows the system to locate the Bash interpreter dynamically using the PATH environment variable. This provides better portability across different systems where Bash may be installed in different locations. It ensures that the script runs with the correct interpreter even if Bash is installed in a non-standard location. On the other hand, specifying `#!/bin/bash` directly would require the script to know the exact location of the Bash interpreter, which might differ between systems.


# 0x0B. SSH 

## Resource

- [What is a (physical) server - text](https://en.wikipedia.org/wiki/Server_%28computing%29#Hardware_requirement)
- [What is a (physical) server - video](https://www.youtube.com/watch?v=B1ANfsDyjeA)
- [SSH essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
- [SSH Config File](https://www.ssh.com/academy/ssh/config)
- [Public Key Authentication for SSH](https://www.ssh.com/academy/ssh/public-key-authentication)
- [How Secure Shell Works](https://www.youtube.com/watch?v=ORcvSkgdA58)
- [SSH Crash Course](https://www.youtube.com/watch?v=hQWRp-FdTpc) (*(Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.*)

### For reference:

- [Understanding the SSH Encryption and Connection Process](https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process)
- [Secure Shell Wiki](https://en.wikipedia.org/wiki/Secure_Shell)
- [IETF RFC 4251 (Description of the SSH Protocol)](https://www.ietf.org/rfc/rfc4251.txt)
- [Internet Engineering Task Force](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force)
- [Request for Comments (RFCs)](https://en.wikipedia.org/wiki/Request_for_Comments)

## Tasks

<details>
<summary><a href="./0-use_a_private_key">0. Use a private key</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/yW4gBSpM/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./1-create_ssh_key_pair">1. Create an SSH key pair</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/pXPbpdbx/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./2-ssh_config">2. Client configuration file</a></summary><br>
<a href='https://postimg.cc/Hjb2CMHK' target='_blank'><img src='https://i.postimg.cc/y6brchGV/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary>3. Let me in!</summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/3N2k9F3k/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./100-puppet_ssh_config.pp">4. Client configuration file (w/ Puppet)</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/ryBvRXzV/image.png' border='0' alt='image'/></a><br>
<ul><li>Install puppet stdlib module;</li></ul>
<pre>sudo puppet module install puppetlabs-stdlib</pre>
</details>

