# === PROBLEM 0 ===
# ~ Scenario ~
# You are a software engineer at Ring, the company that makes the
# doorbells with cameras. There is a new feature request for the
# doorbell to greet the person at the door. Your task is to write
# a script that will ask the user their first name, last name,
# and why they're here. After collecting this message, print a
# greeting for the person.
#
# ~ Success Criteria ~
# The script will prompt the user for their first name, last
# name, and why they're here. Then print the message:
#   "Hello, {first_name} {last_name}. We've informed the resident that you're here to {why_theyre_here}."
#
# ~ Example ~
# Scenario 1
#   Inputs:
#     First Name: Hugh
#     Last Name: Janus
#     Why They're Here: drop off a package
#   Output:
#     Hello, Hugh Janus. We've informed the resident that you're here to drop off a package.
# Scenario 2
#   Inputs:
#     First Name: Jenna
#     Last Name: Talia
#     Why They're Here: rob the place
#   Output:
#     Hello, Jenna Talia. We've informed the resident that you're here to rob the place.

# TODO write your code here

fname = input("First Name: ")
lname = input("Last Name: ")
reason = input("Why They're Here: ")

def script(fname, lname, reason):
    print("Hello, " + fname + " " + lname + ". We've informed the resident that you're here to " + reason + ".")

script(fname, lname, reason)