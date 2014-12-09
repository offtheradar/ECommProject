#!/usr/bin/python

import sys
import os
import stat
import cgi
import cgitb
import re
     
def main():
        print "Content-type: text/html\n"
        form = cgi.FieldStorage()
        inventory = []
        content = ""
        per = False

        with open ('LoggedIn.csv', 'r') as logd:
                users = []
                for line in logd:
                       line = line.strip()
                       users.append(line)
                if (form.has_key("username")):
                        per = True

                if (per == True):
                	if ((form.has_key("neb")) and (form["neb"].value !="0") and (form.has_key("checkneb")) and (form["checkneb"].value !="")):
                        	neb = int(form.getvalue("neb"))
                	else:
                        	neb = 0
                	if ((form.has_key("checkgal")) and (form["checkgal"].value !="0") and (form.has_key("checkgal")) and (form["checkgal"].value !="")):
                        	gal = int(form.getvalue("gal"))
                	else:
                        	gal = 0

                    	with open ('inventory.csv', 'r') as inv:
                        	for line in inv:
                        		line = (line.split(","))
                        		inventory.append(int(line[1]))

                        	if ((inventory[0]-(neb))>=0)and((inventory[1]-(gal))>=0):
                        		line1 = 'neb,'+str(inventory[0]-(neb))+',10000\n'
                        		line2 = 'gal,'+str(inventory[1]-(gal))+',10000\n'


                        		content = line1+line2

                    			with open ('inventory.csv', 'w') as wf:
                                	 	wf.write(content)
                        		wf.close
                        		print "<html>"
                        		print"  <head><title>Bill</title></head>"
                        		print " <body>"
                        		print "  <p>"
                       			print "  <b>BILL</b><br>"
                        		print "  ============================<br>"
                       	 		print "  Nebula * " + str(neb) + "  = $" + str(10000*(neb)) + "<br>"
                        		print "  Galaxy * " + str(gal) + " = $" + str(10000*(gal))+ "<br>"
                        		print "  <b>TOTAL : $" + str( (10000*(neb)) + (10000*(gal)))+ " CND</b><br>"
                        		print "  THANK YOU FOR YOUR PURCHASE"

                        		print " </body>"
                        		print "</html>"
                                else:
                        		print "<html>"
                        		print " <head><title>Error</title></head>"
                        		print " <body>"
                        		print "  <p>"
                        		print " Out of inventory.<br>"
                        		print "  </p>"
                        		print " </body>"
                        		print "</html>"
                	fp.close()

                else:
                        	print "<html>"
                        	print " <head><title>Error</title></head>"
                        	print " <body>"
                        	print "You are not loggedin!"
                        	print "  Login page : " + '<a href="login.html">Login</a><br>'
                        	print "  Registration page : " + '<a href="register.html">Register</a><br>'
                        	print " </body>"
                        	print "</html>"
main()

