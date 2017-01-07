from setuptools import setup, find_packages

setup(name='python_image_utils',
    version='0.0.3',
    description='functions for pulling stakeholder info from websites',
    author='lynzt',
    url='https://github.com/lynzt/python_image_utils',
    packages=['image_utils'],
    install_requires=[
        'Pillow',
    ],
    dependency_links=[
        'git+git://github.com/lynzt/python_file_utils.git',
    ]
)
