from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'Kyber Encryption Algorithim'

# Setting up
setup(
    name="mini-kyber",
    version=VERSION,
    author="Garvit Prasad",
    author_email="<garvitpd789@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy'],
    keywords=['python', 'cryptography' , 'encryption' , 'quantum' , 'kyber' , 'falcon'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
