from setuptools import setup, find_packages

setup_requires = [
    ]

install_requires = [
    ]

dependency_links = [
    ]

setup(
    name='things3-wrapper',
    version='0.1',
    description='Things 3 app python wrapper using URL scheme',
    author='jkkwoen',
    author_email='jk.kwoen@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    dependency_links=dependency_links,
    license='MIT',
    )
