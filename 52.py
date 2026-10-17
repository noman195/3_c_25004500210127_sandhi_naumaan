class Academic:
        def score(self): return 85
class Sports:
        def sports_score(self): return 90
class Result(Academic,Sports):
        def total(self): return self.score()+self.sports_score()
r=Result(); print("Academic",r.score(),"Sports",r.sports_score(),"Total",r.total())