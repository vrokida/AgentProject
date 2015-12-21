from app.agent import Agent
from app.agent_mae_project_handle import AgentMaeProjectHandle
from app.agent_project_handler import AgentProjectHandle
from app.agent_dp_project_handle import AgentDPProjectHandle
from app.agent_gad_project_handle import AgentGadProjectHandle

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
        agentGAD = AgentGadProjectHandle()
        agentDP = AgentDPProjectHandle(agentGAD)
        agentMAE = AgentMaeProjectHandle(agentDP)
        agent = agentMAE.handle(self)

        return agent


     #   agentMae.handle()
"""
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
       """




class Pepa:
     if __name__ == '__main__':

        agentGAD = AgentGadProjectHandle()
        agentDP = AgentDPProjectHandle(agentGAD)
        agentMAE = AgentMaeProjectHandle(agentDP)

        project2 = Project('la granja', 'mineria', 20, True)
        a = agentMAE.handle(project2)
        print(a.name)
