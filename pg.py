



# Start Your Code here

class parkingGarage():
    
    # updated to intialize w/o any parameters- the parking spaces/tickets are a set number so we don't really need any parameters
    def __init__(self):
        self.tickets = 5
        self.parkingSpaces = [
            {1: 'open', 'paid' : False}, 
            {2: 'open', 'paid' : False}, 
            {3: 'open', 'paid' : False}, 
            {4: 'open', 'paid' : False}, 
            {5: 'open', 'paid' : False}
        ]
        
        #just throwing this in to maybe have some fun with a print statement later; "Look at all the money our parking garage has made!"
        self.bank = 0

    #Helper function to find open spaces    
    def serveSpace(self):
        for x in range(1, 6):
            if self.parkingSpaces[x-1][x] == 'open':
                return x
            elif self.parkingSpaces[x-1][x] == 'full':
                continue
            
    
    def takeTicket(self):
        a = self.serveSpace()
        if a:
            self.tickets -= 1
            self.parkingSpaces[a-1][a] = 'full'
            print(f'Please proceed to spot {a}.  This is your ticket, don\'t forget {a} or you\'re stuck here forever. . . ')
        else:
            print("We're full!  Sorry, better keep looking for a spot to park.")
    


    def payForParking(self):
        pay = int(input('Please enter your ticket #.'))
        z = int(input("Enter an amount of $35 foo! "))
        if z == 35:
            self.parkingSpaces[pay-1]['paid'] = True
            self.bank += z
        else:
            oth = int(input("Let's try this again, gimme what you got."))
            self.parkingSpaces[pay-1]['paid'] = True
            self.bank += oth
        print("Thank you for paying. You get 15mins tops.  Get outta here! ")



    def leaveGarage(self):
        tic = int(input("What's your ticket number?"))
        # if paid- we let them loose and reset
        
    
    def run(self):
        print("Welcome to Tony's yard/event parking!")
        while True:
            menu = input('p to park, pay to pay, l to leave, done to quit')
            # a few things in here makes this a fully functional program.

            # Finish it off!
            # All right here!

        

#This is the execution code here so we can run and see but ideally I'd import this module to another file in the
#  same folder and these 2 lines + an import above would be everything to run the program.   
t = parkingGarage()
t.run()