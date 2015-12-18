from app.agent_project_handler import AgentProjectHandle



class AgentMaeProjectHandle(AgentProjectHandle):
    def handle(self, nextHandler, project):
        print('***MAE***'+project.name)

