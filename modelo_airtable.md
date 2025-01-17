from pyairtable.orm import Model
from pyairtable.orm import fields as F

class Profesor(Model):
    num_empleado     = F.TextField('num_empleado')
    grado = F.SelectField('grado')
    nombre = F.TextField('nombre')
    apellidos = F.TextField('apellidos')
    es_prodep  = F.CheckboxField('es_prodep')
    division = F.TextField('division')
    class Meta:
        api_key = 'patjXYNaB6OslrJQT.e07924f5190173607585aad092bb5744213a6b9eab8416f489158220245269fd'
        base_id = 'appkdrgj9qjMwaTkr'
        table_name = 'profesor'
