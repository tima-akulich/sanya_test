from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.generics import RetrieveAPIView

# Create your views here.
from my_app.models import SomeModel
from my_app.serializers import SomeModelSerializer


class SomeModelListAPIView(ListAPIView):
    queryset = SomeModel.objects.all()
    serializer_class = SomeModelSerializer


class SomeModelRetrieveAPIView(RetrieveAPIView):
    serializer_class = SomeModelSerializer

    def get_object(self):
        return get_object_or_404(SomeModel, pk=self.kwargs['pk'])

