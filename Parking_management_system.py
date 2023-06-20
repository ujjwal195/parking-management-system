import mysql.connector 
import time
from datetime import date


global conn,cursor
conn = mysql.connector.connect(
    host='localhost', database=' parking_system', user='root', password='Us7003513122')
cursor = conn.cursor()


def clear():
  for _ in range(15):
     print()


def introduction():
    msg = '''
          P A R K I N G   M A N A G E M E N T   S Y S T E M 
          
          - An Introduction
          
          Parking is a very big problem in the matro cities, Day by day basis parking system
          are coming up with new technologoes to solve this issue. 

          This project is also trying to solve this simple but very useful information for the parking management.
          The whole database is store in MySQL table ParkingSystem that stores their parking slot information
          as well as how long a vehicle is parked in thier parking area and how much he/she need to pay for that. 

          Besides all these features it also track the total money collected during the period of time with
          its extensive searching and reporting system

          The whole project is divided into four major parts ie addition of data, modification, searching and 
          reporting. all these part are further divided into menus for easy navigation \n\n\n\n'''
    
    for x in msg:
        print(x, end='')
        time.sleep(0.002)
    wait = input('Press any key to continue.....')


def made_by():
    msg = ''' 
            Parking Management system made by           : Ujjwal Sancheti and Shruti Sharma
            Roll No                                     : 22112032 & 22112027
            School Name                                 : CHRIST(deemed to be university)
            
            
            \n\n\n
        '''

    for x in msg:
        print(x, end='')
        time.sleep(0.002)

    wait = input('Press any key to continue.....')

def display_parking_type_records():
    cursor.execute('select * from parking_type;')
    records = cursor.fetchall()
    for row in records:
        print(row)

def display_parking_space_records():
    cursor.execute('SELECT * FROM parking_space;')
    records = cursor.fetchall()
    for row in records:
        print(row)


def login():
    while True:
        clear()
        uname = input('Enter your id :')
        upass = input('Enter your Password :')
        cursor.execute('select * from login where name="{}" and pwd ="{}"'.format(uname,upass))
        cursor.fetchall()
        rows = cursor.rowcount
        if rows!=1:
            print('Invalid Login details..... Try again')
        else:
            print('You are eligible for operating this system............')
            print('\n\n\n')
            print('Press any key to continue...............')
            break


def add_parking_type_record():
    clear()
    display_parking_type_records()
    name = input('Enter New Parking Type: ')
    price =  input('Enter Parking Price per day : ')
    sql = 'insert into parking_type(name,price) values("{}",{});'.format(name,price)
    try:
        cursor.execute(sql)
        print('\n\n New Parking Type added....')
        cursor.execute('select max(id) from parking_type')
        no = cursor.fetchone()
        wait= input('\n\n\nPress any key to continue............')
    except:
        print('Invalid choice. Please try again.')


def add_parking_slot_record():
    clear()
    display_parking_type_records()
    parking_type_id = input('Enter Parking Type: ')
    status = input('Enter current Status ( Open/Full ) :')
    sql = 'insert into parking_space(type_id,status) values \
            ("{}","{}");'.format(parking_type_id,status) 
    try:
        cursor.execute(sql)
        print('\n\n New Parking Space Record added....')
        cursor.execute('select max(id) from parking_space;')
        no = cursor.fetchone()
        print(' Your Parking ID is : {} \n\n\n'.format(no[0]))
        display_parking_type_records()
        wait = input('\n\n\nPress any key to continue............')
    except:
        print('Invalid choice. Please try again.')

def modify_parking_type_record():
    clear()
    print(' M O D I F Y   P A R K I N G   T Y P E  S C R E E N ')
    print('-'*100)
    print('1. Parking Type Name')
    print('2. Parking Price')
    print('3. Delete Parking Type')
    try:
        choice = int(input('Enter your choice: '))
        field = ''
        if choice == 1:
            field = 'name'
        elif choice == 2:
            field = 'price'
        elif choice == 3:
            field = 'delete'
            display_parking_type_records()
        
        park_id = input('Enter Parking Type ID: ')
        if field != 'delete':
            value = input('Enter new value: ')
            sql = 'UPDATE parking_type SET ' + field + ' = "' + value + '" WHERE id = ' + park_id + ';'
        else:
            sql = 'DELETE FROM parking_type WHERE id = ' + park_id + ';'

        cursor.execute(sql)
        print('Record updated successfully................')
        display_parking_type_records()
        wait = input('\n\n\nPress any key to continue............')
    except:
        print('Invalid choice. Please try again.')

