# Train Booking System

## Overview
The Train Booking System is a console-based application written in Python. This application allows users to sign up, log in, book train tickets, view their booked tickets, and cancel their bookings. The system also provides train schedules and available seat information.

## Features
1. **User Management**:
   - User sign-up
   - User login

2. **Train Management**:
   - Display train schedules
   - Display available seats

3. **Ticket Booking**:
   - Book tickets
   - Allocate seats randomly
   - Make payments

4. **Ticket Management**:
   - Display booked tickets
   - Cancel booked tickets

## Classes and Methods

### User Class
Represents a user with attributes and methods for user management.
- **Attributes**:
  - `name`
  - `age`
  - `ID`
  - `phone_number`
  - `email`
  - `booked_tickets`
  - `account`

- **Methods**:
  - `display()`: Displays user information.

### Train Class
Represents a train with attributes and methods for train management and ticket booking.
- **Attributes**:
  - `train_id`
  - `name`
  - `route`
  - `departure_time`
  - `total_seats`
  - `available_seats`
  - `booked_tickets`

- **Methods**:
  - `display_schedule()`: Displays train schedule.
  - `display_available_seats()`: Displays available seats.
  - `book_ticket(num_tickets, user, class_choice, seat_numbers)`: Books tickets.
  - `display_booked_tickets(user)`: Displays booked tickets for a user.

## Functions
- **allocate_seats(train, num_tickets)**: Allocates seats randomly for the booked tickets.
- **cancellation(train, logged_in_user)**: Cancels booked tickets for the logged-in user.
- **login(user_list)**: Logs in a user.
- **signup(user_list)**: Registers a new user.
- **calculate_ticket_price(class_choice, num_tickets)**: Calculates the price of tickets based on class choice.
- **make_payment(price, user_account)**: Processes the payment for the booked tickets.

## Usage
1. **Sign Up**:
   - Users can sign up by providing their name, age, ID, phone number, and email.

2. **Log In**:
   - Users can log in using their name and ID.

3. **Book Tickets**:
   - Users can view train schedules and available seats.
   - Select a class and the number of tickets to book.
   - Make payment and get seats allocated.

4. **View Booked Tickets**:
   - Users can view their booked tickets.

5. **Cancel Tickets**:
   - Users can cancel their booked tickets.

6. **Exit**:
   - Users can exit the application.

## Running the Application
1. Ensure Python is installed on your system.
2. Run the script in a Python environment.


## Notes
- Ensure to handle invalid inputs and edge cases.
- Extend the application with more features as needed.
- This application is for educational purposes and might need further enhancements for production use.
