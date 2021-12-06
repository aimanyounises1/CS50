people = [{"Name" :"Aiman" , "Street" : "Eldaharat"},
          {"Name" :"Amin" , "Street":"Eldahrat"},
]

people.sort(key=lambda person:person['Name'])
print(people)