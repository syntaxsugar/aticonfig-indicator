from setuptools import setup, find_packages
import glob

setup(name='aticonfig-indicator',
      version='0.1dev',
      description='Aticonfig Temp Indicator on Unity desktop.',
      long_description=open('README.rst').read(),
      url='.',
      license='BSD',
      platforms=['Ubuntu'],
      author='Jaromir Fojtu',
      author_email='jaromir.fojtu@gmail.com',
      scripts=["bin/aticonfig-indicator"],
      packages=['aticonfig_indicator'],
      data_files=[("share/icons/ubuntu-mono-dark/apps/24", glob.glob("icons/*")),
                  ("share/icons/ubuntu-mono-light/apps/24", glob.glob("icons/*")),
                  ("share/icons/hicolor/24x24", glob.glob("icons/*")),
      ],
      include_package_data=True,
)