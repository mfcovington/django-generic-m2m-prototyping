#######################################################
# RELATIONSHIPS FOR GENERATING MODEL & ADMIN CLASSES  #
#######################################################
# For example, ('data', 'publications') yields:       #
# - models.DataPublicationsRelationship               #
# - admin.DataPublicationsAdmin                       #
# - admin.DataToPublicationsRelationshipInline        #
# - admin.PublicationsToDataRelationshipInline        #
#######################################################


RELATIONSHIPS = [
    ('data', 'publications'),
    ('data', 'scientists'),
    ('publications', 'scientists'),
]


#######################################################
# CHOICE LIMITS FOR GENERATING MODEL CLASSES          #
#######################################################
# For example, the following would limit the choices  #
# when selecting a related app and its model for a    #
# related_data to the 'Data' and 'DataSet' models in  #
# an app called 'data':                               #
#                                                     #
#     'data': [                                       #
#         {'app_label': 'data', 'model': 'data' },    #
#         {'app_label': 'data', 'model': 'dataset' }, #
#     ],                                              #
#                                                     #
#######################################################


CT_LIMITS = {
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
