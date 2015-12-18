from app.agent import Agent

III = 'III'
II = 'II'
I = 'I'


class Project:

    activities = {II: 'mineria', I: 'cultivo', III: 'exploitation'}

    def __init__(self, name, activity, amount=10, is_intersect=False):
        self.name = name
        self.activity = activity
        self.amount = amount
        self.is_intersect = is_intersect

    def get_category(self):
        if self.activity == self.activities[I]:
            return I
        elif self.activity == self.activities[II]:
            return II
        else:
            return III

    def get_agent(self):
        if self.get_category() == III:
            agent = Agent('MAE')
        elif self.get_category() == II and self.is_intersect:
            agent = Agent('MAE')
        elif self.get_category() == I and not self.is_intersect:
            agent = Agent('DP')
        elif self.get_category() == I and self.is_intersect:
            agent = Agent('MAE')
        else:
            agent = Agent('GAD')
        return agent
