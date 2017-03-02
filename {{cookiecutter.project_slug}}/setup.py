import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='{{cookiecutter.project_slug}}',
    version='0.0.0',
    packages=find_packages(exclude=["*.swp"]),
    install_requires=[
        'Django',
    ],
    include_package_data=True,
    license='{{cookiecutter.open_source_license}}',  # example license
    description='{{cookiecutter.project_name}}',
    url='https://www.example.com/',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.full_name}}@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8.15',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
