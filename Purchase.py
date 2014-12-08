#!/usr/bin/python
import re
import cgi
import csv
import cgitb
cgitb.enable()

print "Content-type: text/html\n"
form = cgi.FieldStorage()
inventory = []
content = ""
log = False

with open ('LoggedIn.csv', 'r') as logd:
                users = []
                for line in logd:
                        line = line.strip()
                        users.append(line)
                if (form.has_key("username") and str(form["username"].value) in users):
                        log = True

if (log == True):
                if ((form.has_key("neb")) and (form["neb"].value !="0") and (form.has_key("neb")) and (form["neb"].value !="off")):
                        neb = int(form.getvalue("neb"))
                else:
                        neb = 0
                if ((form.has_key("man")) and (form["man"].value !="0") and (form.has_key("man")) and (form["man"].value !="off")):
                        firm = int(form.getvalue("man"))
                else:
                        firm = 0
                
with open ('Inventory.csv', 'r') as fp:
                for line in fp:
                        line = (line.split(","))
                        inventory.append(int(line[2]))
                with open ('Inventory.csv', 'r') as fp:
                        for line in fp:
                                line = (line.split(","))
                                inventory.append(int(line[1]))
if ((inventory[1]-(neb))>=0)and((inventory[2]-(man))>=0):
                        line1 = 'neb,'+str(inventory[1]-(baby))+',20\n'
                        line2 = 'man,'+str(inventory[2]-(firm))+',20\n'
                        
                       
                        content = line1+line2

with open ('Inventory.csv', 'w') as wf:
                        wf.write(content)
                        wf.close
                        print "<html>"
                        print"  <head><title>Bill</title></head>"
                        print " <body>"
                        print "  <p>"
                        print "  <b>BILL</b><br>"
                        print "  ============================<br>"
                        print "  Nebula * " + str(neb) + "  = $" + str(20*(neb)) + "<br>"
                        print "  Galaxy * " + str(man) + " = $" + str(20*(man))+ "<br>"
                       
                        
                        print "  ============================<br>"
                        print "  <b>TOTAL : $" + str( (20*(neb)) + (20*(man) ))+ " CND</b><br>"
                        print "  THANK YOU FOR YOUR PURCHASE"
                       
                        print " </body>"
                        print "</html>"
else:
                        print "<html>"
                        print " <head><title>Error</title></head>"
                        print " <body>"
                        print "  <p>"
                        print "  Our apologies. It seems we're out of inventory.<br>"
                        print "  You have been logged out automatically.<br>"
                        print "  Please login again in order to place an order<br>"
                        
                        print "  </p>"
                        print " </body>"
                        print "</html>"
        		fp.close()

"""        	else:
                	print "<html>"
                	print " <head><title>Error</title></head>"
                	print " <body>"
                	print "  <p>"
                	print "  Please login if you wish to buy stuff.<br>"
                	print "  If you have not yet registered, please do so, if you are an existing member please login. <br>"
                	print "  To go back to Login page : " + '<a href="login.html">Login</a><br>'
                	print "  To go back to Registeration page : " + '<a href="registeration.html">Register</a><br>'
                	print " </body>"
                	print "</html>"
"""


                                                                                                                                  140,0-1       Bot

