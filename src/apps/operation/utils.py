
# Create file path for user recoveries
def upload_recovery_image(instance, path):
    phone_num = instance.recovery_process.user.get_phone_number()

    return f'images/recoveries/{phone_num}/{path}'


# Create file path for user routines
def upload_routine_image(instance, path):
    phone_num = instance.user.get_phone_number()

    return f'images/routines/{phone_num}/{path}'
