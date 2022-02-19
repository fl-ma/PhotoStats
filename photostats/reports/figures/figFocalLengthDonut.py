from plotly.offline import plot
import plotly.graph_objs as go

from .figParent import FigParent
from images.models import Image
from ..repConstants import COLOUR_BLUE


class FocalLengthDonut(FigParent):

    def calculate(self):

        val = {}
        self.filters['camera__camera_make'] = 'Canon'

        img_list = Image.objects.filter(**self.filters)
        map = {}
        myColorsDict = {}

        for img in img_list:
            key, text = get_range(img.focal_length)

            if key in val:
                val[key] += 1
            else:
                map[key] = text
                val[key] = 1

            if key not in myColorsDict:
                myColorsDict[key] = get_color_for_low(key)

        myKeys = []
        myValues = []
        myLabels = []
        myColors = []

        colorKey = sorted(myColorsDict.keys())

        for color in colorKey:
            myColors.append(myColorsDict[color])

        pass

        for idx, key in enumerate(sorted(val)):
            myKeys.append(key)
            myLabels.append(map.get(key))
            myValues.append(val[key])
            myColors.append(COLOUR_BLUE[idx])

        self.total_number = img_list.count()

        self.fig = go.Figure(data=[go.Pie(
            labels=myLabels,
            values=myValues,
            hole=.3,
            direction='clockwise',
            sort=False,
            marker={
                'colors': myColors
            }
        )])


def get_range(int):

    low = int - (int % 10)
    high = low + 9

    return low, (str(low) + "-" + str(high) + " mm")


def get_color_for_low(low):
    idx = int(low/10)
    return COLOUR_BLUE[idx]
