"""
WSGI config for segimg project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import tensorflow as tf
from django.core.wsgi import get_wsgi_application
from pathlib import Path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'segimg.settings')


BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR = os.path.join(BASE_DIR,'static')

BASE_DIR = Path(__file__).resolve().parent
# model_path = 'static/tfmodels/inception_resnet_v2'
# use file join to join the path
model_path = os.path.join(BASE_DIR,'static','tfmodels','inception_resnet_v2')
print('model_path: ', model_path)
# detector = tf.saved_model.load(model_path).signatures['default']

application = get_wsgi_application()
