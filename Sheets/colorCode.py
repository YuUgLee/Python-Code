import datetime

from oauth2client.service_account import ServiceAccountCredentials
import gspread
import gspread_formatting as g

scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('sheets_clients.json', scope)
client = gspread.authorize(creds)
# Accessing specified planner (Make sure it is shared to the program)
spreadsheet = client.open("Planner Spring 2022")
sheet = spreadsheet.sheet1
# Dictionary to convert column number to letter
col_keys = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G"
}


# **********************************************************************************************************************

# **********************************************************************************************************************

# Sorts column by Date
# @param count    -   ending row number
def sortByDate(count):
    sheet.sort((3, 'asc'), range='A2:F' + count)

# **********************************************************************************************************************

# **********************************************************************************************************************

# Sorts column by Date
# @param count    -   ending row number
def sortByWeek(count):
    sheet.sort((1, 'asc'), range='A2:F' + count)


# **********************************************************************************************************************

# **********************************************************************************************************************
# Sorts column by Class
# @param count    -   ending row number

def sortByClass(count):
    sheet.sort((4, 'des'), range='A2:F' + count)


# **********************************************************************************************************************

# **********************************************************************************************************************
# Adds a task to the planner
# @param time       -   date of the added task
# @param section    -   name of class
# @param info       -   description of the class

def addTask(time, section, info):
    values_list = sheet.col_values(3)
    num = len(values_list)
    sheet.update_cell(num + 1, 3, time)
    sheet.update_cell(num + 1, 4, section)
    sheet.update_cell(num + 1, 5, info)
    sheet.update_cell(num + 1, 6, "No")
    sheet.update_cell(num + 1, 2, '=TEXT(C%d,"dddd")' % (num + 1))
    sheet.update_cell(num + 1, 1, "=WEEKNUM(C%d)" % (num + 1))
    val = sheet.cell(num + 1, 1).value
    val = int(val)
    if val % 2 == 0:
        sheet.format("A" + str(num + 1), {
            "backgroundColor": {
                "red": 1.0,
                "green": 1.0,
                "blue": 0.0
            }
        })
    else:
        sheet.format("A" + str(num + 1), {
            "backgroundColor": {
                "red": 0.0,
                "green": 1.0,
                "blue": 0.0
            }
        })


# **********************************************************************************************************************

# **********************************************************************************************************************
# Deletes a task from the planner
# @param row    -   row number of where to delete task

def deleteTask(row):
    cells = sheet.range("A" + str(row) + ":" + "F" + str(row))
    for cell in cells:
        cell.value = ''
    sheet.format("A" + str(row) + ":" + "E" + str(row), {
        "backgroundColor": {
            "red": 1.0,
            "green": 1.0,
            "blue": 1.0
        }
    })
    sheet.update('F'+ str(row), "No")
    sheet.update_cells(cells)


# **********************************************************************************************************************

# **********************************************************************************************************************
# Displays the information from the selected row
# @param row    -   selected row to get information

def showInfo(row):
    cell = []
    for i in range(1, 7):
        cell.append(sheet.cell(row, i).value)
    print("Week: %s Day: %s\nDate: %s\nClass/Section: %s\nDescription: %s\nCompleted?: %s\n" % (
        cell[0], cell[1], cell[2], cell[3], cell[4], cell[5]))


# **********************************************************************************************************************

# **********************************************************************************************************************
# Highlights the rows that are due the next day

