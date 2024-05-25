#
# Wrapper Functions for the
# Dow Jones DNA Snapshot API
#
# The Python Quants GmbH
#
import os
import json
import time
import requests
import avro.schema
import pandas as pd
from avro.io import DatumReader
from avro.datafile import DataFileReader

# snapshot planning
explain_url = 'https://api.dowjones.com/alpha/extractions/documents/_explain'

# analytics end point
analytics_url = 'https://api.dowjones.com/alpha/analytics'

# snapshot creation
snapshot_create_url = 'https://api.dowjones.com/alpha/extractions/documents/'

# snapshot extraction & download list
snapshot_extraction_list_url = 'https://api.dowjones.com/alpha/extractions/'

djdna_avro_schema = {
    "type": "record",
    "name": "Delivery",
    "namespace": "com.dowjones.dna.avro",
    "doc":
        "Avro schema for extraction content used by Dow Jones' SyndicationHub",
    "fields": [
        {"name": "an", "type": ["string", "null"]},
        {"name": "modification_datetime", "type": ["long", "null"]},
        {"name": "ingestion_datetime", "type": ["long", "null"]},
        {"name": "publication_date", "type": ["long", "null"]},
        {"name": "publication_datetime", "type": ["long", "null"]},
        {"name": "snippet", "type": ["string", "null"]},
        {"name": "body", "type": ["string", "null"]},
        {"name": "art", "type": ["string", "null"]},
        {"name": "action", "type": ["string", "null"]},
        {"name": "credit", "type": ["string", "null"]},
        {"name": "byline", "type": ["string", "null"]},
        {"name": "document_type", "type": ["string", "null"]},
        {"name": "language_code", "type": ["string", "null"]},
        {"name": "title", "type": ["string", "null"]},
        {"name": "copyright", "type": ["string", "null"]},
        {"name": "dateline", "type": ["string", "null"]},
        {"name": "source_code", "type": ["string", "null"]},
        {"name": "modification_date", "type": ["long", "null"]},
        {"name": "section", "type": ["string", "