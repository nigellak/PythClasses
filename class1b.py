class  Nigella:
    def __init__(self, name, iDno):
        self.stdName = name
        self.stdID = iDno
        return

studentOne = Nigella('King', '0987')
print(studentOne.stdID, studentOne.stdName)

studentTwo = Nigella('Nigella', '1234')
print(studentTwo.stdName, studentTwo.stdID)


class Work:
    def __init__(self, name, iDno):
        self.EmployeeName = name
        self.EmployeeID = iDno
        return

Emp1 = Work('Dale', '3333')
print(Emp1.EmployeeID, Emp1.EmployeeName)