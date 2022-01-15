from .repParent import RepParent
from directories.directorySelector import DirectorySelector

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
        
        selRight = DirectorySelector()
        selLeft = DirectorySelector()

        if not action:
            #initialize view
            self.context={
                'FilterLeft':  selLeft.getHtml(div_id='FilterLeft',selector_name=SEL_LEFT, title='Directory 1')   ,
                'FilterRight': selRight.getHtml(div_id='FilterRight',selector_name=SEL_RIGHT, title='Directory 2')   ,
                            }  
            
        elif action == 'Search':
            return self.plot_reports()
            
        else:
            #no idea
            raise ValueError('Action unknown')    
        
    
    def plot_reports(self):
        
        #left column
        selLeft = DirectorySelector(self.request.POST.get(SEL_LEFT))
        
        focalDonutLeft = FocalLengthDonut(selLeft.get_selected_as_filter(), 'focalDonutLeft', title='Focal length distribution')
        
        #right column
        selRight = DirectorySelector(self.request.POST.get(SEL_RIGHT))
        
        focalDonutRight = FocalLengthDonut(selRight.get_selected_as_filter(), 'focalDonutRight', title='Focal length distribution')        
        
        self.context={
                'FilterLeft': selLeft.getHtml(div_id='FilterLeft',selector_name=SEL_LEFT, title='Directory 1'),
                'FilterRight': selRight.getHtml(div_id='FilterRight',selector_name=SEL_RIGHT, title='Directory 2'),
                'FocalLengthDonutLeft_div': focalDonutLeft.plot(), 
                'FocalLengthDonutRight_div': focalDonutRight.plot(),
            }