import os
import csv

from django.conf import settings

from . import models


PATCH = settings.BASE_DIR

DIR = os.path.join(
    os.path.dirname(settings.BASE_DIR),
    'deploy/dump/'
)


def load_students():
    with open(DIR + 'students.csv', 'r' ) as theFile:
        reader = csv.DictReader(theFile)
        
        for line in reader:
            print(line.get('discord'))
            
            if line.get('apellido') and line.get('nombres'):

                student = models.Student.objects.create(
                    last_name = line.get('apellido'),
                    first_name = line.get('nombres'),
                    dni = (None, line.get('dni'))[line.get('dni').isdigit()],
                    email = line.get('email'),
                    username_discord = line.get('discord') or None,
                    cellphone = line.get('telefono') or None,
                    )

                teen, created = models.Teen.objects.get_or_create(
                    name = line.get('equipo')
                    )

                teen.students.add(student)

                teen.save()

                # print(line.get('monto'))
                # print(type(line.get('monto')))

                if line.get('monto').isdigit() and line.get('monto').isdigit():
                    
                    models.Payment.objects.create(
                        student = student,
                        value = line.get('monto'),
                        receipt = line.get('comprobante') or None,
                        )

            else:
                print('ERROR')
