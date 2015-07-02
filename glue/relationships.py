######################################################
# RELATIONSHIPS FOR GENERATED ADMIN & INLINE CLASSES #
######################################################
# For example, ('data', 'publications') yields:      #
# - DataToPublicationsRelationshipInline             #
# - PublicationsToDataRelationshipInline             #
# - DataPublicationsAdmin                            #
######################################################


RELATIONSHIPS = [
    ('data', 'publications'),
    ('data', 'scientists'),
    ('publications', 'scientists'),
]


LIMITS = {
    'data': [
        {'app_label': 'data', 'model': 'data' },
        {'app_label': 'data', 'model': 'dataset' },
    ],
    'publications': [
        {'app_label': 'publication', 'model': 'publication' },
        {'app_label': 'publication', 'model': 'publicationset' },
    ],
    'scientists': [
        {'app_label': 'scientist', 'model': 'scientist' },
    ],
}
