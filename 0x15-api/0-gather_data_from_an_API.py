#!/usr/bin/python3
""" Returns emp TODO list progress using REST API """

import requests as req
from sys import argv

if __name__ == "__main__":
    emp = req.get("https://jsonplaceholder.typicode.com/users" +
		  argv[1]).json()
    tasks = req.get("https://jsonplaceholder.typicode.com/todos?userId=" +
		   argv[1]).json()
    tasks_done = req.get("https://jsonplaceholder.typicode.com/todos?userId=" +
			 argv[1] + "&completed=true").json

    print("Employee {} is done with task({}/{}):"
	  .format(emp.get("name"), len(tasks_done), len(tasks)))
    for task in tasks_done:
	print("/t " + task.get("title"))
