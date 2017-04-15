import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../..', '.env')
load_dotenv(dotenv_path)

if os.environ.get("LOCAL_DEV") or os.environ.get("CIRCLE_CI"):
    print "loading development settings"
    from .development import *
elif os.environ.get("HEROKU"):
    print "loading production settings"
    from .production import *
else:
    print "Error determining environment"
