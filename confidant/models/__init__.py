import time

from pynamodb.exceptions import TableError

from confidant import app
from confidant.models.credential import Credential
from confidant.models.service import Service

# Only used when using dynamodb local
if app.config.get('DYNAMODB_URL'):
    i = 0
    # This loop is absurd, but there's race conditions with dynamodb local
    while i < 5:
        try:
            if not Credential.exists():
                Credential.create_table(
                    read_capacity_units=10,
                    write_capacity_units=10,
                    wait=True
                )
            if not Service.exists():
                Service.create_table(
                    read_capacity_units=10,
                    write_capacity_units=10,
                    wait=True
                )
            break
        except TableError:
            i = i + 1
            time.sleep(2)
