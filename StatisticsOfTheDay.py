import pandas as pd
class StatisticsOfTheDay:

    def __init__(self,calories,steps,heartfrequency):
        self.calories=calories
        self.steps=steps
        self.heartfrequency=heartfrequency
    
    def save_days_statistics(self,filepath):
        results={"calories": self.calories,"steps": self.steps,"heartfrequency": self.heartfrequency}
        resultsDf=pd.DataFrame(results)
        resultsDf.to_csv(filepath)
        