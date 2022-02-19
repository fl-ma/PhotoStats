from django.shortcuts import render


class RepParent():

    def __init__(self, request):
        self.request = request
        self.template_name = ''
        self.context = None

        self.build()

    def build(self):
        pass

    def render(self):
        return render(self.request,
                      self.template_name,
                      self.context
                      )
