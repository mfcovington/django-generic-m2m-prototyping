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
