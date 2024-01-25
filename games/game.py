import abc
from turtle import Screen
import os


class GameInterface(metaclass=abc.ABCMeta):

    def __init__(self) -> None:
        self.screen = Screen()
        self.path = os.path.join(os.path.dirname(os.path.realpath("Turtle-Racing-Game")), "assets")

    @classmethod
    def __subclasshook__(cls, __subclass: type) -> bool:
        return (hasattr(__subclass, "config") and
                callable(__subclass.config) and 
                hasattr(__subclass, "play") and
                callable(__subclass.play) and
                hasattr(__subclass, "destroy") and 
                callable(__subclass.destroy) or 
                NotImplemented
        ) 

    @abc.abstractmethod 
    def config(self):
        """Configuration of the game"""
        raise NotImplementedError

    @abc.abstractmethod
    def play(self, **kwargs):
        """Play the game"""
        raise NotImplementedError

    @abc.abstractmethod
    def destroy(self):
        """Destoy window"""
        raise NotImplementedError

