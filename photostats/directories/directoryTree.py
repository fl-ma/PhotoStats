from .models import Directory

from .directoryTreeEl import DirectoryTreeElement


class DirectoryTree:

    def __init__(self, model: Directory, depth: int):
        self.element = DirectoryTreeElement(model, depth)
        self.children = []

        child_models = Directory.objects.filter(parent=model)

        for child_model in child_models:
            child = DirectoryTree(child_model, depth+1)

            self.children.append(child)

    def get_as_list(self):

        list = []

        for child in self.children:
            list.extend(get_tree_list(child))

        return list


def get_tree_list(parent: DirectoryTree):

    list = []

    if parent.element.model.selectable:
        list.append(parent.element)

    for child in parent.children:
        list.extend(get_tree_list(child))

    return list


def read_dir_and_children(parent: Directory):

    children = Directory.objects.filter(parent=parent)

    pk_list = []

    for child in children:
        pk_list.append(child.pk)

        pk_list.extend(read_dir_and_children(child))

    return pk_list
