from ast import Delete


citizens = [{ 'First Name': 'Preston' , 'Last Name': 'Cunningham', 'Age': 49 , 'Education': 'Doctoral', 'Occupation':' Teacher' ,'Experience (Years)': 6, 'Salary': 62499}, 
 { 'First Name': 'Madaline', 'Last Name': 'Farrell', 'Age': 41, 'Education': 'Bachelor', 'Occupation': 'Insurer','Experience (Years)': 16, 'Salary': 50190},
 { 'First Name': 'Eleanor', 'Last Name': 'Carter', 'Age': 49, 'Education': 'Lower secondary', 'Occupation': 'Programmer','Experience (Years)': 18, 'Salary': 189716},
 { 'First Name': 'Adison', 'Last Name': 'Hall', 'Age': 42 , 'Education': 'Bachelor', 'Occupation': 'Florist','Experience (Years)': 21, 'Salary': 34517},
 { 'First Name': 'Grace', 'Last Name': 'Cooper', 'Age': 49, 'Education': 'Master', 'Occupation': 'Singer','Experience (Years)': 9, 'Salary': 51994},
 { 'First Name': 'Alford', 'Last Name': 'Kelley', 'Age': 49, 'Education': 'Bachelor', 'Occupation': 'Aeroplane Pilot','Experience (Years)': 9, 'Salary': 170466},
 { 'First Name': 'Vincent', 'Last Name': 'Anderson', 'Age': 47, 'Education': 'Master', 'Occupation': 'Botanist','Experience (Years)': 6, 'Salary': 71617},
 { 'First Name': 'Myra', 'Last Name': 'Wright', 'Age': 45, 'Education': 'Master', 'Occupation': 'Geologist' ,'Experience (Years)': 18, 'Salary': 48786},
 { 'First Name': 'Chester', 'Last Name':'Bennett', 'Age': 42, 'Education': 'Doctoral', 'Occupation': 'Astronomer','Experience (Years)': 13, 'Salary': 44826},
 { 'First Name': 'Blake', 'Last Name': 'Tucker', 'Age': 42, 'Education': 'Doctoral', 'Occupation': 'Firefighter','Experience (Years)': 21, 'Salary': 36761},
 { 'First Name': 'Paige', 'Last Name': 'Ryan', 'Age': 43, 'Education': 'Primary', 'Occupation': 'Fine Artist','Experience (Years)': 19, 'Salary': 28181},
 { 'First Name': 'Natalie', 'Last Name': 'Ellis', 'Age': 45, 'Education': 'Bachelor', 'Occupation': 'Baker','Experience (Years)': 0, 'Salary': 31194},
 { 'First Name': 'Martin', 'Last Name': 'Thompson', 'Age': 47, 'Education': 'Bachelor', 'Occupation': 'Journalist','Experience (Years)': 21, 'Salary': 90183},
 { 'First Name': 'Alan', 'Last Name': 'Sullivan', 'Age': 46, 'Education': 'Doctoral', 'Occupation': 'Singer','Experience (Years)': 2, 'Salary': 18440},
 { 'First Name': 'Inga', 'Last Name': 'Bergman', 'Age': 41, 'Education': 'Bachelor', 'Occupation': 'Producer','Experience (Years)': 22, 'Salary': 80029},
 { 'First Name': 'Freddy', 'Last Name': 'Brown', 'Age': 48, 'Education': 'Bachelor', 'Occupation': 'Economist','Experience (Years)': 18, 'Salary': 146217},
 { 'First Name': 'Adelaide', 'Last Name': 'Farrell', 'Age': 42, 'Education': 'Bachelor', 'Occupation': 'Mechanic','Experience (Years)': 9, 'Salary':19414},
 { 'First Name': 'Luke', 'Last Name': 'Cooper', 'Age': 40, 'Education': 'Upper secondary', 'Occupation': 'Producer','Experience (Years)': 17, 'Salary': 160541},
 { 'First Name': 'Sofia', 'Last Name': 'Hall', 'Age': 41, 'Education': 'Doctoral', 'Occupation': 'Baker','Experience (Years)': 1, 'Salary': 25904},
 { 'First Name': 'Ashton', 'Last Name': 'Kelly', 'Age': 49, 'Education': 'Master', 'Occupation': 'Chef','Experience (Years)': 6, 'Salary': 95533}
]

def get_variable (Lista,x):
    variable =[]
    for i in range (len(Lista) ):
        variable.append(Lista[i][x])
    return variable

first_name = get_variable(citizens,'First Name')
last_name = get_variable(citizens,'Last Name')
age = get_variable(citizens,'Age')
education = get_variable(citizens,'Education')
occupation = get_variable(citizens,'Occupation')
experience = get_variable(citizens,'Experience (Years)')
salary = get_variable(citizens,'Salary')

def get_average (Lista):
    suma = 0
    for i in range (len(Lista)):
        suma += Lista[i]
    mean =suma/len(Lista)
    return round(mean,1)

average_age = get_average(age)
print("La media de edad es ",average_age)

def unique (Lista):
    levels = []
    for i in range (len(Lista)):
        if Lista[i] not in levels:
            levels.append(Lista[i])
    return levels

educational_levels = unique(education)
print("Los niveles educacionales que tenemos son: ", educational_levels)
print ("Tenemos ",len(educational_levels)," niveles educacionales")

ocupation_num = unique(occupation)
print("Las ocupaciones que tenemos son: ", ocupation_num)
print("Tenemos ",len(ocupation_num)," ocupaciones")

def list_2 (Lista):
    lista = []
    for i in  range(len(Lista)):
        nd={}
        nd["First Name"] = Lista[i]["First Name"]
        nd["Last Name"] =  Lista[i]["Last Name"]
        nd["Age"] =  Lista[i]["Age"]
        lista.append(nd)
    return lista
print("Lista con nombres, apellidos y edades: ", list_2(citizens))

def salario_medio_ocupacion (Lista):
    lista = []
    for i in range(len(Lista)):
        nd={}
        nd["Occupation"] = Lista[i]["Occupation"]
        nd["Salary"] = Lista[i]["Salary"]
        lista.append(nd)
    return lista
print("Lista con ocupaciones y salarios: ", salario_medio_ocupacion(citizens))