def urgency():
    tmrw = datetime.date.today() + datetime.timedelta(days=1)
    today = datetime.date.today()
    tmrw = tmrw.strftime("%#m/%#d/%Y")
    today = today.strftime("%#m/%#d/%Y")
    # print(today, tmrw)
    cells = sheet.findall(str(tmrw))
    # cells2 = sheet.findall(str(tmrw.lstrip("0")))
    # cells.extend(cells2)

    for cell in cells:
        cell1 = col_keys[cell.col - 2] + str(cell.row)
        fmt = g.cellFormat(
            backgroundColor=g.Color(1, 0.7, 0),
        )
        g.format_cell_range(sheet, cell1, fmt)
    cells = sheet.findall(str(today))
    # print(cells)
    try:
        for i in range(len(cells)):
            # print(cells[i].row, cells[i].col)
            if cells[i].row == 1 and cells[i].col == 10:
                cells.pop(i)
    except:
        print()
    for cell in cells:
        # print(cell.col)
        cell1 = col_keys[cell.col - 2] + str(cell.row)
        # print(cell1)
        fmt = g.cellFormat(
            backgroundColor=g.Color(1, 0.3, 0),
        )
        g.format_cell_range(sheet, cell1, fmt)
    # for cell in cells:
    #     cell1 = col_keys[cell.col - 2] + str(cell.row)
    #     val = (sheet.acell(cell1).value)
        # if int(sheet.acell(cell1).value%2) == 0:
        #     fmt = g.cellFormat(
        #         backgroundColor=g.Color(1, 1, 0),
        #     )
        #     g.format_cell_range(sheet, cell1, fmt)
        # else:
        #     cell1 = col_keys[cell.col - 2] + str(cell.row)
        #     fmt = g.cellFormat(
        #         backgroundColor=g.Color(0, 0.8, 0.5),
        #     )
        #     g.format_cell_range(sheet, cell1, fmt)


# **********************************************************************************************************************

# **********************************************************************************************************************
# Complete a task
# @param row    -   Selected row to complete status to "Yes"

def complete(row):
    values_list = sheet.col_values(3)
    num = len(values_list)
    sheet.update_cell(row, 6, "Yes")


# **********************************************************************************************************************

# **********************************************************************************************************************
# Organizes and color codes planner

def organize():
    values_list = sheet.col_values(4)
    num = len(values_list)
    sortByWeek(str(num))
    highlight(str(num))
    sortByClass(str(num))
    colorOrangeRange("CECS 429")
    colorBlueRange("CECS 491B")
    colorPurpleRange("CECS 475")
    colorGreenRange("CECS 478")
    # colorIndigoRange("ENGR 361")
    values_list = sheet.col_values(4)
    num = len(values_list)
    clearCells('', num)
    sortByDate(str(num))

    urgency()


# **********************************************************************************************************************

# **********************************************************************************************************************
# Highlights planner and tasks
# @param count  -   ending row number


def highlight(count):
    sheet.format("C2:E" + count, {
        "backgroundColor": {
            "red": 1.0,
            "green": 1.0,
            "blue": 0.0,
        }
    })
    sheet.format("A2:A" + count, {
        "backgroundColor": {
            "red": 1.0,
            "green": 1.0,
            "blue": 0.0
        }
    })
    values_list = sheet.col_values(1)
    total = int(values_list[len(values_list) - 1])
    weeknum = sheet.acell('J2').value
    # print(weeknum)
    cell_list = sheet.findall(weeknum)
    if cell_list[0].col != 1:
        cell_list.pop(0)
    # print(cell_list)
    # print("A" + str(cell_list[0].row) + ":A" + str(cell_list[len(cell_list) - 1].row))
    if cell_list:
        sheet.format("A" + str(cell_list[0].row) + ":A" + str(cell_list[len(cell_list) - 1].row), {
            "backgroundColor": {
                "red": 0,
                "green": 1.0,
                "blue": 0
            }
        })






    # Add after line 231 to revert back to previous build
    # values_list = sheet.col_values(1)
    # total = int(values_list[len(values_list) - 1])
    # for i in range(0, total + 1, 2):
    #     if i == 0:
    #         continue
    #     cell_list = sheet.findall(str(i))
    #     if not cell_list:
    #         continue
    #     if cell_list[0].col != 1:
    #         cell_list.pop(0)
    #     # print("A" + str(cell_list[0].row) + ":A" + str(cell_list[len(cell_list) - 1].row))
    #     sheet.format("A" + str(cell_list[0].row) + ":A" + str(cell_list[len(cell_list) - 1].row), {
    #         "backgroundColor": {
    #             "red": 1.0,
    #             "green": 1.0,
    #             "blue": 0.0
    #         }
    #     })


