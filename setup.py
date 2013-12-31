#!/usr/bin/env python


try:
    import setuptools

except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

    import setuptools

import os


parent_directory = os.path.abspath(os.path.dirname(__file__))


meta_files = {
    'README.md': None,
    'CLASSIFIERS': None,
}

for filename in meta_files:
    try:
        current_file = open(os.path.join(parent_directory, filename))
        meta_files[filename] = current_file.read()
        current_file.close()

    except IOError:
        raise IOError('{0} not found.'.format(filename))


# Get our list of classifiers
classifiers = meta_files['CLASSIFIERS'].split('\n')
classifiers.remove('')


setuptools.setup(
    name='approuter',
    description='Routes specific Django applications to specific databases.',
    long_description=meta_files['README.md'],

    version='0.1.0',
    classifiers=classifiers,

    author='Rentlytics, Inc.',
    author_email='engineers@rentlytics.com',
    url='https://github.com/rentlytics/django-approuter/',

    packages=setuptools.find_packages(),
    keywords='django database router',

    zip_safe=False,

    install_requires=[]
)