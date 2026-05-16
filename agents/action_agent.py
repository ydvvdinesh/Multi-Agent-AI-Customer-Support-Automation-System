def extract_actions(ticket):

    actions = []

    ticket = ticket.lower()

    if "clear cache" in ticket:
        actions.append("Clear application cache")

    if "disable antivirus" in ticket:
        actions.append("Disable antivirus temporarily")

    if "tls 1.3" in ticket:
        actions.append("Upgrade server to TLS 1.3")

    return actions


if __name__ == "__main__":

    ticket = input("Enter support ticket:\n")

    actions = extract_actions(ticket)

    print("\nActions:\n")

    for action in actions:
        print("-", action)