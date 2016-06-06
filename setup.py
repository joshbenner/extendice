from setuptools import setup, find_packages

setup(
    name='extendice',
    url='https://github.com/joshbenner/extendice',
    license='MIT',
    author='Josh Benner',
    author_email='josh@bennerweb.com',

    packages=find_packages(),
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=[
        'pyparsing>=1.5'
    ]
)
