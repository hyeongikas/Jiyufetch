from setuptools import setup

setup(
    name='jiyufetch',
    version='0.1',
    py_modules=['Main_1', 'ascii_art'],
    entry_points={
        'console_scripts': [
            'jiyufetch=Main_1:main'
        ]
    },
)
