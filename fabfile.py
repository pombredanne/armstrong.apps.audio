from armstrong.dev.tasks import *

full_name= 'armstrong.apps.audio'

settings = {
    'DEBUG': True,
    'INSTALLED_APPS': (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'armstrong.core.arm_content',
        full_name,
        'armstrong.core.arm_sections',
        'south',
    ),
    'ROOT_URLCONF': 'armstrong.core.arm_content.tests.arm_content_support.urls',
}

main_app = "audio"
tested_apps = (main_app, )
