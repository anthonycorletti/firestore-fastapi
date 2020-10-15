import sys

from google.cloud import firestore
from mockfirestore import MockFirestore

# Project ID is determined by the GCLOUD_PROJECT environment variable
if "pytest" in sys.argv[0]:
    # testing db
    db = MockFirestore()
else:
    # not a testing db
    db = firestore.Client()  # pragma: no cover
