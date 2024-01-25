# AuthorName: Tanay Patel
# AppName: M02LabCaseStudy.py
# This is a simple program that takes student information as input and provides recognition based on GPA.
# Infinite loop to continuously input student data until the last name "ZZZ" is entered.


while True:
  # Input for student's last name.
  stdlastname = input("\nEnter student's last name: ")
  
  # Check if the last name is "ZZZ" to exit the loop.
  if stdlastname == "ZZZ":
    print("\n")
    break
  
  # Input for student's first name.
  stdfirstname = input("Enter student's first name: ")
  
  # Input for student's GPA
  stdgpa = float(input("Enter student's GPA: "))
  
  # Check if the student's GPA is equal to or greater than 3.5 and print Dean's list recognition.
  if stdgpa >= 3.5:
    print("The student has made the Dean's list.")
  
  # Check if the student's GPA is equal to or greater than 3.25 and print Honor Roll recognition.
  if stdgpa >= 3.25:
    print("The student has made the Honor Roll.")
  
  # Print a newline for better readability before the next iteration.
  print("\n")
