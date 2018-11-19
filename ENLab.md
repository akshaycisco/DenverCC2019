Thanks for Joining the EN Lab Track - Cisco Connect @ Denver (http://cs.co/denverlab18)

# Lab Setup 
Make sure you have following softwares installed
  1. [Install Cisco Anyconnect](https://developer.cisco.com/site/sandbox/anyconnect/)
  2. [Install RDP](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients)
  
  
# Lab Instructions
  1. Connect to Lab setup via Cisco Anyconnect
       * Anyconnect Host : dcloud-sjc-anyconnect.cisco.com
       * Username/ Password : check with proctor
  2. After succesfully "Connected to dcloud-sjc-anyconnect.cisco.com"
       * Open RDP - 198.18.134.48
       * Username : developer
       * Password : C1sco12345
       * Note: The IP address is 198... not 192...   
  3. Now you must be logged into CentOS Machine where you will continue your lab.
  4. Open Terminal on the CentOS desktop and run following commands
        [developer@centos ~]$ cd code/
        [developer@centos code]$ source venv/bin/activate
        (venv) [developer@centos code]$ pip list
        * this will list all installed packages 
        * Note: Make sure (venv) prefix is present all the time.
 ## Excercise 1:  Verify Python script for Accessing IOS-XE device
      1. Open 'Atom' Text Editor on Desktop
      2. Navigate to following folder 
            /code/netprog_basics/programming_fundamentals/python_part_3/
      3. Make sure the credentials & IP are as follows on following 3 files:
      
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
			  
            File: api_ncclient_example.py .. line 28
                delete line 28: <name>GigabitEthernet1</name>
            	Change line 42: 
				from : pprint(interface_python["interfaces"]["interface"]["name"]["#text"])
				to : pprint(interface_python["interfaces"])
	    	After changes in api_ncclient_example.py -lines 24 - 41 should look like -
			netconf_filter = """
			<filter>
  			<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    			<interface>
    			</interface>
  			</interfaces>
			</filter>
			"""

			m = manager.connect(host=router["ip"],
                    	port=router["port"],
                    	username=router["user"],
                    	password=router["pass"],
                    	hostkey_verify=False)

			interface_netconf = m.get_config("running", netconf_filter)
			interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
			pprint(interface_python["interfaces"])
	    
	    Save and close all the files
   ## Excercise 2: Execute the Python scripts
   	1) Open Terminal on the CentOS desktop and run following commands
	* [developer@centos ~]$ cd code/
	* [developer@centos code]$ source venv/bin/activate
	2) Navigate to python_part_3
            (venv) [developer@centos ~] cd /home/developer/code/netprog_basics/programming_fundamentals/python_part_3/
	    
   ### Excercise 2a: Access IOS XE Device with CLI ( Using Netmiko Library)
   	1) Open Terminal on the CentOS desktop and run following commands
	* [developer@centos ~]$ cd code/
	* [developer@centos code]$ source venv/bin/activate
	2) Navigate to python_part_3
            (venv) [developer@centos ~] cd /home/developer/code/netprog_basics/programming_fundamentals/python_part_3/
	3) Run the Python code for Netmiko:
	
		(venv) [developer@centos python_part_3]$ python api_netmiko_example.py
		
   ### Excercise 2b: Access IOS XE Device with REST-API ( Using Requests Library)
   	1) Open Terminal on the CentOS desktop and run following commands
	* [developer@centos ~]$ cd code/
	* [developer@centos code]$ source venv/bin/activate
	2) Navigate to python_part_3
            (venv) [developer@centos ~] cd /home/developer/code/netprog_basics/programming_fundamentals/python_part_3/
	3) Run the Python code for RESTAPI:
	
		(venv) [developer@centos python_part_3]$ python api_requests_example.py
		
   ### Excercise 2c: Access IOS XE Device with NETCONF ( Using ncclient Library)
   	1) Open Terminal on the CentOS desktop and run following commands
	* [developer@centos ~]$ cd code/
	* [developer@centos code]$ source venv/bin/activate
	2) Navigate to python_part_3
            (venv) [developer@centos ~] cd /home/developer/code/netprog_basics/programming_fundamentals/python_part_3/
	3) Run the Python code for RESTAPI:
	
		(venv) [developer@centos python_part_3]$ python api_ncclient_example.py	

   ### Excercise 2d: Access IOS XE Device with Ansible 
   	1) Open Terminal on the CentOS desktop and run following commands
	* [developer@centos ~]$ cd code/
	* [developer@centos code]$ source venv/bin/activate
	2) Navigate to python_part_3
            (venv) [developer@centos ~] cd /home/developer/code/dnav3-code/intro-ansible
	3) Follow detailed-instructions: 
		https://learninglabs.cisco.com/tracks/dnav3-track/intro-ansible-iosxe/ansible-ios-modules/step/2
		
	4) Run Ansible playbook - 
		ansible-playbook ansible-02-ios-modules/02-ios_command_show.yaml
 
 ## Excercise 3: Access DNA Center API with Postman
  	1) Open Postman App on Desktop
	2) Ignore prompt for Updates & close all Pop-up windows
	3) Make sure you see the Collections & Environment
		* Click Import - Top Left corner
		* Choose File -> code/dnav3-code/postman/(all-files) -> Click Import
	4) Go to Collections -> 'dnav3-dnac-nbapi-hello-network'
		Make sure Environment on Top right is set to -> 'dnav3-dnac-nbapi-hello-network'
	5) First lets get our Access token a.k.a Ticket
		Collections ->'dnav3-dnac-nbapi-hello-network'->'1.Ticket' -> Send-Post request
		Expected output:
			200 OK 
			Token:"...."
	6) Using the Access Token from previous step we will send GET request to list all Network Device information
		Collections ->'dnav3-dnac-nbapi-hello-network'->'2.Network Device' -> Send-GET request
		Expected output:
			200 OK 
			(List of device information)


   References: 
   	Cisco DNA Lab Modules - https://learninglabs.cisco.com/tracks/dnav3-track
	Cisco Devnet : https://developer.cisco.com/startnow/
	
   
        
        
