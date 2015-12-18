import unittest
from app.project import Project, Agent



class ProjectTest(unittest.TestCase):
    def test_create_project(self):
        project = Project('banana', 'cultivo', 100)
        self.assertEqual(project.name, 'banana')

    def test_give_project_with_activity_cultivo_return_the_category_I(self):
        project = Project('banana', 'cultivo')
        self.assertEqual(project.get_category(),'I')

    def test_give_project_with_activity_mineria_return_the_category_II(self):
        project = Project('banana', 'mineria')
        self.assertEqual(project.get_category(),'II')

    def test_give_project_with_activity_exploitation_return_the_category_II(self):
        project = Project('banana', 'exploitation')
        self.assertEqual(project.get_category(),'III')

    def test_give_project_category_III_return_agent_MAE(self):
        project = Project('banana', 'exploitation')
        agent = Agent('MAE')
        self.assertEqual(project.get_agent(), agent)

    def test_give_project_category_I_return_agent_DP(self):
        project = Project('banana', 'cultivo')
        agent = Agent('DP')
        self.assertEqual(project.get_agent(), agent)

    def test_give_project_category_II_return_agent_GAD(self):
        project = Project('banana', 'mineria')
        agent = Agent('GAD')
        self.assertEqual(project.get_agent(), agent)

    def test_give_project_category_I_and_intersected_return_agent_MAE(self):
        project = Project('la granja', 'cultivo', 10, True)
        agent = Agent('MAE')
        self.assertEqual(project.get_agent(), agent)

    def test_give_project_category_II_and_intersected_return_agent_MAE(self):
        project = Project('la granja', 'mineria', 20, True)
        agent = Agent('MAE')
        self.assertEqual(project.get_agent(), agent)

