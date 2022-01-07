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
        
        #filter unknown cameras
        self.filters['camera__camera_model__isnull']=False
        
        cameras = Camera.objects.all()
        photos = Image.objects.filter(**self.filters)
        
        photos_cam = photos.values('date_taken__date', 'camera__camera_model').annotate(total=Count('date_taken__date')).order_by('date_taken__date')
        photos_tot = photos.values('date_taken__date').annotate(total=Count('date_taken__date')).order_by('date_taken__date')      

        streams = {}
        
        #get a proper dictionary to enable .get()
        total_dict = {}

        for photo in photos_tot:
            total_dict[photo.get('date_taken__date')] = photo.get('total')
        #     print(photo.get('date_taken__date'), photo.get('total'))
            
        # print('---------------')
        
                
        for photo_cam in photos_cam:

            cam_model = photo_cam.get('camera__camera_model')
            
            cam = streams.get(cam_model)
            
            if not cam:
                streams[cam_model] = DateSeries()
                cam = streams.get(cam_model)
            
            cam.dates.append(photo_cam.get('date_taken__date'))
            
            count_total = total_dict.get(photo_cam.get('date_taken__date'))
            
            if count_total == 0 and photo_cam.get('total') > 0:
                raise ValueError('No total found for: ' + photo_cam.get('date_taken__date') + 'but photos from ' + cam_model)
            
            cam.values.append(photo_cam.get('total') / count_total)
            cam.texts.append(photo_cam.get('total'))
            
        
        for key, obj in streams.items():
            self.fig.add_trace(go.Bar(name=key,
                               x=obj.dates,
                               y=obj.values))       
        
        #@TODO:
        # - auf % umstellen
        # texte/hover anpassen
        # farben
        self.fig.update_layout(barmode='relative')    

