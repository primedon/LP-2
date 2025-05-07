def route_ticket(issue):
    if issue == "login":
        return "Forward to IT Support Team."
    elif issue == "software":
        return "Forward to Software Maintenance Team."
    elif issue == "hardware":
        return "Forward to Hardware Repair Team."
    elif issue == "network":
        return "Forward to Network Administration."
    else:
        return "Escalate to supervisor."

# --- Example Usage ---
issue = input("Enter issue type (login/software/hardware/network): ").lower()
print(route_ticket(issue))
