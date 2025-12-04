from abc import ABC, abstractmethod


class Abstract(ABC):
  def invoke(self): pass

  def undo(self): pass


class GenericConcrete(Abstract):
  @abstractmethod
  def invoke(self): pass

  # some default implementation
  @abstractmethod
  def undo(self): pass
  # some default implementation


class Concrete1(GenericConcrete):
  def undo(self): pass

if __name__ == '__main__':
    gc = GenericConcrete()