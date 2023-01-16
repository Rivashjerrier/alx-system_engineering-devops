#!/usr/bin/python3
"""
    This module requests data from a RESTful API
    (https://jsonplaceholder.typicode.com/)
    and returns information about an employees tasks
"""

import requests as req
from sys import argv

if __name__ == "__main__":

    """ Gets employee information """
    emp = req.get("https://jsonplaceholder.typicode.com/users" +
		  argv[1]).json()
    tasks = req.get("https://jsonplaceholder.typicode.com/todos?userId=" +
		   argv[1]).json()
    tasks_done = req.get("https://jsonplaceholder.typicode.com/todos?userId=" +
			 argv[1] + "&completed=true").json

    """ Prints employee information """
    print("Employee {} is done with task({}/{}):"
	  .format(emp.get("name"), len(tasks_done), len(tasks)))
    for task in tasks_done:
	print("/t " + task.get("title"))
