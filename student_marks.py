# Student Marks Analyzer

# Accept marks for 5 subjects
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))
mark4 = float(input("Enter marks for Subject 4: "))
mark5 = float(input("Enter marks for Subject 5: "))

# Calculate total marks
total = mark1 + mark2 + mark3 + mark4 + mark5

# Calculate percentage
percentage = total / 5

# Calculate grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Display the result
print("\n--- Student Marks Analyzer ---")
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
