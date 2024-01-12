from setuptools import setup

setup(
    name='info',
    version='0.1',
    py_modules=['info'],
    entry_points={
        'console_scripts': [
            'info=info:main',
        ],
    },
)
