'''6. Advanced Grading System
Description: Classify scores into A, B, C, D, F. Bonus: accept plus/minus grading.
Example Input:
Enter score: 87
Expected Output:
Grade: B+'''

def grading(score):
    if score < 0 or score > 100:
        return "Invalid score"
    
    if score >= 90:
        return "Grade: A+"
    elif score >= 85:
        return "Grade: A"
    elif score >= 80:
        return "Grade: B+"
    elif score >= 75:
        return "Grade: B"
    elif score >= 70:
        return "Grade: C+"
    elif score >= 65:
        return "Grade: C"
    elif score >= 60:
        return "Grade: D+"
    elif score >= 50:
        return "Grade: D"
    else:
        return "Grade: F"
    
def main():
    score=int(input("Enter score:"))    
    print(grading(score))

if __name__ == '__main__':
    main()