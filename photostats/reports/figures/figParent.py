from plotly.offline import plot
from plotly.graph_objects import Figure

from django.template import loader

class FigParent:
    
    def __init__(self, filters, id, title = ''):
        
        self.title = title
        self.id = id
        self.fig = Figure()
        self.total_number = 0
        
        self.filters={}
        for key, value in filters.items():            
            self.filters[key]=value
        
        self.calculate()
        
    def calculate(self):
        pass
    
    def plot(self):
        
        template = loader.get_template('reports/blocks/block_figure.html')
        
        context = {
            'div_id': self.id,
            'Title': self.title,
            'Figure': plot(self.fig, output_type='div'),
            'Count': str(self.total_number),
        }
        
        return template.render(context)