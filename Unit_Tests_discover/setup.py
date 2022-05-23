from setuptools import setup, find_packages

setup(
    name='One',
    # name = 'mypackage', 

    version='1.0',
    #version = '0.0.1',

    author='Name',
    #author = 'Name'

    packages=find_packages(include=['src.*', 'env_test.*']),
    #packages=['mypackage'],
    #or
    #packages=find_packages(
        #where='.',
        #include=['mypackage*'],  # ["*"] by default
        #exclude=['mypackage.tests'],  # empty by default

    #namespace_packages=['src'],

    install_requires=open('requirements.txt').readlines(),
    #or
    #install_requires=['requests','importlib-metadata; python_version == "3.8"']

    #tests_require=['pytest'],
    #zip_safe=False
)
