from turtle import ht
from django.template import loader

from .models import Directory
from .directoryTree import DirectoryTree
from .directoryTreeEl import DirectoryTreeElement

class DirectoryTreeUi():
    
    def __init__(self, request):
        
        self.request = request
        
        test = Directory.objects.get(pk=25)
        
        self.tree = DirectoryTree(None, 0)
        
        
    def render(self):
        
        html_list = []
        
        # skipping root node (as it is empty)
        for child in self.tree.children:
            
            html_list.extend(render_tree(child))

        template = loader.get_template('directories/directory_tree.html')
        
        context = {
            'directory_list' : html_list
        }
        
        return template.render(context, self.request)
    
def render_tree(root):

    #render self
    html_list = []
    html_list.append(render_element(root.element))
    
    #render children (recursive)
    for child in root.children:
        html_list.extend(render_tree(child))
        
    return html_list

def render_element(element):
     
    template = loader.get_template('directories/directory_tree_el.html')
        
    context = {
        'dir': element.model,
        'depth': element.depth,
        }
        
    return template.render(context)   