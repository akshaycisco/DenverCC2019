#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 3
Author: Hank Preston <hapresto@cisco.com>

api_requests_example.py
Illustrate the following concepts:
- Making REST API calls using requests library
- Intended to be entered into an interactive
  interpreter
"""


import requests
from pprint import pprint
router = {"ip": "198.18.134.11",
	      "port": "443",
          "user": "admin",
          "pass": "C1sco12345"}

headers = {"Accept": "application/yang-data+json"}

u = "https://{}:{}/restconf/data/interfaces/interface=GigabitEthernet1"

u = u.format(router["ip"], router["port"])

r = requests.get(u,
		     headers = headers,
		     auth=(router["user"], router["pass"]),
		     verify=False)

pprint(r.text)

api_data = r.json()
interface_name = api_data["ietf-interfaces:interface"]["name"]
interface_name
