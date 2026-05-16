def route_ticket(ticket):

    ticket = ticket.lower()

    if "payment" in ticket or "ssl" in ticket:
        return "Security / Payment Team"

    elif "network" in ticket or "internet" in ticket:
        return "Networking Team"

    elif "install" in ticket:
        return "Installation Team"

    elif "sync" in ticket:
        return "Cloud Sync Team"

    else:
        return "General Support"


if __name__ == "__main__":

    query = input("Enter ticket:\n")

    department = route_ticket(query)

    print(f"\nRoute To: {department}")