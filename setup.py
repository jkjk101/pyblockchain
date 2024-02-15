from setuptools import setup, find_packages


setup(name='blockchain',
      version='0.1',
      url='https://github.com/jkjk101/blockchain',
      license='MIT',
      author='jkjk101',
      author_email='jksm101852@gmail.com',
      description='',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)