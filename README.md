# PyPomodoro
A small python script for freelancers to track time using the time-tested Pomodoro technique.

PyPomodoro is a small script that beeps every 30 minutes to remind you of your task status. [Pomodoro](https://en.wikipedia.org/wiki/Pomodoro_Technique) is a simple but empirically-tested tool for time management in any kind of task or project. The premise of the technique is that a project is most efficiently done when it is divided into time-slots of roughly 25 minutes (followed by a 2-3 minute break).

To use this script, all you have to do is run it and provide a few optional parameters like project name and category. Once you start tracking, it beeps every 30 minutes (it is configurable via the `interval` parameter). To start the script:

    python pomodoro.py