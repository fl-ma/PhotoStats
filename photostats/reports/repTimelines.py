from .repParent import RepParent
from directories.directoryTree import selection_to_filter
from directories.directorySelector import getHtml

from .figures.figFocalLengthDonut import FocalLengthDonut
from .figures.figMobileVsCam import MobileVsCam
from .figures.figMobileVsCamRatio import MobileVsCamRatio


SEL_DIR = 'selected_dir'

class RepTimelines(RepParent):
    
    def __init__(self, request):
        super().__init__(request)
        self.template_name = "reports/timelines.html"
        
    def build(self):
        super().build()
    
        action = self.request.GET.get('search')

        if not action:
            #initialize view
            self.context={
                'DirectoryFilter': getHtml(div_id='dir_sel', selector_name=SEL_DIR)
                }  
            
        elif action == 'Search':
            return self.plot_reports()
            
        else:
            #no idea
            raise ValueError('Action unknown')    
        
    
    def plot_reports(self):
        
        filter = selection_to_filter(self.request.GET.get(SEL_DIR))
        
        focalDonut = FocalLengthDonut(filter, 'focalDonut')
        
        mobileVsCam = MobileVsCam(filter, 'mobileVsCam', 'Mobile vs. Camera - absolute')
        
        mobileVsCamRat = MobileVsCamRatio(filter, 'mobileVsCamRat', 'Mobile vs. Camera - ratio')
        
        self.context={
                'FocalLengthDonut_div': focalDonut.plot(), 
                'CamerasOverTime_div': mobileVsCam.plot(),
                'MobileVsCamRatio_div': mobileVsCamRat.plot(),
                'DirectoryFilter': getHtml(div_id='dir_sel', selector_name=SEL_DIR)
            }