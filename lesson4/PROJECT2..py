passenger_name = "divansh"       
destination = "mumbai"            
ticket_price = 875.50        
number_of_tickets = 5          
is_available = True             
 
print("Passenger Name:", passenger_name)
print("Destination:", destination)
print("Ticket Price: Rs", ticket_price)
print("Number of Tickets:", number_of_tickets)
print("Tickets Available?", is_available)
 
print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))
 
total_cost = ticket_price * number_of_tickets
discount = 85.50
final_cost = total_cost - discount
 
print("\nTotal Cost: Rs", total_cost)
print("Discount: Rs", discount)
print("Final Cost: Rs", final_cost)
 
print("Double Ticket Price: Rs", ticket_price * 2)
print("Ticket Price After Rs1 Increase: Rs", ticket_price + 1)
print("Half Ticket Price: Rs", ticket_price / 2)
 
print("\nIs ticket price under Rs1000?", ticket_price < 1000)
print("Are more than 2 tickets booked?", number_of_tickets > 2)
print("Is destination mumbai?", destination == "mumbai")
print("Is final cost more than Rs20000?", final_cost > 20000)
 
travel_message = passenger_name + " is travelling to " + destination + "."
print("\nTravel Message:", travel_message)
 
print("Destination in uppercase:", destination.upper())
print("Passenger name in lowercase:", passenger_name.lower())
 
morning_ticket_price = 800
evening_ticket_price = 1000
 
print("\nBefore Swapping:")
print("Morning Ticket Price: Rs", morning_ticket_price)
print("Evening Ticket Price: Rs", evening_ticket_price)
 
print("\nAfter Swapping:")
print("Morning Ticket Price: Rs", morning_ticket_price)
print("Evening Ticket Price: Rs", evening_ticket_price)
 
print("\n================================")
print("TRAVEL TICKET SUMMARY")
print("================================")
print("Passenger:", passenger_name)
print("Destination:", destination)
print("Tickets Booked:", number_of_tickets)
print("Final Amount to Pay: Rs", final_cost)
print("Booking Confirmed?", is_available)