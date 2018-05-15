# PyPomodoro
A small python script for freelancers to track time using the time-tested Pomodoro technique.

PyPomodoro is a small script that beeps every 30 minutes to remind you of your task status. [Pomodoro](https://en.wikipedia.org/wiki/Pomodoro_Technique) is a simple but empirically-tested tool for time management in any kind of project. The premise of the technique is that a project is most efficiently done when it is divided into time-slots of roughly 25 minutes (followed by a 2-3 minute break). In our script, we assume that one slot equals thirty minutes by default, but you can configure it to anything you want in `slot_interval` variable of `config` module.

To install this script, just [download](https://github.com/prahladyeri/PyPomodoro/archive/master.zip) the repo and extract this in a folder.

To use this script, first you have to create a `config.py` file and set a schedule (bunch of tasks with an approximate duration and category) and a `slot_interval` like this:

	schedule = [
		{"name":"idle", "category":"", "duration":30},
		{"name":"work on pomodoro script", "category":"pomodoro", "duration":30},
		{"name":"work on job search", "category": "freelance-jobsearch", "duration":30},
	]
	
	slot_interval = 25 #minutes

After that, you can start the script and choose the option to start tracking:

    python pomodoro.py

Once you start tracking, it beeps every 30 minutes (or whatever is configured in `config.slot_interval`). At the end of each interval, it will save the timesheet locally to a pickle file, `timesheet.pkl` that you can use for analysis later. The timesheet records the task details and the actual duration worked on (start and end times).

	> python pomodoro.py

	[1] Start tracking.
	[2] Show schedule.

	Enter an option (Ctrl+C to exit): 1
	[1] :idle (30 mins)
	[2] pomodoro:work on pomodoro script (30 mins)
	[3] freelance-jobsearch:work on job search (30 mins)

	 Select schedule:1
	Working on :idle
	Started tracking at 15:26
	Beep interval is set to 30

Please note that if you hit `ctrl + c` and cancel the task during tracking, it won't be recorded in the timesheet.
