def average(marks1: float, marks2: float) -> float:
   
    return (marks1 + marks2) / 2

def main():
    exam1_marks = float(input("Enter a first exam marks: "))
    exam2_marks = float(input("Enter a second exam marks: "))

    final_average = average(exam1_marks, exam2_marks)
    
    print("\n--- Result ---")
    print("Exam 1 Marks:", exam1_marks)
    print("Exam 2 Marks:", exam2_marks)
    print("Final Average Marks:", final_average)

if __name__ == '__main__':
    main()
