import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="kyberz",
    version="0.0.1",
    author="Garvit Prasad",
    author_email="garvitpd789@gmail.com",
    packages=["Kyberz"],
    description="Implementation of Kyber a post quantum encryption algorithim ",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/garvitxx18/Kyber",
    license='MIT',
    python_requires='>=3.8',
    install_requires=['numpy']
)
