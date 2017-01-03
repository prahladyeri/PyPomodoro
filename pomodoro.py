"""Time tracking utility for Freelancers"""
import winsound
import os
import time, datetime, pickle

__author__ = "Prahlad Yeri"
__email__ = "prahladyeri@yahoo.com"
__copyright__ = "Copyright 2017, Prahlad Yeri"
__credits__ = ["Prahlad Yeri"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Prahlad Yeri"
__status__ = "Development" #Production, Prototype

project_details = {
	"name" : "",
	"category" : "",
	}
last_beep = None
timesheet = [] #{project: <project_details>, start_time: <datetime>, end_time: <datetime>} TODO: get this from pickle

def start_tracking():
	global project_details, last_beep
	print("Working on %s:%s" % (project_details['name'], project_details['category']))
	print("Started tracking %s" % (datetime.datetime.now()))
	session_start_time = datetime.datetime.now()
	last_beep = datetime.datetime.now()
	while(True):
		diff = (datetime.datetime.now() - last_beep).total_seconds() / 60.0 #in minutes
		#diff = diff.total_seconds() / (60.0) 
		if (diff >= 2): #30
			reminder_text = "%s:%s" % (project_details['name'], project_details['category'])
			diff = (datetime.datetime.now() - session_start_time)
			diff = diff.total_seconds() / (60.0) #in minutes
			minutes_worked = round(diff)
			winsound.Beep(700,800)
			print("Reminder for %s" % reminder_text)
			print("Minutes worked in this session: %s" % minutes_worked)
			print("*******")
			timesheet.append({
			"project": project_details,
			"start_time": last_beep,
			"end_time": datetime.datetime.now()
			})
			pickle.dump(timesheet, open('timesheet.pkl','wb'),-1)
			last_beep = datetime.datetime.now()

def main():
	global project_details, last_beep
	if os.path.exists("timesheet.pkl"):
		timesheet = pickle.load(open('timesheet.pkl','rb'))
		print("Successfully imported pickle file. %d records found" % len(timesheet))
	
	while(True):
		print("[1]: Set Project details.")
		print("[2]: Start tracking.")
		print("[3]: Exit tracker.")
		x = int(input("\nEnter an option: "))
		if x == 1:
			print("Current details: %s:%s" % (project_details['name'], project_details['category']))
			project_details['name'] = input("Enter Project name (example: 'Working on a script'):")
			project_details['category'] = input("Enter Project Category (example: 'python-crawler'):")
			x = input("Details entered successfully.\nDo you want to start tracking now? (Y/n)")
			if x.lower() == 'y':
				start_tracking()
				break
		elif x == 2:
			start_tracking()
			break
		elif x == 3:
			break

if __name__ == "__main__":
	print("")
	main()