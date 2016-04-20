from setuptools import setup
from setuptools import find_packages

from inotifications import __version__

if __name__ == '__main__':

    setup(name='inotifications',
          version=__version__,
          description='Notifications for Jupyter Notebooks',
          setup_requires=['setuptools-markdown'],
          long_description_markdown_filename='README.md',
          url='https://github.com/niloch/inotifications',
          author='csulliva',
          author_email='csulliva@brandeis.edu',
          license='MIT',
          packages=find_packages(),
          install_requires=[
              'ipython>=3.0',
              'notebook>=3.0'
          ],
          zip_safe=False,
          include_package_data=True,
          keywords=['ipython', 'notifications', 'audio', 'alerts', 'jupyter'],
          classifiers=[
              'Development Status :: 3 - Alpha',
              'Intended Audience :: Science/Research',
              'License :: OSI Approved :: MIT License',
              'Topic :: Scientific/Engineering :: Visualization',
              'Programming Language :: Python :: 2',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3',
              "Programming Language :: Python :: 3.3",
              "Programming Language :: Python :: 3.4",
              "Programming Language :: Python :: 3.5",
          ])
