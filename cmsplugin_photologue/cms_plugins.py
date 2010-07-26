from django.conf import settings
from django.forms.widgets import Media
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from models import *
from photologue.models import *

#overrides photologue.urls.SAMPLE_SIZE : 'Number of random images from the gallery to display.'
SAMPLE_SIZE = ":%s" % getattr( settings, 'CMSPLUGIN_PHOTOLOGUE_SAMPLE_SIZE', 3 )

class CMSPhotologueGalleryPlugin( CMSPluginBase ):
    model = PhotologueGalleryPlugin
    name = _( "Photologue Gallery" )
    text_enabled = True
    render_template = "plugins/cmsplugin_photologue/photologue_gallery.html"

    def render( self, context, instance, placeholder ):
        context.update( {'gallery':instance.gallery, 'placeholder':placeholder} )
        context.update( {'queryset': Gallery.objects.filter( is_public=True ), 'allow_empty': True, 'paginate_by': 5, 'sample_size':SAMPLE_SIZE, 'css' : instance.get_css_display()} )
        return context

    def get_plugin_media( self, request, context, plugin ):
        return Media( 
            css={ 'all': ( 'cmsplugin_photologue/css/galleriffic.css', ), },
            js=( 
                 'cmsplugin_photologue/js/jquery.galleriffic.js',
                 'cmsplugin_photologue/js/jquery.opacityrollover.js',
            ) )

plugin_pool.register_plugin( CMSPhotologueGalleryPlugin )


class CMSPhotologuePhotoPlugin( CMSPluginBase ):
    model = PhotologuePhotoPlugin
    name = _( "Photologue Photo" )
    text_enabled = True
    render_template = "plugins/cmsplugin_photologue/photologue_photo.html"

    def render( self, context, instance, placeholder ):
        context.update( {'photo':instance.photo, 'placeholder':placeholder} )
        context.update( {'slug_field': 'title_slug', 'queryset': Photo.objects.filter( is_public=True ), 'is_thumb' : instance.is_thumb, 'css' : instance.get_css_display()} )
        return context

plugin_pool.register_plugin( CMSPhotologuePhotoPlugin )
