from plotly.offline import plot
import plotly.graph_objs as go

from reports.repParent import RepParent
from images.models import Image
from .repConstants import COLOUR_BLUE

class FocalLengthDonut(RepParent):
    
    def calculate_fig(self):
        
        val = {}
        img_list = Image.objects.filter(camera__camera_make='Canon')
        map = {}
        
        for img in img_list:
            key, text = get_range(img.focal_length)
            
            if key in val:
                val[key] += 1
            else:
                map[key] = text
                val[key] = 1
                
        myKeys = []
        myValues = []
        myLabels = []
        myColors = []
        
        for idx, key in enumerate(sorted(val)):
            myKeys.append(key)
            myLabels.append(map.get(key))
            myValues.append(val[key])
            myColors.append(COLOUR_BLUE[idx])
        
            
        self.fig = go.Figure(data=[go.Pie(
            labels=myLabels, 
            values=myValues, 
            hole=.3,
            direction ='clockwise',
            sort=False,
            marker =  {
                'colors': myColors
                }
            )])


def get_range(int):
    
    low = int - ( int % 10 )
    high = low + 9
    
    return low, (str(low) + "-" + str(high) + " mm")