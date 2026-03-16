from Person import Person
class Student(Person):
    def __init__(self,name,age,grade,score,code):
        super().__init__(name,age) # Llama al constructor Padre y hereda sus atributos(person)
        self.grade = grade
        self.__score = score
        self.code = code

    def avg_score(self,score1,score2,score3):
       
            if score1 > 5:
                raise ValueError("Score1 no puede ser mayor a 5.")
            if score2 > 5:
                raise ValueError("Score2 no puede ser mayor a 5.")
            if score3 > 5:        
                raise ValueError("Score3 no puede ser mayor a 5.")  
            total= float(score1) + float(score2) + float(score3)
            total = total / 3
            return total
 

    