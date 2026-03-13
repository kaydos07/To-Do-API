from .models import task
from .serializer import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status   


@api_view(['GET'])
def get_tasks(request):
    tasks = task.objects.all()
    serialize = TaskSerializer(tasks, many = True)
    return Response(serialize.data)

@api_view(['GET'])
def get_task_detail(request, id):
    try: 
        task_detail = task.objects.get(id=id) 
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(task_detail)
    return Response(serializer.data)

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_task(request, id):
    try:
        task_obj = task.objects.get(id=id)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(task_obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def delete_task(request,id):
    try:
        task_obj = task.objects.get(id=id)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    task_obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    