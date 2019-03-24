#!/usr/bin/python3
# read content from gfwlist url and generate a foxproxy configuation file with it

import requests
import base64
import re

def parse():
	url = "https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt"
	resp = requests.get(url)
	rules = base64.b64decode(resp.content).decode()
	for line in re.findall("([^\n]+)", rules):
		if line.find("[") >= 0:
			continue
		if line.find("\\") >= 0:
			continue
		if line.find("!") >= 0:
			if line.find("General List End") >= 0:
				break
			else:
				continue

		obj = re.search("([^|@]+)", line)
		if obj:
			yield obj.group()

def join():
	text = None
	with open("foxyproxy.json", "r") as f:
		text = f.read()
		f.close()

	buff = ["""{
			"title": "✧(๑•̀ㅂ•́)و✧",
			"active": true,
			"pattern": "%s",
			"type": 1,
			"protocols": 1
		}""" % rule
		for rule in parse()
	]

	with open("foxyproxy.new.json", "w") as f:
		f.write(re.sub('"fuckmylife"', ",\n		".join(buff), text))

join()
