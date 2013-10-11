'''
Setup File
'''
from setuptools import setup
import multiprocessing

setup(name='cmd_utils',
      version='0.3.0',
      description='Wrapper for subprocess.Popen and paramiko',
      long_description=('Wrapper for subprocess.Popen and paramiko '
                        'to allow easy running of commands locally and '
                        'remotely with error handling'),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 2.7',
          'Intended Audience :: Developers',
          'Operating System :: Unix',
          'License :: OSI Approved :: MIT License',
      ],
      keywords='cmd shell ssh command run paramiko',
      url='https://github.com/graze/pycmd-utils',
      author='Mark Egan-Fuller',
      author_email='mark.eganfuller@graze.com',
      license='MIT',
      packages=['cmd_utils'],
      zip_safe=False,
      install_requires=["paramiko"],
      test_suite='nose.collector',
      tests_require=['nose']
      )
