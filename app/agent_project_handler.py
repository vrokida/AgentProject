from abc import ABCMeta, abstractmethod


class AgentProjectHandle(object):
    __metaclass__ = ABCMeta

    def __init__(self, agent=None):
        self.nextHandler = agent

    @abstractmethod
    def handle(self, project):
        print('abstract method')
        return None

    def __str__(self):
        return 'es '+self.__class__.__name__



