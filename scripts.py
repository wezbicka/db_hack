from datacenter.models import Schoolkid

students = Schoolkid.objects.all()
print(students)
child = Schoolkid.objects.filter(full_name__contains="Фролов Иван")[0]
print(child.full_name)