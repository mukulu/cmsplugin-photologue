BETA

Name: cmsplugin-photologue
Description: for django-cms. provides a plugin bridge between django-cms & django-photologue, for cms plugins, page apphook attachment, and navigation extension
Download: http://bitbucket.org/tehfink/cmsplugin-photologue/

Requirements:
- django-photologue >= trunk r407
- django-cms = trunk
- django = 1.2.1

Setup
- make sure requirements are installed and properly working
- add cmsplugin_photologue to python path
- add 'cmsplugin_photologue' to INSTALLED_APPS
- add ('cmsplugin_photologue.urls', 'Photologue app') to CMS_APPLICATIONS_URLS
- add ('cmsplugin_photologue.menu.get_nodes', 'Photologue app Navigation') to CMS_NAVIGATION_EXTENDERS
- run `python manage.py syncdb` and, if you haven't already, photologue's `python manage.py plinit`
- add plugins to pages, or attach 'Photologue plugin app' and 'Photologue plugin navigation' to a page (you may have to restart server process for urls to an attached page to work, something with how django-cms caches urls)

Versioning:
i'm going to _try_ and track the most recent django-cms release and the current trunk, starting with 2.0.2.
- branches are named based on django-cms; eg: cms-2.X
- releases are tagged based on django-cms; eg: cms-2.0.2

Optional
- the photologue default templates extend a 'base.html', while django-cms uses a default 'index.html'. quick solution: create a 'base.html' placeholder template which extends 'index.html'. see 'cmsplugin_photologue/templates/base.html' for an example.
- recommended: install cms-context_processors (or your own), so {{ site }} will work in photologue pages attached to cms pages. NB: this should be fixed in latest django-cms trunk. does it work for anyone?
- define CMSPLUGIN_PHOTOLOGUE_SAMPLE_SIZE, CMSPLUGIN_PHOTOLOGUE_CSS in settings.py
- copy cmsplugin_photologue/templates/plugins/ to your project directory

Todo:
- create variable to control root view displayed when attaching app to cms page
- define CMSPLUGIN_PHOTOLOGUE_SAMPLE_SIZE per plugin
- cache navigation extenders

Example Projects:
- are stripped down, slightly modified versions of django-cms' example project for each relevant version
- require a virtualenv with the requirements above installed
- should work out of the box
- username/password: admin/password


Examples (settings.py):
CMSPLUGIN_PHOTOLOGUE_CSS = (('0', ''),('1', 'left'),('2', 'right'),('3', 'center'),) )
- adds an optional css class to the gallery or photo enclosing div in the plugin templates

CMSPLUGIN_PHOTOLOGUE_SAMPLE_SIZE = 3
- overrides photologue.urls.SAMPLE_SIZE : 'Number of random images from the gallery to display.'


Note:
This is not great code, but it works. Please tell me how to make it better!
