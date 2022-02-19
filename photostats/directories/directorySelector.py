from django.template import loader

from .models import Directory
from .directoryTree import read_dir_and_children, DirectoryTree


class DirectorySelector():
    """Encapsulates directory as selector for reports
    """

    def __init__(self, selected=None):
        self.selected_pk = selected

    def get_html(self, div_id, selector_name, title=''):
        """Return as HTML string
        """
        template = loader.get_template('directories/block_directory_sel.html')

        if self.selected_pk:
            selectedDir = int(self.selected_pk)
        else:
            selectedDir = None

        tree = DirectoryTree(None, 0)

        context = {
            'DivId': div_id,
            'Title': title,
            'SelectorName': selector_name,
            'dirList': tree.get_as_list(),
            'Selected': selectedDir,
        }

        return template.render(context)

    def get_selected_as_filter(self):
        """Return selected directory as django pk filter
        """
        if not self.selected_pk:
            raise ValueError("Nothing selected")

        selection = Directory.objects.get(pk=int(self.selected_pk))

        pk_list = [selection.pk]

        pk_list.extend(read_dir_and_children(selection))

        return {'path__pk__in': pk_list}
