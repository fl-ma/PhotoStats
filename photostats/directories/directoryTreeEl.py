from .models import Directory


class DirectoryTreeElement:

    def __init__(self, model: Directory, depth: int):
        self.model = model
        self.depth = depth

        if model:
            self.title = str(model)

        else:
            self.title = ''
