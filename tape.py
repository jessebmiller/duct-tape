import inspect
from datetime import date
from datetime import timedelta

def yell(on=None):
    if on is None:
        frame = inspect.currentframe()
	_, file_name, line_no, _, _, _  = inspect.getouterframes(frame)[1]
        with open(file_name, "r+") as source_file:
            lines = source_file.readlines()
            yell_date = date.today() + timedelta(days=30)
            lines[line_no - 1] = "yell({}) # {}\n".format(
                yell_date.toordinal(), yell_date.ctime())
            source_file.seek(0)
            source_file.writelines(lines)
    else:
        if date.fromordinal(on) < date.today():
            print "LOOK AT THIS CODE AGAIN!!!, CONSIDER REFACTORING!!!"
