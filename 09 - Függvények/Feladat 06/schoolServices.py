
def calculateGrade(points) -> int:
    grade:int=0
    if(points < 50):
        grade = 1
    elif(points < 60):
        grade = 2
    elif(points < 70):
        grade = 3
    elif(points < 85):
        grade = 4
    elif( points <= 100):
        grade = 5
    return grade
