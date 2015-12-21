from app.agent_mae_project_handle import AgentMaeProjectHandle
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
        agent_gad = AgentGadProjectHandle()
        agent_dp = AgentDPProjectHandle(agent_gad)
        agent_mae = AgentMaeProjectHandle(agent_dp)
        agent = agent_mae.handle(self)

        return agent

