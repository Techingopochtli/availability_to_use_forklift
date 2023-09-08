from employee import Employee
from flask import request


def fill_employee(response):
    employe1 = Employee(response.get("login"))
    print(response)
    keys = list(response.keys())
    for key in keys:
        print(key)
    print(employe1.id)