def modify_parking_space_record():
    clear()
    print(' M O D I F Y  P A R K I N G   S P A C E   R E C O R D ')
    print('-'*100)
    print('1. Parking Type ID (1-Two Wheeler, 2: Car, 3: Bus, etc)')
    print('2. Status')
    print('3. Delete Parking Space')
    try:
        choice = int(input('Enter your choice: '))
        field = ''
        if choice == 1:
            field = 'type_id'
        elif choice == 2:
            field = 'status'
        elif choice == 3:
            field = 'delete'
            display_parking_space_records()
        
        print('\n\n\n')
        space_id = input('Enter Parking Space ID: ')
        
        if field != 'delete':
            value = input('Enter new value: ')
            sql = 'UPDATE parking_space SET ' + field + ' = "' + value + '" WHERE id =' + space_id + ';'
        else:
            sql = 'DELETE FROM parking_space WHERE id =' + space_id + ';'

        cursor.execute(sql)
        print('Record updated successfully................')
        wait = input('\n\n\nPress any key to continue............')
    except:
        print('Invalid choice. Please try again.')


def add_new_vehicle():
    clear()
    print('Vehicle Login Screen ')
    print('-'*100)
    try:
        vehicle_id = input('Enter Vehicle Number :' )
        display_parking_type_records()
        parking_id = input('Enter Parking ID:')
        entry_date = date.today()
        sql = 'insert into transaction(vehicle_id,parking_id,entry_date) values \
            ("{}","{}","{}");'.format(vehicle_id,parking_id,entry_date)
        cursor.execute(sql)
        cursor.execute('update parking_space set status ="full" where id ={}'.format(parking_id))
        print('\n\n\n Record added successfully.................')
        wait= input('\n\n\nPress any key to continue.....')
    except:
        print('Invalid choice. Please try again.')

def remove_vehicle():
    clear()
    print('Vehicle Logout Screen')
    print('-'*100)
    try:
        vehicle_id = input('Enter vehicle No :')
        exit_date = date.today()
        sql = 'select parking_id,price,entry_date from transaction tr,parking_space ps, parking_type pt \
            where tr.parking_id = ps.id and ps.type_id = pt.id and \
            vehicle_id ="'+vehicle_id+'" and exit_date is NULL;'
        cursor.execute(sql)
        record = cursor.fetchone()
        days = (exit_date-record[2]).days 
        if days ==0:
            days = days+1
        amount = record[1]*days
        clear()
        print('Logout Details ')
        print('-'*100)
        print('Parking ID : {}'.format(record[0]))
        print('Vehicle ID : {}'.format(vehicle_id))
        print('Parking Date : {}'.format(record[2]))
        print('Current Date : {}'.format(exit_date))
        print('Amount Payable : {}'.format(amount))
        wait = input('press any key to continue......')
        # update transaction and parking space tables
        sql1 = 'update transaction set exit_date ="{}" , amount ={} where vehicle_id ="{}" \
                and exit_date is NULL;'.format(exit_date,amount, vehicle_id)
        sql2 =  'update parking_space set status ="open" where id = {}'.format(record[0])
        cursor.execute(sql1)
        cursor.execute(sql2)
        wait = input('Vehicle Out from our System Successfully.......\n Press any key to continue....')
    except:
        print('Invalid choice. Please try again.')

