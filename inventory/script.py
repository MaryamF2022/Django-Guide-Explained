import os
from django.contrib.auth.models import User
from django.core.files import File
from .models import NewFile
from django.db import transaction
from inventory.models import Band
from django.db import connection

# file_obj = open("C:\\Users\\faris\\OneDrive\\Desktop\\maryam's  site\\practice\\HTML CSS practice\\responsive design.txt" 'rb')
# django_file = File(file_obj, name=os.path.basename(file_obj))

# newrecord = NewFile.objects.create(user=User.objects.get(), upload=django_file)

@transaction.atomic()
def inner_func():
    new_band3 = Band.objects.create(name='Newwwwwwww new new...')
    print("Inner function perform dtata operations")
    transaction.commit()

    

# @transaction.atomic()
# def outer_func():
#     new_band1 = Band.objects.create(name='Newwwww..')
    
#     inner_func()
   
#     raise RuntimeError("An error occurred within the inner block!")
@transaction.atomic()
def perform_nested_transactions():
    # initial_autocommit = transaction.get_autocommit()

    try:
        
        print("Outer atomic block started")
        new_band1 = Band.objects.create(name='Newwwww..')

        
        sid = transaction.savepoint()
        new_band2 = Band.objects.create(name='Newwwwwwww new ...')
        
        print("Inner function perform dtata operations")
        transaction.savepoint_commit(sid)
        print('Inner block changes commited')
        
        new_band3 = Band.objects.create(name='Newwwww.. new new')
        # transaction.commit()
        print("Outer block changes committed")
        raise RuntimeError
    except RuntimeError as e:
        # An error occurred, rollback changes
        # connection.rollback()
        transaction.savepoint_rollback(sid)

        print("Error occurred. Changes rolled back.")

    # finally:
        # Restore initial autocommit state
        # connection.set_autocommit(initial_autocommit)
        
            
        

def perform_dtabase_operation():
    commit_mode = transaction.get_autocommit()
    print(commit_mode)
    try:
        transaction.set_autocommit(False)

        Band.objects.create(name ="Created new band")
        inner_func()
        transaction.commit()
        print("Changes commited successfully")
        raise RuntimeError
        
    except Exception as e:
        transaction.rollback()
        print("Transaction rolled back")
    finally:
        transaction.set_autocommit(True)