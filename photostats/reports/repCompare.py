from .repParent import RepParent
from directories.directoryTree import selection_to_filter
from directories.directorySelector import getHtml

from .figures.figFocalLengthDonut import FocalLengthDonut

SEL_LEFT = 'selectorLeft'
SEL_RIGHT = 'selectorRight'

class RepCompare(RepParent):   
    
    def __init__(self, request):
        super().__init__(request)
        self.template_name = "reports/compare.html"
        
    def build(self):
        super().build()
    
        action = self.request.POST.get('search')

        if not action:
            #initialize view
            self.context={
                'FilterLeft':  getHtml(div_id='FilterLeft',selector_name=SEL_LEFT, title='Directory 1')   ,
                'FilterRight': getHtml(div_id='FilterRight',selector_name=SEL_RIGHT, title='Directory 2')   ,
                            }  
            
        elif action == 'Search':
            return self.plot_reports()
            
        else:
            #no idea
            raise ValueError('Action unknown')    
        
    
    def plot_reports(self):
        
        #left column        
        filter = selection_to_filter(self.request.POST.get(SEL_LEFT))
        
        focalDonutLeft = FocalLengthDonut(filter, 'focalDonutLeft')
        
        #right column
        filter = selection_to_filter(self.request.POST.get(SEL_RIGHT))
        
        focalDonutRight = FocalLengthDonut(filter, 'focalDonutRight')        
        
        self.context={
                'FilterLeft': getHtml(div_id='FilterLeft',selector_name=SEL_LEFT, title='Directory 1'),
                'FilterRight': getHtml(div_id='FilterRight',selector_name=SEL_RIGHT, title='Directory 2'),
                'FocalLengthDonutLeft_div': focalDonutLeft.plot(), 
                'FocalLengthDonutRight_div': focalDonutRight.plot(),
            }