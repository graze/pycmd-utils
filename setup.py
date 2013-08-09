'''
Setup File
'''
from setuptools import setup
import multiprocessing

setup(name='cmd_utils',
      version='0.1',
      description='Wrapper for subprocess.Popen and paramiko',
      long_description=('Wrapper for subprocess.Popen and paramiko '
                        'to allow easy running of commands locally and '
                        'remotely with error handling'),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 2.7',
          'Intended Audience :: Developers',
      ],
      keywords='cmd shell ssh command run paramiko',
      url='',
      author='Mark Egan-Fuller',
      author_email='',
      license='',
      packages=['cmd_utils'],
      zip_safe=False,
      install_requires=["paramiko"],
      test_suite='nose.collector',
      tests_require=['nose']
      )
