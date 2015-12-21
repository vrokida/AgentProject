from app.agent import Agent
from app.agent_project_handler import AgentProjectHandle


class AgentMaeProjectHandle(AgentProjectHandle):
    def __init__(self, agent):
        super(AgentMaeProjectHandle, self).__init__(agent)


    def handle(self, project):
        if project.get_category() == 'III':
            print('*responsability**MAE***')
            return Agent('MAE')
        else:
             return self.nextHandler.handle(project)



