def assign_grade(score):
    if score < 0 or score > 100:
        print("Invalid score! Please enter a value between 0 and 100.")
    elif score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
        
assign_grade(89)
assign_grade(64)
assign_grade(97)
assign_grade(77)