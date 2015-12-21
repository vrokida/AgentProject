from app.agent_project_handler import AgentProjectHandle
from app.agent import Agent

class AgentDPProjectHandle(AgentProjectHandle):
    def handle(self, project):

        if project.get_category() == 'II' or project.is_intersect:
           # print('***DP***'+project.name)
             return Agent('DP')
        else:
            return self.nextHandler.handle(project)
            


