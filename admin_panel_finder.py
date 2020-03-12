#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("AzCyberTeam.txt","r");
	AzCyberTeam = raw_input("Enter Site Name \n(ex : saytname.com or www.saytname.com ): ")
	print "\n\nAvilable links : \n"
	while True:
		sub_AzCyberTeam = f.readline()
		if not sub_AzCyberTeam:
			break
		req_AzCyberTeam = "http://"+AzCyberTeam+"/"+sub_AzCyberTeam
		req = Request(req_AzCyberTeam)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_AzCyberTeam

def Credit():
	Space(9); print "╔════════════════════════════════════╗"
	Space(9); print "║  ***   Admin Panel Finder   ***    ║"
	Space(9); print "║  ***    Script by PU24T     ***    ║"
	Space(9); print "║       𝔸𝕫𝕖𝕣𝕓𝕒𝕚𝕛𝕒𝕟 ℂ𝕪𝕓𝕖𝕣 𝕋𝕖𝕒𝕞        ║"
	Space(9); print "╚════════════════════════════════════╝"

Credit()
findAdmin()
