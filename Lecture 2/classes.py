class Flight():
    def __init__(self , capacity):
        self.capacity = capacity
        self.passengers =  []
    
    def add_pass(self,passenger):
        if not self.open_seats():
            return False
        self.passengers.append(passenger)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
people = ["Ross" , "Chandler" , "Phoebe" , "Joe" , "Monica"] 

for person in people:
    success = flight.add_pass(person)
    print(success)
    if success:
        print(f"added this {person} successfully")
    else:
        print(f"No seat is available for {person}")