from crud import create_record, read_records, update_record, delete_record
from log import logger

# 1. Create a new record with invalid mobile number
invalid_mobile_record = {
    'mobile': 123,  # Invalid mobile number (too short)
    'email': 'invalid_email@gmail.com',
    'gender': 'Male',
    'blood_group': 'O+',
    'dob': '1990-01-01'
}
create_record(invalid_mobile_record)

# 2. Create a new record with invalid email
invalid_email_record = {
    'mobile': 919876543210,
    'email': 'invalid_email',  # Invalid email format
    'gender': 'Male',
    'blood_group': 'O+',
    'dob': '1990-01-01'
}
create_record(invalid_email_record)

# 3. Create a new record with invalid gender
invalid_gender_record = {
    'mobile': 919876543211,
    'email': 'b@gmail.com',
    'gender': 'InvalidGender',  # Invalid gender
    'blood_group': 'O+',
    'dob': '1990-01-01'
}
create_record(invalid_gender_record)

# 4. Create a new record with invalid blood group
invalid_blood_group_record = {
    'mobile': 919876543212,
    'email': 'c@gmail.com',
    'gender': 'Female',
    'blood_group': 'InvalidBG',  # Invalid blood group
    'dob': '1990-01-01'
}
create_record(invalid_blood_group_record)

# 5. Create a new record with invalid DOB
invalid_dob_record = {
    'mobile': 919876543213,
    'email': 'd@gmail.com',
    'gender': 'Other',
    'blood_group': 'AB+',
    'dob': '19900101'  # Invalid DOB format
}
create_record(invalid_dob_record)

# 6. Create a valid record
valid_record = {
    'mobile': 919876543214,
    'email': 'e@gmail.com',
    'gender': 'Male',
    'blood_group': 'B+',
    'dob': '1992-02-02'
}
create_record(valid_record)


# 7. Update the valid record with an invalid email
update_record(919876543214, {'email': 'invalid_email'})

# 8. Update the valid record with a valid email
update_record(919876543214, {'email': 'updated_e@gmail.com'})

# 9. Delete the valid record
delete_record(919876543214)

# Read all records after performing operations
records = read_records()
logger.info(f"Final Records: {records}")
