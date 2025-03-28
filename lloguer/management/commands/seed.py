from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from lloguer.models import Automobil, Reserva
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Genera automóviles, usuarios y reservas con datos falsos'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Crear 4 Automóviles
        automoviles = []
        for _ in range(4):
            automobil = Automobil.objects.create(
                marca=fake.company(),
                model=fake.word(),
                matricula=fake.license_plate()
            )
            automoviles.append(automobil)

        # Crear 8 Usuarios
        usuarios = []
        for _ in range(8):
            user = User.objects.create_user(
                username=fake.user_name(),
                password=fake.password(),
                email=fake.email()
            )
            usuarios.append(user)

        # Crear 1 o 2 reservas para cada usuario
        for usuario in usuarios:
            num_reservas = random.choice([1, 2])
            for _ in range(num_reservas):
                automobil = random.choice(automoviles) 
                data_inici = fake.date_this_year()
                data_fi = data_inici + timedelta(days=random.randint(1, 7))

                Reserva.objects.create(
                    automobil=automobil,
                    user=usuario,
                    data_inici=data_inici,
                    data_fi=data_fi
                )

        self.stdout.write(self.style.SUCCESS('Datos creados correctamente'))
