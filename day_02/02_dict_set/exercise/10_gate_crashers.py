invited = {"Ana", "Ben", "Carlo", "Dani"}
attended = {"Ben", "Carlo", "Ely"}

# TODO: Who are all the involved members?
involved = invited | attended
print(f"Involved Members: {involved}.")

# TODO: Who was absent?
absent = invited - attended
print(f"Absent: {absent}.")

# TODO: Who gatecrashed?
gatecrashed = attended - invited
print(f"Not enrolled but attended: {gatecrashed}.")

# TODO: Who was invited and attended
proper = invited & attended
print(f"Attended properly: {proper}.")
