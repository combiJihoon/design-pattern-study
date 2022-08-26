
### template method pattern

R = TypeVar("R")

class ProblemSolveResultTemplate(metaclass=ABCMeta):
    def result(self):
        self.preprocessing()
        result = self.build_result()
        self.afterprocessing()
        return result

    def preprocessing(self):
        pass

    def afterprocessing(self, solved_problems: List[SolvedProblemSchema]):
        pass

    @abstractmethod
    def build_result(self) -> R:
        pass
