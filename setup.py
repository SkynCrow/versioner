from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
with open('version.txt', 'r', encoding='utf-8') as f:
    version = f.read().strip()
setup(
    name='versioner',
    version=version,
    author='Franco Tardones',
    author_email='ftardones@gmail.com',
    description='A CI/CD base for other projects with deploy, save, run, and setup commands.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/skyncrow/versioner',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'argparse',
    ],
)