# Procrastination Risk Detector
# This is a program to chek your procrastination level

print("Procrastination Risk Detector")

# Get user inputs
plan = float(input("How many hours did you plan to study today? "))
actual = float(input("How many hours did you actually study? "))
dist = int(input("How many times did you get distracted? "))

# I will store the result in a variable
result = ""   # just initializing it

# Checking the conditions
if actual >= plan and dist <= 1:
    result = "Low Procrastination Risk"
    # debug: print("Inside low risk")   # I forgot to remove this
elif actual >= plan / 2:   # using elif is better because it stops checking
    result = "Moderate Procrastination Risk"
else:
    result = "High Procrastination Risk"

# Now show the report
print("\n----- Study Report -----")
print("Planned hours:", plan)
print("Actual hours:", actual)
print("Distractions:", dist)

print("\nYour Result: %s" % result)

# Extra tip
print("\nTip: Try to reduce distractions and follow your study plan.")

# Say thanks to the user
print("Thanks for using my program!")
