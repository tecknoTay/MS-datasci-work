#All of the data here is fake data generated or manually inserted.

import csv
import random
from datetime import date
import numpy as np


def employees(cnt1):
    
    data=[]
    data1=[]
    count = cnt1
    
    eName_list = ['Ann', 'Beth','Blaire', 'Claire', 'Dawn', 'Dee', 'Elle', 'Eve', 'Faye', 
                  'Gail', 'Grace', 'Gwen', 'Jane', 'Jean', 'Joy', 'Kate', 'Kim', 'Liv', 
                  'Madge', 'Paige', 'Pearl', 'Rose', 'Ruth', 'Tess', 'Blake', 'Brock',
                  'Cade', 'Cale', 'Chad', 'Chase', 'Clark', 'Cole', 'Drake', 'Grant', 
                  'Heath', 'Jack', 'Jake', 'Kent', 'Kurt', 'Luke', 'Max', 'Neil', 'Rhett',
                  'Ross', 'Todd', 'Trent', 'Vince', 'Holland', 'Kellon', 'Vincent', 'Kandy', 'Yancy']

    glteam_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

    subteam_list = ['Reading', 'General Science', 'Algebra', 'History', 'Spanish', 'Computing', 'P.E.', 'French',
    'Writing', 'Geography', 'Chemisty', 'Physics', 'Art']


    for i in range(1, count):
        emp_id = i + 5
        eName1, eName2, glteam, subteam, name = " ", " ", " ", " ", " "
        eName1 = random.choice(eName_list)
        eName2 = f'{eName1}'
        subteam = random.choice(subteam_list)
        glteam = random.choice(glteam_list)
        

        data1=[(emp_id, subteam, eName1, glteam)]
        data += data1
        data1 = []
       
        
    print(data)
    
    with open('employee.csv','w') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['EmpID', 'Subject_team', 'Name', 'Grade_team'])
        for row in data:
            csv_out.writerow(row)

def customers(cnt2):

    data=[]
    data1=[]
    count = cnt2
    
    custName_list = ['Ami', 'Bn','Blake', 'Clarence', 'Doath', 'Donald', 'Elle', 'Eve', 'Faye', 
                  'Gail', 'Grace', 'Gwen', 'Jane', 'Jean', 'Joy', 'Kate', 'Kim', 'Liv', 
                  'Margret', 'Paige', 'Peter', 'Rose', 'Ruth', 'Tess', 'Blake', 'Brock',
                  'Callie', 'Cane', 'Chad', 'Chanze', 'Clark', 'Cole', 'Drake', 'Grant', 
                  'Heath', 'Jack', 'Jake', 'Kent', 'Kelly', 'Logan', 'Marcy', 'Nelly', 'Rently',
                  'Ross', 'Todd', 'Trent', 'Vince', 'Sandy', 'Billy', 'Pete',]
    
    st_list = ['AL', 'OH', 'AK', 'LA', 'OK', 'AZ', 'ME', 'OR', 'AR', 'MD', 'PA', 'AS', 'MA', 'PR', 'CA', 'MI', 'RI', 'CO', 'MN', 'SC', 'CT', 
                  'MS', 'SD', 'DE'	'MO', 'TN', 'DC', 'MT', 'TX', 'FL', 'NE' 'TT', 'GA', 'NV', 'UT', 'GU', 'NH', 'VT',
                  'HI', 'NJ', 'VA', 'ID', 'NM', 'VI', 'IL', 'NY', 'WA', 'IN', 'NC', 'WV', 'IA', 'ND', 'WI', 'KS'
                  'CM', 'WY']
    
    city_list = ['Ann Arbor', 'Reno', 'Vallejo', 'Springfield', 'North Charleston', 'Santa Rosa', 'Elk Grove',  'Newark',
                 'Newport News', 'Santa Maria', 'Raleigh', 'Billings', 'Las Cruces', 'Edison', 'Vacaville', 
                 'Rochester', 'Santa Clara', 'Manchester', 'San Antonio', 'Montego', 'Austin', 'Dallas', 'Potomic', 'Houma', 'Shrevport'
                 'El Paso', 'Atlanta', 'Chamblee', 'Miami', 'Detroit']
    
    district_list = ['San Bart District', 'South Lake District', 'East Baton District', 'West Turtle District', 'Ten10 District', 
    'OVO District', 'Moore District', 'Redlight District']
    
    
    for i in range(1, count):
        cust_id = i
        custName1, custName2, name, state, city, district = " ", " ", " ", " ", " ", " "
        custName1 = random.choice(custName_list)
        custName2 = f'{custName1}'
        state = random.choice(st_list)
        city = random.choice(city_list)
        district = random.choice(district_list)
        
        
        data1=[(cust_id, custName2, state, city, district)]
        data += data1
        data1 = []
       
    print(data)
    
    with open('customer.csv','w') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['CustID','Name', 'State', 'City', 'District'])
        for row in data:
            csv_out.writerow(row)



def products(cnt2):
    
    data=[]
    data1=[]
    count = cnt2
    
    model_no_list = ['A560', 'S768', 'E220', 'N190', 'C200', 'Y081']
    material_type_list = ['Print Materials', 'Digital Materials']
    subject_list = ['Classic Interface', 'Interactive Interface']
    shipping_address_list = ['1201 W.Elm', '6789 Bird St', '78 Tourist St', '101 Hall Ct', '23 Paul Way', '4325 Thomas Ln',
    '0034 Marcella Ln', '56 KMP Rd', '768 Dancing Way', '2323 Old K Way', '5674 Google St', '2020 ACV Dr.', '21 Lakeview Terrace',
    '80 Eighty Way', '900 Birdwell', '111 Hill Country Way', '303 Michigan Ave', '456 Nunez Way']
    productid_list = np.array(random.sample(list(range(1,50)),10))
    
    for i in range(1, count):
        
        custid = i
        
        model_no, material_type, subject, shipping_address, productid = " ", " ", " ", " ", " "
        model_no = random.choice(model_no_list)
        material_type = random.choice(material_type_list)
        interface_type = random.choice(subject_list)
        shipping_address = random.choice(shipping_address_list)
        productid = random.choice(productid_list)
        
        
        data1=[(productid, shipping_address, model_no, interface_type, material_type, custid)]
        data += data1
        data1 = []
       
        
    #print(data)
   
    with open('product.csv','w') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['ProductID','Shipping Address', 'Model', 'Interface_type', 'Material_type', 'CustID'])
        for row in data:
            csv_out.writerow(row)


def invoices(cnt2):
    
    data=[]
    data1=[]
    count = cnt2
    
    
    for i in range(1, count):
        data1 = []
        custid, empid = i, i + 5
        invid = i + 10
        
        
        start_dt = date.today().replace(day=1, month=1).toordinal() #random date 73 - 76
        end_dt = date.today().toordinal()
        random_day = date.fromordinal(random.randint(start_dt, end_dt))
        rDate = str(random_day)
        data1=[(invid, rDate, custid, empid)]
        data += data1
       
        
    #print(data)
    
    with open('invoice.csv','w') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['InvID','Date','CustID','EmpID'])
        for row in data:
            csv_out.writerow(row)



def main():
   
    count1, count2 = 10000, 5000
    
    employees(count1)
    customers(count2)
    products(count2)
    invoices(count2)


# Driver Code
if __name__ == '__main__':
    main()
    
    
