Application Settings
--------------------

This package includes a method of storing sections of config values that should be editable through the web.
To integrate with this system, you need to define the schema for the control panel section using colander:

.. code-block:: python
    from colander import Email, Schema, SchemaNode, SequenceSchema, String

    class EmailAddresses(SequenceSchema):
          email = SchemaNode(
              String(),
              title='Email Address',
              description='Add an email address to be notified of new user creation.',
              validator=Email(),
          )

    class EmailNotification(Schema):
        email_addresses = EmailAddresses()

    email_notification_schema = EmailNotification(
        path='.'.join((EmailNotification.__module__, 'email_notification_schema')),
        name='email_notification',
        title='New User Creation: Email Notification',
        description='List of email addresses to notify when a new user is created.'
    )

Then in your application's initialization, add it via `config.add_controlpanel_section(email_notification_schema)`.
The entire list of configured sections will be available at `/control_panel`. The `path` and `name` fields are necessary components of the schema.
