from .repParent import RepParent
from directories.directoryTree import get_directory_tree_list, selection_to_filter

from .figures.figFocalLengthDonut import FocalLengthDonut
from .figures.figMobileVsCam import MobileVsCam
from .figures.figMobileVsCamRatio import MobileVsCamRatio

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
                'dirList': get_directory_tree_list()   ,
                            }  
            
        elif action == 'Search':
            return self.plot_reports()
            
        else:
            #no idea
            raise ValueError('Action unknown')    
        
    
    def plot_reports(self):
        dir_list = get_directory_tree_list()
        
        #left column        
        filter = selection_to_filter(self.request.POST.get('selected_dir_left'))
        
        focalDonutLeft = FocalLengthDonut(filter)
        
        #right column
        filter = selection_to_filter(self.request.POST.get('selected_dir_right'))
        
        focalDonutRight = FocalLengthDonut(filter)        
        
        self.context={
                'FocalLengthDonutLeft_div': focalDonutLeft.plot(), 
                'FocalLengthDonutRight_div': focalDonutRight.plot(),
                'dirList' : dir_list,
            }