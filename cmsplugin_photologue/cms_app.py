from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class PhotologueHook( CMSApp ):
    name = _( "Photologue" )
    urls = ["photologue.urls"]

apphook_pool.register( PhotologueHook )
