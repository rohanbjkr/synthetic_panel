from setuptools import setup, find_packages
import os

# Read long description from README.md safely
this_dir = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(this_dir, 'README.md')
try:
    with open(readme_path, encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''

setup(
    name='synthetic_panel',
    version='0.1.4',
    description='Estimate poverty transition shares using synthetic panel methodology with bootstrapping.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rohan Byanjankar',
    author_email='rohanbjkr@gmail.com',
    url='https://github.com/rohanbjkr/synthetic_panel',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
        'pandas>=1.3.0',
        'scipy>=1.7.0',
        'statsmodels>=0.13.0',
        'tqdm>=4.62.0',
        'joblib>=1.0.0',
        'openpyxl>=3.0.0'
    ],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    license='MIT',
    keywords='poverty synthetic-panel bootstrap estimation econometrics',
    project_urls={
        'Source': 'https://github.com/rohanbjkr/synthetic_panel',
        'Bug Tracker': 'https://github.com/rohanbjkr/synthetic_panel/issues',
    },
)
