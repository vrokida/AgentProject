from app.agent_project_handler import AgentProjectHandle
from app.agent import Agent

class AgentGadProjectHandle(AgentProjectHandle):
    def handle(self, project):
        if project.get_category() == 'I' and not project.is_intersect:
            #print('***GAD***'+project.name)
            return Agent('GAD')
        else:
           # print('-------FIN----------------')
            return None
            


