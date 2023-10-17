
import random
#-------------------classes------------------------
class User: # user class
    def __init__(self, name, age, ID, phone_number, email):
        self.name = name
        self.age = age
        self.ID = ID
        self.phone_number = phone_number
        self.email = email
        self.booked_tickets = []  # Store booked tickets for each user
        self.account = 5000  # Initialize the user's account balance

    def display(self):
        print(self.name, self.age, self.ID, self.phone_number, self.email)

class Train: # Train class
    def __init__(self, train_id, name, route, departure_time, total_seats, available_seats):
        self.train_id = train_id
        self.name = name
        self.route = route
        self.departure_time = departure_time
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.booked_tickets = {}  # Store booked tickets for each train
#----------------------functions-------------------
    def display_schedule(self): 
        print(f"Train Name: {self.name}")
        print(f"Train ID: {self.train_id}")
        print(f"Departure Time: {self.departure_time}")
        print(f"Route: {', '.join(self.route)}")

    def display_available_seats(self):
        print(f"Train Name: {self.name}")
        print(f"Available Seats: {self.available_seats}/{self.total_seats}")

    def book_ticket(self, num_tickets, user, class_choice,seat_numbers):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            if user.name not in self.booked_tickets:
                self.booked_tickets[user.name] = []
            self.booked_tickets[user.name].append((self.name, class_choice, seat_numbers))
            user.booked_tickets.append((self.name, class_choice, seat_numbers))
            print(f"Successfully booked {num_tickets} tickets for {self.name} in {class_choice} class.")
            print(f"Allocated seats: {seat_numbers}")
        else:
            print(f"Sorry, there are not enough seats available on {self.name}.")


    def display_booked_tickets(self, user):
        if user.name in self.booked_tickets:
            print(f"Booked tickets for {user.name} on {self.name}:")
            for ticket in self.booked_tickets[user.name]:
                print(f"Train: {ticket[0]}, Class: {ticket[1]}, Seats: {ticket[2]}")
        else:
            print(f"No booked tickets found for {user.name} on {self.name}.")

#----------------------------------------------------------------------------
def allocate_seats(train, num_tickets):
    if num_tickets <= train.available_seats:
        seat_numbers = list(range(1, train.available_seats + 1))
        random.shuffle(seat_numbers)
        allocated_seats = seat_numbers[:num_tickets]
        
        seat_numbers = seat_numbers[num_tickets:]
        
        return allocated_seats
    else:
        return None
#-------------------------------------------------------------------------------------

def cancellation(train, logged_in_user):
    if logged_in_user.name in train.booked_tickets:
        print(f"Are you sure you want to cancel your tickets for {logged_in_user.name} on {train.name}?")
        print("1. Yes")
        print("2. No")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            for ticket in train.booked_tickets[logged_in_user.name]:
                train.booked_tickets[logged_in_user.name].remove(ticket)
            train.available_seats += len(train.booked_tickets[logged_in_user.name])
            del train.booked_tickets[logged_in_user.name]
            print(f"Your tickets for {logged_in_user.name} on {train.name} have been cancelled.")
        elif choice == 2:
            pass
#-------------------------------------------------------------------------------------

## User Functions

def login(user_list):
    x = input("Enter your name: ").lower()
    y = int(input("Enter ID: "))

    for user in user_list:
        if x == user.name and y == user.ID:
            print("Login successful!")
            return user  # Return the logged-in user

    print("Invalid login credentials. Please try again.")
    return None  # Return None if login fails

def signup(user_list):
    name = input("Enter your name: ").lower()
    age = int(input("Enter your age: "))
    ID = int(input("Enter your ID: "))
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ").lower()
   
          
    new_user = User(name, age, ID, phone_number, email)
    user_list.append(new_user)
#----------------------------------------------------------------
def calculate_ticket_price(class_choice, num_tickets):
    ticket_prices = {
        1: 450,  # 1st class
        2: 350,  # 2nd class
        3: 250   # 3rd class
    }
    if class_choice in ticket_prices:
        return ticket_prices[class_choice] * num_tickets
    else:
        return None

