
import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup
for i in range(1, 10):
	page = requests.get("https://www.naukri.com/jobs-in-nasik-%s" %i)
	soup = BeautifulSoup(page.content, 'html.parser')
	data = soup.find_all("div",{"itemtype":"http://schema.org/JobPosting"}) 
	item = data[0] 
	alldata = []   
	desig = []      																	
	org =[]
	exp = []
	loc = []
	skill = []
	salary = []
	date = []
	store = []

	for item in data:
		try:
			desig = item.find(class_="desig").get_text()
			str(desig + ",")
			org = item.find(class_="org").get_text()	
			str(org + ",")	
			exp = item.find(class_="exp").get_text()
			str(exp + ",")
			loc = item.find(class_="loc").get_text()
			str(loc + ",")
		except:
			pass
		try:
			skill = item.find(class_="skill").get_text()
			str(skill + ",")
	    except:
	    	pass
	    try:
	    	salary = item.find(class_="salary").get_text()
		    str(salary + ",")
		except:
	    	pass
	    try:
	    	date = item.find(class_="date").get_text()
			str(date)
		except:
	    	pass

		
        for alldata in  range (1):
        	with open('amol-data.csv', 'a') as csv_file:		  
	    		writer = csv.writer(csv_file)
	    		writer.writerow([desig, org,exp,loc,skill,salary,date, datetime.now()])

		# outputFile = open('naukariD.csv', 'w')          
		# outputWriter = csv.writer(outputFile)
		# outputWriter.writerow([desig, org,exp,loc,skill,salary,date, datetime.now()])

		

 
