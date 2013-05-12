from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from sixfeetup.bowab.db import Base
from sixfeetup.bowab.configuration import require_csrf

from pyramid_controlpanel.views import ControlPanel
from pyramid_controlpanel.configuration import add_controlpanel_section


def includeme(config):
    config.include('sixfeetup.bowab')
    config.add_models('pyramid_controlpanel.models')
    config.add_directive('add_controlpanel_section', add_controlpanel_section)
    config.add_route('control_panel', '/control_panel')
    config.add_view(ControlPanel,
                    attr="get", request_method='GET',
                    route_name='control_panel',
                    permission='admin',
                    http_cache=0,
                    renderer='templates/control_panel.pt')
    config.add_view(ControlPanel,
                    attr="post", request_method='POST',
                    route_name='control_panel',
                    permission='admin',
                    decorator=[require_csrf],
                    http_cache=0,
                    renderer='templates/control_panel.pt')


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)

    # Includes for any packages that hook into configuration.
    config.include('pyramid_tm')
    config.include('sixfeetup.bowab')

    # Extending an existing package allows you to override
    # view mappings and other configuration details.
    # config.include('base_package_name')

    # overriding templates should be done as follows:
    # config.override_asset('base_package_name:templates/base.pt',
    #                       'pyramid_controlpanel:templates/override.pt')

    # Configuring URLs
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()

    return config.make_wsgi_app()
