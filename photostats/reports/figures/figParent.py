from plotly.offline import plot
from plotly.graph_objects import Figure

class FigParent:
    
    def __init__(self, filters):
        
        self.fig = Figure()
        self.title = ''
        
        
        self.filters={}
        for key, value in filters.items():            
            self.filters[key]=value
        
        self.calculate()
        
    def calculate(self):
        pass
    
    def plot(self):
        return plot(self.fig, output_type='div')