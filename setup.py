from setuptools import setup


DESCRIPTION = """
commute.py helps users who travel across multiple modes of transport
and multiple waypoints to make data-based decisions about which route
to use and prefer at a given time or at a given time in future.
"""


def readme():
    try:
        import pandoc
    except ImportError:
        return ''
    doc = pandoc.Document()
    with open("README.md") as f:
        doc.markdown_github = f.read()
        return doc.rst

setup(name='commute',
      version='0.2',
      description=DESCRIPTION,
      long_description=readme(),
      url='https://github.com/dhruvbaldawa/commute.py',
      author='Dhruv Baldawa',
      author_email='dhruvbaldawa@gmail.com',
      license='MIT',
      packages=['commute'],
      install_requires=[
          'click',
          'googlemaps',
          'networkx',
          'pyyaml',
          'parsedatetime',
      ],
      entry_points={
          'console_scripts': ['commute=commute.cli:cli'],
      },
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities',
      ],
      keywords='commute googlemaps directions',
      include_package_data=True,
      zip_safe=False)
