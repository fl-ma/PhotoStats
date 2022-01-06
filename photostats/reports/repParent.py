from plotly.offline import plot
from plotly.graph_objects import Figure

class RepParent:
    
    def __init__(self, filters):
        
        self.fig = Figure()
        self.title = ''
        
        
        self.filters={}        
        for filter in filters:            
            self.filters[filter[0]]=filter[1]
        
        self.calculate_fig()
        
    def calculate_fig(self):
        pass
    
    def plot(self):
        return plot(self.fig, output_type='div')