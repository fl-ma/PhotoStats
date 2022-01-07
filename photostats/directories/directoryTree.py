from .models import Directory


class DirectoryTreeElement:
    
    def __init__(self, dir_obj: Directory):
        self.key   = dir_obj.pk
        
        # self.title = get_title(dir_obj, prefix)
        self.title = str(dir_obj)
    
# Tree idea pause for now due to complexity
# if I choose a subfolder to be selectable but not it's parent. how to handle?


# def get_title(dir_obj, prefix):
#     if prefix:
#         title = prefix + ' ' + str(dir_obj)
    
#     else:
#         title = str(dir_obj)
        
#     return title


# def get_dir_and_children(parent: Directory, prefix = '') -> list:
    
#     dirs = []    
#     dirs.append(DirectoryTreeElement(parent, prefix))
    
#     children_db = Directory.objects.filter(parent=parent)
    
#     if not prefix:
#         childPrefix = ' -'
    
#     else:
#         childPrefix = prefix + '-'
    
    
#     for child in children_db:
#         dirs.append(DirectoryTreeElement(child, childPrefix))
        
#         get_dir_and_children(child, childPrefix)
    
#     return dirs


def get_directory_tree_list():
    
    dirs_db = Directory.objects.filter(selectable = True)
        
        
    dirs = []
        
    for dir in dirs_db:
        dirs.append(DirectoryTreeElement(dir))
        
        # children = get_dir_and_children(dir, '')            
        # dirs.extend(children)
        
    return dirs

def selection_to_filter(input):
    
    pk = int(input)
    selection = Directory.objects.get(pk=pk)
    
    pk_list = [selection.pk]
    
    pk_list.extend( read_dir_and_children(selection))
    
    return {'path__pk__in': pk_list}


def read_dir_and_children(parent: Directory):
    
    children = Directory.objects.filter(parent=parent)
    
    pk_list = []
    
    for child in children:
        pk_list.append(child.pk)
        
        pk_list.extend(read_dir_and_children(child))
        
    return pk_list
    
    
        

    