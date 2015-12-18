from abc import  ABCMeta, abstractmethod


class AgentProjectHandle:
    __metaclass__ = ABCMeta
    @abstractmethod
    def handle(self, netxHandler):
        print('should implement')


