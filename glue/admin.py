from django.contrib import admin

from genericadmin.admin import GenericAdminModelAdmin, GenericTabularInline

from .models import (DataPublicationsRelationship, DataScientistsRelationship,
    PublicationsScientistsRelationship)


##############################################
# RELATIONSHIPS FOR GENERATED INLINE CLASSES #
##############################################


relationships = [
    ('data', 'publications'),
    ('data', 'scientists'),
    ('publications', 'scientists'),
]


###########################
# GENERATE INLINE CLASSES #
###########################


def generate_tabular_inline_model(relationship):
    content_1, content_2 = relationship
    klass_name = '{}To{}RelationshipInline'.format(content_1.capitalize(), content_2.capitalize())
    klass = type(
        klass_name,
        (GenericTabularInline,),
        {
            'ct_field': '{}_content_type'.format(content_1.lower()),
            'ct_fk_field': '{}_object_id'.format(content_1.lower()),
            'ordering': ['{}_content_type'.format(content_2.lower())],
            'model': eval('{}{}Relationship'.format(*sorted(map(lambda x: x.capitalize(), r)))),
            '__module__': __name__,
        }
    )
    globals()[klass_name] = klass


for r in relationships:
    generate_tabular_inline_model(sorted(r))
    generate_tabular_inline_model(sorted(r, reverse=True))


#################
# ADMIN CLASSES #
#################


@admin.register(DataPublicationsRelationship)
class DataPublicationsAdmin(GenericAdminModelAdmin):
    pass


@admin.register(PublicationsScientistsRelationship)
class PublicationsScientistsAdmin(GenericAdminModelAdmin):
    pass


@admin.register(DataScientistsRelationship)
class DataScientistsAdmin(GenericAdminModelAdmin):
    pass
