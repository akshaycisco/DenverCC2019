Thanks for Joining the EN Lab Track - Cisco Connect @ Denver

# Lab Setup 
Make sure you have following softwares installed
  1. [Install Cisco Anyconnect](https://developer.cisco.com/site/sandbox/anyconnect/)
  2. [Install RDP](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients)
  
  
# Lab Instructions
  1. Connect to Lab setup via Cisco Anyconnect
       *Anyconnect Host : dcloud-sjc-anyconnect.cisco.com
       *Username/ Password : check with proctor
  2. After succesfully "Connected to dcloud-sjc-anyconnect.cisco.com"
       *Open RDP - 198.18.134.48
       *Username : developer
       *Password : C1sco12345
       Note: The IP address is 198... not 192...   
  3. Now you must be logged into CentOS Machine where you will continue your lab.
  4. Open Terminal on the CentOS desktop and run following commands
        [developer@centos ~]$ cd code/
        [developer@centos code]$ source venv/bin/activate
        (venv) [developer@centos code]$ pip list
        ** this will list all installed packages ** 
        Note: Make sure (venv) prefix is present all the time.
 ## Excercise 1:  Python script for Accessing IOS-XE device with CLI
      1. Open 'Atom' Text Editor on Desktop
      2. Navigate to following folder 
            /code/netprog_basics/programming_fundamentals/python_part_3/
      3. Make sure the credentials & IP are as follows on following 2 files:
            File: api_netmiko_example.py .. lines 18-22
                router = {"device_type": "cisco_ios",
                           "host": "198.18.134.11",
                           "user": "admin",
                           "pass": "C1sco12345"}
            File: api_requests_example.py .. line 18-22
                router = {"ip": "198.18.134.11,
	                        "port": "443",
                          "user": "admin",
                          "pass": "C1sco12345"}
            File: api_ncclient_example.py .. lines 19-23
                router = {"ip": "198.18.134.11",
                          "port": 830,
                          "user": "admin",
                          "pass": "C1sco12345"}
            
            
      2. Navigate to python_part_3
            (venv) [developer@centos ~] cd /home/developer/code/netprog_basics/programming_fundamentals/python_part_3/
            
        
        
