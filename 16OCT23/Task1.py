# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:

# input- score - 89
# output- B

per=float(input("Enter your Percentage : "))

if per >=90 and per <=100:
    print(f'Your grade is A')
elif per >=80 and per <=89:
    print(f'Your grade is B')
elif per >=70 and per <=79:
    print(f'Your grade is C')
elif per >=60 and per <=69:
    print(f'Your grade is D')
else:
    print(f'Your grade is E')


