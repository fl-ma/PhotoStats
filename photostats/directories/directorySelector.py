from django.template import loader

from .models import Directory
from .directoryTree import get_directory_tree_list, read_dir_and_children


class DirectorySelector():
    
    def __init__(self, selected=None):
        self.selected_pk = selected

    def getHtml(self, div_id, selector_name, title=''):
    
        template = loader.get_template('directories/block_directory_sel.html')
        
        if self.selected_pk:
            selectedDir = int(self.selected_pk)
        else:
            selectedDir = None
        
        context = {
            'DivId': div_id,
            'Title': title,
            'SelectorName': selector_name,
            'dirList': get_directory_tree_list(),
            'Selected': selectedDir,
        }
        
        return template.render(context)
    
    
    def get_selected_as_filter(self):
        
        if not self.selected_pk:
            raise ValueError("Nothing selected")
    
        selection = Directory.objects.get(pk=int(self.selected_pk))
        
        pk_list = [selection.pk]
        
        pk_list.extend( read_dir_and_children(selection))
        
        return {'path__pk__in': pk_list}