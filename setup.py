from setuptools import setup, find_packages

setup(
    name='reckitt_rnd_project',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=4.0',
        'djangorestframework',
        # ... your other deps
    ],
)
