from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


from EmployeeApp.models import Department
from EmployeeApp.serializers import DepartmentSerializer
# Create your views here.


@csrf_exempt
def departmentapi(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                department = Department.objects.get(pk=id)  # type: ignore[attr-defined]
                serializer = DepartmentSerializer(department)
                return JsonResponse(serializer.data, safe=False, status=200)
            except ObjectDoesNotExist:
                return JsonResponse({'message': 'Department not found.'}, status=404)
        else:
            departments = Department.objects.all()               # type: ignore[attr-defined]

            serializer = DepartmentSerializer(departments, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Department created successfully.', 'data': serializer.data}, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        if id is None:
            return JsonResponse({'message': 'ID is required for update.'}, status=400)
        try:
            department = Department.objects.get(pk=id)# type: ignore[attr-defined]
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Department not found.'}, status=404)
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(department, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Department updated successfully.', 'data': serializer.data}, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        if id is None:
            return JsonResponse({'message': 'ID is required for deletion.'}, status=400)
        try:
            department = Department.objects.get(pk=id) # type: ignore[attr-defined]
            department.delete()
            return JsonResponse({'message': 'Department deleted successfully.'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Department not found.'}, status=404)

            # INSERT_YOUR_CODE
from .models import Employees
from .serializers import EmployeeSerializer

@csrf_exempt
def employeesapi(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                employee = Employees.objects.get(pk=id)  # type: ignore[attr-defined]
                serializer = EmployeeSerializer(employee)
                return JsonResponse(serializer.data, safe=False, status=200)
            except ObjectDoesNotExist:
                return JsonResponse({'message': 'Employee not found.'}, status=404)
        else:
            employees = Employees.objects.all()  # type: ignore[attr-defined]
            serializer = EmployeeSerializer(employees, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Employee created successfully.', 'data': serializer.data}, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        if id is None:
            return JsonResponse({'message': 'ID is required for update.'}, status=400)
        try:
            employee = Employees.objects.get(pk=id)  # type: ignore[attr-defined]
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Employee not found.'}, status=404)
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(employee, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Employee updated successfully.', 'data': serializer.data}, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        if id is None:
            return JsonResponse({'message': 'ID is required for deletion.'}, status=400)
        try:
            employee = Employees.objects.get(pk=id)  # type: ignore[attr-defined]
            employee.delete()
            return JsonResponse({'message': 'Employee deleted successfully.'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Employee not found.'}, status=404)

            # INSERT_YOUR_CODE
            

@csrf_exempt
def savefile(request):
    if request.method == 'POST' and request.FILES.get('file'):
        image = request.FILES['file']
                    # Save the image to the default storage (MEDIA_ROOT)
        file_name = default_storage.save(image.name, ContentFile(image.read()))
        return JsonResponse({'fileName': file_name}, status=201)
    return JsonResponse({'message': 'No image uploaded.'}, status=400)