def search_menu():
    clear()
    print(' S E A R C H  P A R K I N G  M E N U ')
    print('1.  Parking ID \n')
    print('2.  Vehicle Parked  \n')
    print('3.  Free Space \n')
    try:
        choice = int(input('Enter your choice :'))
        field = ''
        if choice == 1:
            field = 'id'
        if choice == 2:
            field = 'vehicle No'
        if choice == 3:
            field = 'status'
        value = input('Enter value to search :')
        if choice == 1 or choice==3:
            sql = 'select ps.id,name,price, status \
            from parking_space ps , parking_type pt where ps.id = pt.id AND ps.id ={}'.format(value)
        else:
            sql = 'select id,vehicle_id,parking_id,entry_date from transaction where exit_date is NULL;'

        cursor.execute(sql)
        results = cursor.fetchall()
        records = cursor.rowcount
        for row in results:
            print(row)
        if records < 1:
            print('Record not found \n\n\n ')
        wait = input('\n\n\nPress any key to continue......')
    except:
        print('Invalid choice. Please try again.')

def parking_status(status):
    clear()
    print('Parking Status :',status)
    print('-'*100)
    sql ="select * from parking_space where status ='{}'".format(status)
    try:
        cursor.execute(sql)
        records = cursor.fetchall()
        for row in records:
            print(row)
        wait =input('\n\n\nPress any key to continue.....')
    except:
        print('Invalid choice. Please try again.')

def vehicle_status_report():
    clear()
    print('Vehicle Status - Currently Parked')
    print('-'*100)
    sql='select * from transaction where exit_date is NULL;'
    try:
        cursor.execute(sql)
        records = cursor.fetchall()
        for row in records:
            print(row)
        wait =input('\n\n\nPress any key to continue.....')
    except:
        print('Invalid choice. Please try again.')

def money_collected():
    clear()
    start_date = input('Enter start Date(yyyy-mm-dd): ')
    end_date = input('Enter End Date(yyyy-mm-dd): ')
    sql = "select sum(amount) from transaction where \
          entry_date ='{}' and exit_date ='{}'".format(start_date,end_date)
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        clear()
        print('Total money Collected from {} to {}'.format(start_date,end_date))
        print('-'*100)
        print(result[0])
        wait =input('\n\n\nPress any key to continue.....')
    except:
        print('Invalid choice. Please try again.')

def report_menu():
    try:
        while True:
            clear()
            print(' P A R K I N G    R E P O R T S  ')
            print('-'*100)
            print('1.  Parking Types \n')
            print('2.  Free Space  \n')
            print('3.  Ocupied Space  \n')
            print('4.  Vehicle Status  \n')
            print('5.  Money Collected  \n')
            print('6.  Exit  \n')
            choice = int(input('Enter your choice :'))
            field = ''
            if choice == 1:
                display_parking_type_records()
            if choice == 2:
                parking_status("open")
            if choice == 3:
                parking_status("full")
            if choice == 4:
                vehicle_status_report()
            if choice == 5:
                money_collected()
            if choice ==6: 
                break
    except:
        print('Invalid choice. Please try again.')    



def main_menu():
    clear()
    login()
    clear()
    introduction()
    
    while True:
        clear()
        print(' P A R K I N G   M A N A G E M E N T    S Y S T E M')
        print('*'*100)
        print("\n1.  Add New Parking Type")
        print("\n2.  Add New Parking Slot")
        print('\n3.  Modify Parking Type Record')
        print('\n4.  Modify Parking Slot Record')
        print('\n5.  Vehicle Login ')
        print('\n6.  Vehicle Logout')
        print('\n7.  Search menu')
        print('\n8.  Report menu')
        print('\n9.  Close application')
        print('\n\n')
        choice = input('Enter your choice: ')

        if choice == '1':
            add_parking_type_record()
        elif choice == '2':
            add_parking_slot_record()
        elif choice == '3':
            modify_parking_type_record()
        elif choice == '4':
            modify_parking_space_record()
        elif choice == '5':
            add_new_vehicle()
        elif choice == '6':
            remove_vehicle()
        elif choice == '7':
            search_menu()
        elif choice == '8':
            report_menu()
        elif choice == '9':
            break
        else:
            print('Invalid choice. Please try again.')
            input('\n\nPress Enter to continue...')
    
    made_by()



if __name__ == "__main__":
    main_menu()
