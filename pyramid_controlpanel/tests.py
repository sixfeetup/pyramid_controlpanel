from unittest import TestCase

from pyramid import testing

from pyramid_controlpanel.views import ControlPanel

from colander import (Integer, Schema, SchemaNode)

from sixfeetup.bowab.tests.mocks import MockSession


TOKEN_DURATION = 60
class Authentication(Schema):
    token_duration = SchemaNode(
        Integer(),
        default=TOKEN_DURATION,
        description=u'Duration (in minutes) password reset tokens are valid for.'
    )
authentication_schema = Authentication(
    path=u'.'.join((Authentication.__module__,
                   'authentication_schema')),
    name=u'authentication_schema',
    title=u'Authentication',
)

class ViewTests(TestCase):
    def setUp(self):
        super(ViewTests, self).setUp()
        self.config = testing.setUp()
        self.config.include('pyramid_controlpanel')
        self.config.add_controlpanel_section(authentication_schema)

    def test_get_value(self):
        # Make sure the default value bubbles up correctly
        request = testing.DummyRequest()
        request.user = None
        request.db_session = MockSession()
        cp = ControlPanel(request)
        authentication_schema
        token_duration = cp.get_value(authentication_schema.name,
                                      'token_duration')
        self.assertTrue(token_duration == TOKEN_DURATION)

