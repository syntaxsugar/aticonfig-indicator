from distutils.core import setup

setup(name='aticonfigindicator',
      version='0.1',
      description='Aticonfig Application Indicator for Ubuntu',
      url='.',
      author='.',
      author_email='.',
      package_dir = {'': 'src'},
      #py_modules=['poc', 'machineindex'],
      package_data = {'': ['img/*.png']}
)