def grade_classifier(score):
    if score >= 90:
        return 'Distinction'
    elif score >= 60:
        return 'Pass'
    else:
        return 'Fail'

print(grade_classifier(100))
print(grade_classifier(90))
print(grade_classifier(89))
print(grade_classifier(65))
print(grade_classifier(30))


scores = [45, 72, 91, 60, 38, 85]

for score in scores:
    print(grade_classifier(score))