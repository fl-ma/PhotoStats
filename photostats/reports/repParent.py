from plotly.offline import plot
from plotly.graph_objects import Figure

class RepParent:
    
    def __init__(self, title):
        
        self.fig = Figure()
        self.title = title
        
        self.calculate_fig()
        
    def calculate_fig(self):
        pass
    
    def plot(self):
        return plot(self.fig, output_type='div')