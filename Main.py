from Student import Student

s1 = Student("Dani",18,5,4.6,200223501)
try:
    s1.avg_score(4.5, 4.8, 5.1) # Esto generará un ValueError porque score3 es mayor a 5
except ValueError as e:
    print(e)