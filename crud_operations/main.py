from crud import create_record, read_records, update_record, delete_record
from log import logger


new_record = { 'mobile': 919876543210,
                'email': 'a@gmail.com',
                'gender': 'Male',
                'blood_group': 'O+',
                'dob': '1990-01-01'}
if create_record(new_record):
    logger.info("New record created")

records = read_records()
logger.info(f"Records: {records}")

# Update a record
updated_record = {
        'email': 'updated_a@gmail.com',
        'gender': 'Other',
        'blood_group': 'A+',
        'dob': '1991-02-02'
    }
if update_record(919876543210, updated_record):
    logger.info("Record updated")

    # Read records again to see the update
records = read_records()
logger.info(f"Records after update: {records}")

# Delete a record
if delete_record(919876543210):
    logger.info("Record deleted")

# Read records again to see the deletion
records = read_records()
logger.info(f"Records after deletion: {records}")
