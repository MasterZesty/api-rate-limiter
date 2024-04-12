from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Simple API Rate Limiter for Flask Apps'
LONG_DESCRIPTION = 'Simple API Rate Limiter for Flask Apps'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="api_rate_limiter_for_flask", 
        version=VERSION,
        author="Krishna-Nimbalkar",
        author_email="kgn272000@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'rate-limiting', 'flask-rate-limiting'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)