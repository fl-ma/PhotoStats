import plotly.graph_objects as go
from datetime import date, datetime
from django.db.models import Count

from .figParent import FigParent
from images.models import Image, Camera

class MobileVsCam(FigParent):
    
    def calculate(self): 
        
        photos_all = Image.objects.filter(**self.filters)        
        photos = photos_all.values('date_taken__date', 'camera__camera_model').annotate(total=Count('date_taken__date')).order_by('date_taken__date')
        
        cameras = Camera.objects.all()
        
        self.total_number = photos_all.count()
        
        for cam in cameras:
            
            if not cam.camera_model:
                continue
            
            dates = []
            count = []
            
            for img in photos:
                
                if img.get('camera__camera_model') == cam.camera_model:
                    dates.append(img.get('date_taken__date'))
                    count.append(img.get('total'))
                    
            self.fig.add_trace(go.Scatter(
                x=dates, y=count,
                hoverinfo='x+y',
                mode='lines',
                # line=dict(width=0.5, color='rgb(131, 90, 241)'),
                stackgroup="one",
                name=cam.camera_model
            ))        
        
        
        # img_list = Image.objects.all().order_by('date_taken')
        # cameras = Camera.objects.all()
        
        # values = {}
        
        # for cam in cameras:
        #     values[cam.camera_model] = []
                
        # x = []
        # date    = datetime.min.date()
        # idx     = 0
        
        # for img in img_list:
            
        #     #group by date
        #     if date < img.date_taken.date():
        #         date = img.date_taken.date()
        #         x.append(date)
        #         y.append(1)
                
        #         idx = len(x) - 1
            
        #     else:
        #         y[idx] += 1
            
        
        # self.fig.add_trace(go.Scatter(
        #     x=x, y=y,
        #     hoverinfo='x+y',
        #     mode='lines',
        #     line=dict(width=0.5, color='rgb(131, 90, 241)'),
        #     stackgroup='one' # define stack group
        # )) 
            
            
        # x=['Winter', 'Spring', 'Summer', 'Fall']
        # self.fig.add_trace(go.Scatter(
        #     x=x, y=[40, 60, 40, 10],
        #     hoverinfo='x+y',
        #     mode='lines',
        #     line=dict(width=0.5, color='rgb(131, 90, 241)'),
        #     stackgroup='one' # define stack group
        # ))