import os

from setuptools import setup, find_packages

version = '0.1'

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'pyramid_tm',
    'SQLAlchemy',
    'zope.sqlalchemy',
    'waitress',
    ]

setup(
      name='pyramid_controlpanel',
      version=version,
      description='Free-form storage of application-specific variables.',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Six Feet Up, Inc.',
      author_email='info@sixfeetup.com',
      url='https://www.sixfeetup.com',
      keywords='web pyramid deform colander registry control-panel json',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="pyramid_controlpanel",
      entry_points="""\
      [paste.app_factory]
      main = pyramid_controlpanel:main
      [console_scripts]
      initialize_pyramid_controlpanel_db = pyramid_controlpanel.scripts.initializedb:main
      """,
      )
