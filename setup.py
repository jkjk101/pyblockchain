from setuptools import setup, find_packages

setup(name='pyblockchain',
      version='0.1',
      url='https://github.com/jkjk101/pyblockchain',
      license='MIT',
      author='jkjk101',
      author_email='jksm101852@gmail.com',
      description='',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)
