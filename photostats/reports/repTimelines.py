from .repParent import RepParent
from directories.directorySelector import DirectorySelector

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
        dirSelector = DirectorySelector()

        if not action:
            #initialize view
            self.context={
                'DirectoryFilter': dirSelector.get_html(div_id='dir_sel', selector_name=SEL_DIR)
                }  
            
        elif action == 'Search':
            return self.plot_reports()
            
        else:
            #no idea
            raise ValueError('Action unknown')    
        
    
    def plot_reports(self):
        
        dirSelector = DirectorySelector(selected=self.request.GET.get(SEL_DIR))
        filter = dirSelector.get_selected_as_filter()
        
        focalDonut = FocalLengthDonut(filter, 'focalDonut', 'Focal length distribution')
        
        mobileVsCam = MobileVsCam(filter, 'mobileVsCam', 'Mobile vs. Camera - absolute')
        
        mobileVsCamRat = MobileVsCamRatio(filter, 'mobileVsCamRat', 'Mobile vs. Camera - ratio')
        
        self.context={
                'FocalLengthDonut_div': focalDonut.plot(), 
                'CamerasOverTime_div': mobileVsCam.plot(),
                'MobileVsCamRatio_div': mobileVsCamRat.plot(),
                'DirectoryFilter': dirSelector.get_html(div_id='dir_sel', selector_name=SEL_DIR)
            }