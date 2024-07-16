# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys
# import certifi
# from pymongo import MongoClient
# from dotenv import load_dotenv
# ca = certifi.where()
# load_dotenv()
# MONGO_URI=os.getenv('MONGO_URI')
# client = MongoClient(MONGO_URI, tlsCAFile=ca)



# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ReqGenius.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv
# ca = certifi.where()
# load_dotenv()
# MONGO_URI = os.getenv('MONGO_URI')
# client = MongoClient(MONGO_URI, tlsCAFile=ca)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ReqGenius.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as e:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from e
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
