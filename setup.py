from setuptools import setup, find_packages
 
setup(name='pyhubb',
      version='0.1',
      url='https://github.com/gatlinnewhouse/pyhubb',
      license='MIT',
      author='Gatlin Newhouse',
      author_email='gatlin.newhouse@gmail.com',
      description='Adds python client object and methods to access Hubb.me API enpoint with HTTP gets',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)