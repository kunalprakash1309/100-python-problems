# Question:
# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" 
# or "Yes", otherwise print "No".

choice = input("Proivde yes or no: ").lower()

output = "Yes" if choice == "yes" else "No"

print(output)
