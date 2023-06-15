from monuments.models import Monument
from culture.models import Culture
from showplaces.models import Showplace
from .models import HistoricalObject


def transport_data():
    objects = Monument.objects.all()
    for ob in objects:
        HistoricalObject.objects.create(name=ob.name, object_type_id=1, description=ob.description,
                                        picture=ob.picture)
    objects = Showplace.objects.all()
    for ob in objects:
        HistoricalObject.objects.create(name=ob.name, object_type_id=2, description=ob.description,
                                        picture=ob.picture)
    objects = Culture.objects.all()
    for ob in objects:
        HistoricalObject.objects.create(name=ob.name, object_type_id=3, description=ob.description,
                                        picture=ob.picture)
