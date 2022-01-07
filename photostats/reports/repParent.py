from plotly.offline import plot
from plotly.graph_objects import Figure

class RepParent:
    
    def __init__(self, filters):
        
        self.fig = Figure()
        self.title = ''
        
        
        self.filters={}
        for key, value in filters.items():            
            self.filters[key]=value
        
        self.calculate_fig()
        
    def calculate_fig(self):
        pass
    
    def plot(self):
        return plot(self.fig, output_type='div')