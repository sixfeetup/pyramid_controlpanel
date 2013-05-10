from pyramid.exceptions import ConfigurationError


def add_controlpanel_section(config, schema, override=False):
    controlpanel = config.registry.setdefault('controlpanel', {})
    if schema.name in controlpanel and not override:
        msg = '%s section already implemented by: %s'
        raise ConfigurationError(msg % (schema.name,
                                        schema.path))
    controlpanel[schema.name] = schema