def make_payment(price, user_account):
    if price is not None and price > 0:
        print(f"Price of tickets: {price} L.E.")
        choice = int(input("Choose a payment method enter 1 for credit and 2 for vodafone Cash): "))
        while True: 
            if choice == 1:
                card_number = input("Enter your card number(16 Numbers): ")
                if len(card_number) == 16 and card_number.isdigit():
                    return card_number
                else:
                    print("Invalid card number.Please enter a 16-digit number.")
                return True
            elif choice == 2:
                print("Transfer money to this number: 01XXXXXXXXX")
                confirmation = input("Enter 'confirm' when payment process is completed: ").lower()
                if confirmation == "confirm":
                    user_account -= price
                    return True
            else:
                print("Invalid payment method.")
#--------------------main code for application------------------

if __name__ == "__main__":
    user_list = []
    train_list = []

    user1 = User("mariam", 19, 1, 1111111, "mariam@gmail.com")
    user2 = User("abdelrahman", 22, 2, 2222222, "abdo@gmail.com")
    user3 = User("fatma", 19, 3, 3333333, "fatma@gmail.com")
    user4 = User("hussein", 15, 4, 4444444, "hussein@gmail.com")
    user5 = User("joudy", 20, 5, 5555555, "joudy@gmail.com")
    user6 = User("am", 20, 6, 5555555, "joudy@gmail.com")

    user_list.extend([user1, user2, user3, user4, user5, user6])

    train1 = Train(
        train_id=88,
        name="Express123",
        route=["Alexandria", "Cairo", "Aswan"],
        departure_time="05:50 AM",
        total_seats=100,
        available_seats=80)
    train_list.append(train1)

    logged_in_user = None  # Initialize the logged-in user variable
    class_choice = 0
    while True:
        if logged_in_user is None:
            print("Welcome to the Booking System!")
            print("Press 1 for Sign-Up.")
            print("Press 2 for Login.")
        else:    
            print(f"Welcome, {logged_in_user.name}!")
            print("Press 3 to Book Tickets.")
            print("Press 4 to Display Booked Tickets.")
            print("Press 5 for cancellation.")
            print("Press 6 to Exit.")
        operation = int(input("Select an operation: "))

        if logged_in_user is None:

            if operation == 1:
                signup(user_list)
                print(f"Signed up Successfully , Please log in to book your tickets.")

            elif operation == 2:
                logged_in_user = login(user_list)
                if logged_in_user:
                    print(f"Logged in as {logged_in_user.name}")


        elif operation == 3:
            if logged_in_user:
                for train in train_list:
                    train.display_schedule()
                    train.display_available_seats()
                    class_choice = int(input("Choose a class (1-3)\n"
                                            "1st class is for 450 L.E\n"
                                            "2nd class is for 350 L.E\n"
                                            "3rd class is for 250 L.E:\n your choice: "))
                    num_tickets_to_book = int(input("Enter the number of tickets you want to book: "))
                    
                    if num_tickets_to_book <= train.available_seats:
                        price = calculate_ticket_price(class_choice, num_tickets_to_book)
                        if price > 0:
                            if make_payment(price, logged_in_user.account):
                                allocated_seats = allocate_seats(train, num_tickets_to_book)
                                if allocated_seats:
                                    train.book_ticket(num_tickets_to_book, logged_in_user, class_choice, allocated_seats)
                                    
                                    print("Your booking process is successful!")
                                else:
                                    print("Failed to allocate seats.")
                            else:
                                print("Payment failed. Insufficient funds.")
                        else:
                            print("Invalid class choice or number of tickets.")
                    else:
                        print("Not enough available seats.")
            else:
                print("Please log in to book tickets.")
        


        elif operation == 4:
            if logged_in_user:
                for train in train_list:
                    train.display_booked_tickets(logged_in_user)
            else:
                print("Please log in to view booked tickets.")




        elif operation == 5:
            if logged_in_user:
                for train in train_list:
                             cancellation(train, logged_in_user)
                         



        elif operation == 6:
             print(f"Goodbye & Good luck {logged_in_user.name}")
             break
        
        else:
            print("Please enter a valid option (1, 2, 3, 4, 5, or 6).")
