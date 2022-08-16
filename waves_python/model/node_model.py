from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class NodeModel:

    def __str__(self):
        return f"{self.__class__.__name__}{self.to_json()}"


