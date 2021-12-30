x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30
print(x);
print(students)
print(sports_directory)
print(z)



students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]




def iterateDictionary(some_list):
    for items in some_list:
        message = ''
        for index in range(0,len(items.items())):
            key, value = list(items.items())[index]
            message += f'{key} - {value}'
            if index != len(items.items()) -1:
                message+=', '
        print(message)    
        
iterateDictionary(students)

    

def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])
    

iterateDictionary2('first_name',students)


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f'{len(value)} {key.upper()}')
        for item in value:
            print(item)
        print('\n')

printInfo(dojo)