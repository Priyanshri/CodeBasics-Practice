import datetime

class CricketPlayer:
    
    #this is the parameterized constructor method, it is called when an object of the class is created.
    def __init__(self, fname, lname, birth_year, team):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        self.team = team
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_average_score(self):
        return sum(self.scores)/len(self.scores)

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

# The __str__ method is used to define a string representation of the object, which is useful for printing the object. 
    def __str__(self):
        return f"{self.first_name} {self.last_name}, the cricket player from {self.team}"

# operators overloading is used to define the behavior of operators for user-defined classes.
# ( __add__ , __sub__ , __mul__ , __truediv__ , __mod__ , __pow__ , __lshift__ , __rshift__ , __and__ , __or__ , __xor__ , __floordiv__ , __pos__ , __neg__ , __lt__ , __gt__ , __eq__ , __ne__ , __ge__ , __le__ , __contains__ , __getitem__ , __setitem__ , __delitem__ , __iter__ , __next__ , __call__ , __len__ , __reversed__ , __hash__  )

    def __lt__(self, other):
        self_avg_score = self.get_average_score()
        other_avg_score = other.get_average_score()
        return self_avg_score < other_avg_score

    def __eq__(self, other):
        self_age = self.get_age()
        other_age = other.get_age()
        return self_age == other_age

virat = CricketPlayer('virat', 'kohli', 1988, 'India')
virat.add_score(37)
virat.add_score(100)
virat.add_score(23)

david = CricketPlayer('david','warner', 1988, 'australia')
david.add_score(37)
david.add_score(23)
david.add_score(85)

print("Virat avg score: ",virat.get_average_score())
print("David avg score: ", david.get_average_score())

print("Is virat less than david: ", virat < david)