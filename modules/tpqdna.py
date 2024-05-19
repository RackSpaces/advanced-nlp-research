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

