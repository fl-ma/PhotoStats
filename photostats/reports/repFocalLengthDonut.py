from plotly.offline import plot
import plotly.graph_objs as go

class FocalLengthDonut:
    
    def __init__(self, img_list):
        
        
        val = {}
        
        for img in img_list:
            key = get_range(img.focal_length)
            
            if key in val:
                val[key] += 1
            else:
                val[key] = 1
        
        myKeys = []
        myValues = []
        
        for key in sorted(val):
            myKeys.append(key)
            myValues.append(val[key])
            
            
        # self.fig = go.Figure(data=[go.Pie(labels=list(val.keys()), values=list(val.values()), hole=.3)])
        self.fig = go.Figure(data=[go.Pie(labels=myKeys, values=myValues, hole=.3)])
        

def get_range(int):
    
    low = int - ( int % 10 )
    high = low + 9
    
    return (str(low) + "-" + str(high) + " mm")