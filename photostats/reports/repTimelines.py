from .repParent import RepParent
from directories.directoryTree import get_directory_tree_list, selection_to_filter

from .figures.figFocalLengthDonut import FocalLengthDonut
from .figures.figMobileVsCam import MobileVsCam
from .figures.figMobileVsCamRatio import MobileVsCamRatio

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
                'dirList': get_directory_tree_list()   ,
                            }  
            
        elif action == 'Search':
            return self.plot_reports()
            
        else:
            #no idea
            raise ValueError('Action unknown')    
        
    
    def plot_reports(self):
        dir_list = get_directory_tree_list()
        
        filter = selection_to_filter(self.request.GET.get('selected_dir'))
        
        focalDonut = FocalLengthDonut(filter)
        
        mobileVsCam = MobileVsCam(filter)
        
        mobileVsCamRat = MobileVsCamRatio(filter)
        
        self.context={
                'FocalLengthDonut_div': focalDonut.plot(), 
                'CamerasOverTime_div': mobileVsCam.plot(),
                'MobileVsCamRatio_div': mobileVsCamRat.plot(),
                'dirList': dir_list 
            }