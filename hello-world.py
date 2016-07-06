import os
import sys
import django

if __name__ == '__main__':
    print('{}'.format(os.path.split(sys.argv[0])[1]))
    print('Django version is {}'.format(django.get_version()))
