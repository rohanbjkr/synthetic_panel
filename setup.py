from setuptools import setup, find_packages

setup(
    name='synthetic_panel',
    version='0.1.1',
    description='Estimate poverty transition shares using synthetic panel methodology with bootstrapping.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Rohan Byanjankar',
    author_email='rohanbjkr@gmail.com',
    url='https://github.com/yourusername/synthetic_panel',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'statsmodels',
        'tqdm',
        'joblib',
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
)
