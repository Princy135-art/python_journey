class scoreboard:
    def __init__(self,score):
        self.__score=score
    def get_score(self):
        return self.__score
s1= scoreboard(0)
print(s1.get_score())

    