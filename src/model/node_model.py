from pydantic import BaseModel


class NodeModel(BaseModel):

    def __hash__(self):
        return hash(tuple(self))

    def __eq__(self, obj):
        if self is obj:
            return True
        if obj is None or not isinstance(obj, self.__class__):
            return False
        return self.dict() == obj.dict()

    def __str__(self):
        return f"{self.__class__.__name__}{self.json(by_alias=True)}"
