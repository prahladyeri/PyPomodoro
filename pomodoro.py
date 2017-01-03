"""Time tracking utility for Freelancers"""
import winsound
import os
import time, datetime, pickle
import config

__author__ = "Prahlad Yeri"
__email__ = "prahladyeri@yahoo.com"
__copyright__ = "Copyright 2017, Prahlad Yeri"
__credits__ = ["Prahlad Yeri"]
__license__ = "MIT"
__version__ = "1.0.3"
__maintainer__ = "Prahlad Yeri"
__status__ = "Development" #Production, Prototype

last_beep = None
timesheet = [] #{project: <project_details>, start_time: <datetime>, end_time: <datetime>} TODO: get this from pickle

"""Updates the start time in config.schedule as per the current time."""
def set_schedule():
	now = datetime.datetime.now()
	#start = datetime.datetime(now.year, now.month, now.day, 13,30)
	i = 0
	for item in config.schedule:
		item['start'] = now + datetime.timedelta(minutes = i)
		i += item['duration']

def select_schedule():
	if len(config.schedule) == 0:
		return False
	i = 1
	for item in config.schedule:
		print("[%d] %s:%s (%s mins)" % (i, item['category'], item['name'], item['duration']))
		i += 1
	while True:
		num = int(input("\n Select schedule:"))
		if num in range(1, len(config.schedule)+1):
			return config.schedule[num-1]
		else:
			print("Invalid Input")

def start_tracking(task):
	global last_beep
	print("Working on %s:%s" % (task['category'], task['name']))
	print("Started tracking at %s" % (datetime.datetime.now().strftime("%H:%M")))
	print("Beep interval is set to %d" % config.slot_interval)
	session_start_time = datetime.datetime.now()
	last_beep = datetime.datetime.now()
	while(True):
		diff = (datetime.datetime.now() - last_beep).total_seconds() / 60.0 #in minutes
		#diff = diff.total_seconds() / (60.0) 
		if (diff >= config.slot_interval): #30
			reminder_text = "%s:%s" % (task['category'], task['name'])
			diff = (datetime.datetime.now() - session_start_time)
			diff = diff.total_seconds() / (60.0) #in minutes
			minutes_worked = round(diff)
			winsound.Beep(700,800)
			print("Reminder for %s" % reminder_text)
			print("Minutes worked in this session: %s" % minutes_worked)
			print("*******")
			timesheet.append({
			"task": task,
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
		print("[1] Start tracking.")
		print("[2] Show schedule.")
		if os.name =='nt':
			char = 'C'
		else:
			char = 'D'
		x = int(input("\nEnter an option (Ctrl+%s to exit): " % (char)))
		if x == 1:
			sch = select_schedule()
			if sch != False:
				start_tracking(sch)
		elif x == 2:
			print("Scheduled Tasks")
			print("---------------")
			set_schedule()
			for item in config.schedule:
				print("%s (%s mins): %s:%s" % (item['start'].strftime("%H:%M"), item['duration'], item['category'], item['name']))
			print("\n")
		else:
			break

if __name__ == "__main__":
	print("")
	main()