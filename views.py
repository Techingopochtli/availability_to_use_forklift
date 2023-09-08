from flask import Blueprint, redirect, url_for, render_template, jsonify, request
import xlwings as xw
from employee import Employee
import functions as f
views = Blueprint(__name__, "views")


@views.route("/", methods=['GET', 'POST'])
def home():

    return render_template("home.html", boolean=True)


@views.route("/submit", methods=['GET', 'POST'])
def submit():

    col = request.form
    f.fill_employee(col)
    new_data_raw = list(request.form.values())
    master_wb = xw.Book("employees.xlsx")
    master_sheets = master_wb.sheets["Empleados"]
    newrow = master_sheets.range("A1").end("down").row + 1
    master_sheets.range(newrow, 1).value = new_data_raw
    master_wb.sheets[0].range('A2').expand('right').copy()
    master_wb.sheets[0].range('A2').expand().paste(paste='formats')
    master_wb.save()

    return render_template("submitted.html", boolean=True)