# **********************************************************************************************************************

# **********************************************************************************************************************
# Clears color of selected cells after deleting tasks
# @param name   -   name of section or class to find
# @param row    -   max number of rows

def clearCells(name, row):
    sheet.format("A" + str(row+1) + ":E" + str(row+11), {
        "backgroundColor": {
            "red": 1.0,
            "green": 1.0,
            "blue": 1.0
        }
    })
    # values = sheet.findall(name)
    # for cell in values:
    #     if cell.col == 4 and cell.row <= row:
    #         cell1 = col_keys[cell.col - 1] + str(cell.row)
    #         cell2 = col_keys[cell.col] + str(cell.row)
    #         cell3 = col_keys[cell.col + 1] + str(cell.row)
    #         cell4 = col_keys[1] + str(cell.row)
    #         cell5 = col_keys[6] + str(cell.row)
    #         fmt = g.cellFormat(
    #             backgroundColor=g.Color(1, 1, 1),
    #         )
    #         g.format_cell_range(sheet, cell1, fmt)
    #         g.format_cell_range(sheet, cell2, fmt)
    #         g.format_cell_range(sheet, cell3, fmt)
    #         g.format_cell_range(sheet, cell4, fmt)
    #         g.format_cell_range(sheet, cell5, fmt)


# **********************************************************************************************************************

# **********************************************************************************************************************
# Colors selected cells with orange
# @param name   -   name of section or class to find


def colorOrangeRange(name):
    values = sheet.findall(name)
    if not values:
        return

    else:
        sheet.format("C" + str(values[0].row) + ":E" + str(values[len(values) - 1].row), {
            "backgroundColor": {
                "red": 1.0,
                "green": 0.5,
                "blue": 0.0
            }
        })
# **********************************************************************************************************************

# **********************************************************************************************************************
# Colors selected cells with green
# @param name   -   name of section or class to find

def colorIndigoRange(name):
    values = sheet.findall(name)
    if not values:
        return
    else:
        sheet.format("C" + str(values[0].row) + ":E" + str(values[len(values) - 1].row), {
            "backgroundColor": {
                "red": 0.0,
                "green": 1.0,
                "blue": 1.0
            }
        })

# **********************************************************************************************************************

# **********************************************************************************************************************
# Colors selected cells with green
# @param name   -   name of section or class to find

def colorGreenRange(name):
    values = sheet.findall(name)
    if not values:
        return
    else:
        sheet.format("C" + str(values[0].row) + ":E" + str(values[len(values) - 1].row), {
            "backgroundColor": {
                "red": 0.0,
                "green": 0.8,
                "blue": 0.5
            }
        })


# **********************************************************************************************************************

# **********************************************************************************************************************
# Colors selected cells with purple
# @param name   -   name of section or class to find

def colorPurpleRange(name):
    values = sheet.findall(name)
    if not values:
        return
    else:
        sheet.format("C" + str(values[0].row) + ":E" + str(values[len(values) - 1].row), {
            "backgroundColor": {
                "red": 0.5,
                "green": 0.4,
                "blue": 1.0
            }
        })


# **********************************************************************************************************************

# **********************************************************************************************************************
# Colors selected cells with blue
# @param name   -   name of section or class to find

def colorBlueRange(name):
    values = sheet.findall(name)
    if not values:
        return
    else:
        sheet.format("C" + str(values[0].row) + ":E" + str(values[len(values) - 1].row), {
            "backgroundColor": {
                "red": 0.0,
                "green": 0.6,
                "blue": 2.0
            }
        })
