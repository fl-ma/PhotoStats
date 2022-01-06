import plotly.graph_objects as go
from datetime import date, datetime
from django.db.models import Count

from reports.repParent import RepParent
from images.models import Image, Camera


class DateSeries():
    
    def __init__(self):
        self.dates = []
        self.values = []
        self.texts = []
        

class MobileVsCamRatio(RepParent):
    
    def calculate_fig(self): 
        
        self.fig = go.Figure()
        
        cameras = Camera.objects.all()
        
        photos_cam = Image.objects.filter(**self.filters).values('date_taken__date', 'camera__camera_model').annotate(total=Count('date_taken__date')).order_by('date_taken__date')
        photos_tot = Image.objects.filter(**self.filters).values('date_taken__date').annotate(total=Count('date_taken__date')).order_by('date_taken__date')      

        streams = {}
        # total = DateSeries()
        
        #get a proper dictionary to enable .get()
        total_dict = {}

        for photo in photos_tot:
            total_dict[photo.get('date_taken__date')] = photo.get('total')
            # total.dates.append(photo.get('date_taken__date'))
            # total.values.append(photo.get('total'))
            print(photo.get('date_taken__date'), photo.get('total'))
            
        print('---------------')
        
                
        for photo_cam in photos_cam:
            
            #@TODO: replace this by a proper filter earlier
            if not photo_cam.get('camera__camera_model'):
                cam_model = 'Unknown'
                
            else:
                cam_model = photo_cam.get('camera__camera_model')
            
            cam = streams.get(cam_model)
            
            if not cam:
                streams[cam_model] = DateSeries()
                cam = streams.get(cam_model)
            
            cam.dates.append(photo_cam.get('date_taken__date'))
            
            count_total = total_dict.get(photo_cam.get('date_taken__date'))
            
            cam.values.append(photo_cam.get('total') / count_total)
            cam.texts.append(photo_cam.get('total'))
            
        
        for key, obj in streams.items():
            print(key,obj)    
            self.fig.add_trace(go.Bar(name=key,
                               x=obj.dates,
                               y=obj.values))       
        
        #@TODO:
        # - auf % umstellen
        # texte/hover anpassen
        # farben
        self.fig.update_layout(barmode='relative')    

