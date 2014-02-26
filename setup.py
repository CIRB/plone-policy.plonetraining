from setuptools import setup, find_packages
import os

version = '1.3.3'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='policy.plonetraining',
      version=version,
      description="'policy of plone training site'",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['policy', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
	  'collective.ckeditor',
	  'collective.contentstats',
	  'collective.easyslider', 
	  'collective.gallery', 
      'collective.galleria',
      'collective.galleriffic',
	  'collective.js.colorpicker',
	  'collective.js.fullcalendar',        
	  'collective.plonefinder',
      'collective.quickupload',
	  'collective.recaptcha',
      'cirb.footersitemap',    
      'products.geoloc',
	  'Products.LinguaPlone',
      'Products.Maps',
      'Products.PloneFormGen',
	  'qi.portlet.TagClouds',
      'quintagroup.analytics',
      'Solgema.fullcalendar',
      'webcouturier.dropdownmenu',
	  'collective.portlet.videoanysurfer',
	  'collective.videoanysurfer',
	  'collective.linguafaq',
      'collective.portlet.twittermultistream',
      'collective.diggdigg',
	  'collective.oembed',
	  'collective.portlet.oembed',
	  'collective.portlet.socialnetworks',
      'fourdigits.portlet.twitter',
      'collective.anysurfer',
      'collective.checktranslated',
      'collective.z3cform.norobots',
      'plonetheme.plonetraining',
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["templer.localcommands"],
      )
