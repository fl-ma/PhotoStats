from django.template import loader

from .directoryTree import get_directory_tree_list

def getHtml(div_id, selector_name, title='', selected=None):
    
        template = loader.get_template('directories/block_directory_sel.html')
        
        context = {
            'DivId': div_id,
            'Title': title,
            'SelectorName': selector_name,
            'dirList': get_directory_tree_list(),
        }
        
        return template.render(context)    
    