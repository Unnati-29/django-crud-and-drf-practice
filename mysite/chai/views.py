from django.shortcuts import render
from urllib3 import request
from .forms import ChaiVarietyForm
from .models import ChaiVariety
from django.shortcuts import get_object_or_404
from .models import ChaiVariety, Store, ChaiReview
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ChaiSerializer, ReviewSerializer
from rest_framework import mixins, generics, viewsets

# Create your views here.
# @api_view(['GET' , 'POST'])
# def chai_api(request):
#    if request.method == 'GET':
#     chais = ChaiVariety.objects.all()

#     serializer = ChaiSerializer(chais,many=True)

#     return Response(serializer.data)
#    if request.method == 'POST':
#     serializer = ChaiSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)

#     return Response(serializer.errors, status=400)


# @api_view(['GET' , 'PUT' , 'DELETE'])
# def chai_detail_api(request, chai_id):

#     chai = get_object_or_404(ChaiVariety,pk=chai_id)
#     if request.method == 'GET':
#         serializer = ChaiSerializer(chai)
#         return Response(serializer.data)

#     elif request.method == 'PUT':

#         serializer = ChaiSerializer(chai,data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':

#         chai.delete()

#         return Response(
#             {"message": "Chai deleted successfully"},status=204)

# mixins

# class ChaiListCreateAPIView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

#     queryset = ChaiVariety.objects.all()
#     serializer_class = ChaiSerializer

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)

# mixins

# class ChaiDetailAPIView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

#     queryset = ChaiVariety.objects.all()
#     serializer_class = ChaiSerializer
#     lookup_field = 'pk'

#     def get(self, request, pk):
#         return self.retrieve(request, pk)

#     def put(self, request, pk):
#         return self.update(request, pk)

#     def delete(self, request, pk):
#         return self.destroy(request, pk)

# generics

# class ChaiListCreateAPIView(
#     generics.ListCreateAPIView
# ):

#     queryset = ChaiVariety.objects.all()
#     serializer_class = ChaiSerializer


# class ChaiDetailAPIView(
#     generics.RetrieveUpdateDestroyAPIView
# ):

#     queryset = ChaiVariety.objects.all()
#     serializer_class = ChaiSerializer
#     lookup_field = 'pk'

class ChaiViewSet(viewsets.ModelViewSet):
    queryset = ChaiVariety.objects.all()
    serializer_class = ChaiSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ChaiReview.objects.all()
    serializer_class = ReviewSerializer

def all_chai(request):
    return render(request, 'chai/all_chai.html')

def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai': chai})

def chai_store_view(request):
    stores = None

    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)

        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']

            print("Selected Chai:", chai_variety)

            stores = Store.objects.filter(
                chai_varieties=chai_variety
            )

            print("Stores:", stores)

    else:
        form = ChaiVarietyForm()

    return render(
        request,
        'chai/chai_stores.html',
        {'form': form, 'stores': stores}
    )

