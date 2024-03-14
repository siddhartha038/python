
def display_ticket(passenger_name, train_name, seat_number):
    print("-------------------------------")
    print("|         TRAIN TICKET        |")
    print("-------------------------------")
    print(f"Passenger Name: {passenger_name}")
    print(f"Train Name: {train_name}")
    print(f"Seat Number: {seat_number}")
    print("-------------------------------")

# Example usage
passenger_name = input("Enter passenger name: ")
train_name = input("Enter train name: ")
seat_number = input("Enter seat number: ")

display_ticket(passenger_name, train_name, seat_number)
