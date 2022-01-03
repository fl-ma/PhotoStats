import plotly.graph_objects as go
from datetime import date, datetime

from images.models import Image

class MobileVsCam:
    
    def __init__(self):
        
        img_list = Image.objects.all().order_by('date_taken')     
        
        self.fig = go.Figure()
        
        x = []
        y = []
        date    = datetime.min.date()
        idx     = 0
        
        for img in img_list:
            
            #group by date
            if date < img.date_taken.date():
                date = img.date_taken.date()
                x.append(date)
                y.append(1)
                
                idx = len(x) - 1
            
            else:
                y[idx] += 1
            
            # if img.camera_make == 'Canon':
            
        
        self.fig.add_trace(go.Scatter(
            x=x, y=y,
            hoverinfo='x+y',
            mode='lines',
            line=dict(width=0.5, color='rgb(131, 90, 241)'),
            stackgroup='one' # define stack group
        )) 
            
            
        # x=['Winter', 'Spring', 'Summer', 'Fall']
        # self.fig.add_trace(go.Scatter(
        #     x=x, y=[40, 60, 40, 10],
        #     hoverinfo='x+y',
        #     mode='lines',
        #     line=dict(width=0.5, color='rgb(131, 90, 241)'),
        #     stackgroup='one' # define stack group
        # ))