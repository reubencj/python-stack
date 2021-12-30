context = {
    'questions': [{
        'id': 1, 
        'content': 'what is your name?'},
        {
         'id':2, 
         'content': 'where are you born?'   
        }
    
    ]
}

# print(context.items()); 

capitals = {"Washington":"Olympia","California":"Sacramento",
"Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}

t = capitals.items()

for k, v in t:
    print(f"the capital of {k} is {v}")