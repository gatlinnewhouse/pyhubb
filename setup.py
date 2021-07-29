from setuptools import find_packages, setup

setup(
    name='pyhubb',
    packages=find_packages(include=['pyhubb']),
    version='0.1.0',
    description='Python Library for the Hubb.me API',
    author='Gatlin Newhouse',
    license='MIT',
    install_requires=['requests','json','pickle','collections','os','time','fire'],
    setup_requires=[],
)
