__author__ = 'Ehsan'
from sqlAPI import SQLAPI

def main ():
    print("Hello there")
    name = '11'
    if (isinstance(name,str)==True):
        print("Ehsan is string")

    obj = SQLAPI()
    # obj.tableCreate()
    obj.insertEmployeesData(11.34, 'Raha','Dar', 'ehsanab', '123345', '23')
    obj.insertVenueData(123, 'UBC')

if __name__ == "__main__":
    main()