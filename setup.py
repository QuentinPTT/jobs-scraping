# setup.py
from setuptools import setup, find_packages

setup(
    name='f1_jobs',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'f1-jobs=scripts.run_scraper:main',
        ],
    },
)
