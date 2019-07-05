import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='aiosteam',
    version='0.0.2a',
    author='truedl',
    description='An asynchronous steam API wrapper written in Python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/truedl/aiosteam',
    packages=['aiosteam'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
