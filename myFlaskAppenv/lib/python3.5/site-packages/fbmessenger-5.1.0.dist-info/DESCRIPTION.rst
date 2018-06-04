Facebook Messenger
==================

|PyPI| |Build Status| |Coverage Status| |PyPI|

A python library to communicate with the Facebook Messenger API’s

Table of Contents
-----------------

.. raw:: html

   <!-- MarkdownTOC depth="2" autolink="true" autoanchor="true" bracket="round" -->

-  `Installation <#installation>`__
-  `Example usage with Flask <#example-usage-with-flask>`__
-  `Elements <#elements>`__
-  `Attachments <#attachments>`__
-  `Templates <#templates>`__
-  `Sender Actions <#sender-actions>`__
-  `Quick Replies <#quick-replies>`__
-  `Thread settings <#thread-settings>`__

.. raw:: html

   <!-- /MarkdownTOC -->

 ## Installation

Install from pip

.. code:: bash

    pip install fbmessenger

 ### Facebook app setup

-  `Create a page <https://www.facebook.com/pages/create/>`__ for your
   app, if you don’t already have one
-  `Create an
   app <https://developers.facebook.com/quickstarts/?platform=web>`__
-  Add the Messenger product
-  Select the Page to generate a page token

 ## Example usage with Flask

First you need to create a verify token, this can be any string e.g.

::

    'my_verify_token'

Messenger class
~~~~~~~~~~~~~~~

We need to extend the ``BaseMessenger`` abstract class and implement
methods for each of the following subscription fields.

-  ``message``
-  ``delivery``
-  ``read``
-  ``optin``
-  ``postback``
-  ``account_linking``

.. code:: python

    from fbmessenger import BaseMessenger


    class Messenger(BaseMessenger):
        def __init__(self, page_access_token):
            self.page_access_token = page_access_token
            super(Messenger, self).__init__(self.page_access_token)

        def message(self, message):
            self.send({'text': 'Received: {0}'.format(message['message']['text'])}, 'RESPONSE')

        def delivery(self, message):
            pass

        def read(self, message):
            pass

        def account_linking(self, message):
            pass

        def postback(self, message):
            pass

        def optin(self, message):
            pass

Create a route for the callback url
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This can be used to process any messages received and also to verify
your app

.. code:: python

    import os
    from flask import Flask, request

    app = Flask(__name__)
    app.debug = True

    messenger = Messenger(os.environ.get('FB_VERIFY_TOKEN'), os.environ.get('FB_PAGE_TOKEN'))

    @app.route('/webhook', methods=['GET', 'POST'])
    def webhook():
        if request.method == 'GET':
            if (request.args.get('hub.verify_token') == os.environ.get('FB_VERIFY_TOKEN')):
                return request.args.get('hub.challenge')
            raise ValueError('FB_VERIFY_TOKEN does not match.')
        elif request.method == 'POST':
            messenger.handle(request.get_json(force=True))
        return ''


    if __name__ == "__main__":
        app.run(host='0.0.0.0')

 ## Elements

Import the elements (or just the ones you need)

::

    from fbmessenger import elements

Messaging type
~~~~~~~~~~~~~~

Starting from 7th May 2018, Facebook requires that all message sends
must include the ``messaging_type`` property:

https://developers.facebook.com/docs/messenger-platform/reference/send-api

This is passed in the ``send()`` calls below - in each case, we’ll just
use ``RESPONSE``. You should use whatever value is appropriate for your
application. Supported values are:

-  ``RESPONSE``
-  ``UPDATE``
-  ``MESSAGE_TAG``
-  ``NON_PROMOTIONAL_SUBSCRIPTION``

See `Messaging
Types <https://developers.facebook.com/docs/messenger-platform/send-messages/#messaging_types>`__
for more information.

Notification Type
~~~~~~~~~~~~~~~~~

Any of the elements below may be sent in conjunction with a notification
type (see the `Send API
documentation <https://developers.facebook.com/docs/messenger-platform/reference/send-api/>`__
for more details). ``notification_type`` is an optional parameter to the
``.send()`` call. For example:

.. code:: python

    messenger.send({'text': msg}, 'RESPONSE', notification_type='SILENT_PUSH')

Supported values are are: - ``REGULAR`` - ``SILENT_PUSH`` - ``NO_PUSH``

If a value is not provided, then the notification preference will not be
set and Facebook Messenger’s default will apply (which is ``REGULAR`` at
the time of writing).

Text
~~~~

You can pass a simple dict or use the Class

.. code:: python

    messenger.send({'text': msg}, 'RESPONSE')

    elem = elements.Text('Your Message')
    messenger.send(elem.to_dict(), 'RESPONSE')

Web button
~~~~~~~~~~

.. code:: python

    btn = elements.Button(title='Web button', url='http://example.com')
    messenger.send(btn.to_dict(), 'RESPONSE')

Payload button
~~~~~~~~~~~~~~

To use these buttons you must have the ``message_deliveries``
subscription enabled

.. code:: python

    btn = elements.Button(title='Postback button', payload='payload')
    messenger.send(btn.to_dict(), 'RESPONSE')

 ## Attachments

You can upload attachments to Facebook for use in their other APIs:

.. code:: python

    attachment = attachments.Image(url='https://example.com/image.jpg')
    client = MessengerClient(page_access_token=12345678)
    res = client.upload_attachment(attachment)
    print(res)
    {"attachment_id": "12345"}

Images
~~~~~~

.. code:: python

    image = attachments.Image(url='http://example.com/image.jpg')
    messenger.send(image.to_dict(), 'RESPONSE')

Audio
~~~~~

.. code:: python

    audio = attachments.Image(url='http://example.com/audio.mp3')
    messenger.send(audio.to_dict(), 'RESPONSE')

Video
~~~~~

.. code:: python

    video = attachments.Video(url='http://example.com/video.mp4')
    messenger.send(video.to_dict(), 'RESPONSE')

Files
~~~~~

.. code:: python

    file = attachments.File(url='http://example.com/file.txt')
    messenger.send(file.to_dict(), 'RESPONSE')

 ## Templates

Import the templates (or just the ones you need)

::

    from fbmessenger import templates

Generic template
~~~~~~~~~~~~~~~~

.. code:: python

    btn = elements.Button(title='Web button', url='http://facebook.com')
    elems = elements.Element(
        title='Element',
        item_url='http://facebook.com',
        image_url='http://facebook.com/image.jpg',
        subtitle='Subtitle',
        buttons=[
            btn
        ]
    )
    res = templates.GenericTemplate(elements=[elems])
    messenger.send(res.to_dict(), 'RESPONSE')

Button template
~~~~~~~~~~~~~~~

.. code:: python

    btn = elements.Button(title='Web button', url='http://facebook.com')
    btn2 = elements.Button(title='Postback button', payload='payload')
    res = templates.ButtonTemplate(
        text='Button template',
        buttons=[btn, btn2]
    )
    messenger.send(res.to_dict(), 'RESPONSE')

Receipt template
~~~~~~~~~~~~~~~~

.. code:: python

    element = elements.Element(
        title='Classic White T-Shirt',
        subtitle='100% Soft and Luxurious Cotton',
        quantity=2,
        price=50,
        currency='USD',
        image_url='http://petersapparel.parseapp.com/img/whiteshirt.png',
    )
    adjustment1 = elements.Adjustment(name='New Customer Discount', amount=20)
    adjustment2 = elements.Adjustment(name='$10 Off Coupon', amount=10)
    address = elements.Address(
        street_1='1 Hacker Way',
        city='Menlo Park',
        postal_code='94025',
        state='CA',
        country='US'
    )
    summary = elements.Summary(
        subtotal=75.00,
        shipping_cost=4.95,
        total_tax=6.19,
        total_cost=56.14
    )
    res = templates.ReceiptTemplate(
        recipient_name='Stephane Crozatier',
        order_number='12345678902',
        currency='USD',
        payment_method='Visa 2345',
        order_url='http://petersapparel.parseapp.com/order?order_id=123456',
        timestamp='1428444852',
        address=address,
        summary=summary,
        adjustments=[adjustment1, adjustment2],
        elements=[element]
    )
    messenger.send(res.to_dict(), 'RESPONSE')

Media template
~~~~~~~~~~~~~~

::

    btn = elements.Button(
        button_type='web_url',
        title='Web button',
        url='http://facebook.com'
    )
    attachment = attachments.Image(attachment_id='12345')
    res = templates.MediaTemplate(attachment, buttons=[btn])
    messenger.send(res.to_dict())

 ## Sender Actions

Typing on
~~~~~~~~~

.. code:: python

    typing_on = SenderAction(sender_action='typing_on')
    messenger.send_action(typing_on.to_dict())

Typing off
~~~~~~~~~~

.. code:: python

    typing_ffn = SenderAction(sender_action='typing_off')
    messenger.send_action(typing_off.to_dict())

Mark seen
~~~~~~~~~

.. code:: python

    mark_seen = SenderAction(sender_action='mark_seen')
    messenger.send_action(mark_seen.to_dict())

 ## Quick Replies

.. code:: python

    quick_reply_1 = QuickReply(title='Do something', payload='Send me this payload')
    quick_reply_2 = QuickReply(title='Do something else', payload='Send me this other payload')
    quick_replies = QuickReplies(quick_replies=[
        quick_reply_1,
        quick_reply_2
    ])
    text = { text: 'A message' }
    text['quick_replies'] = quick_replies.to_dict()
    messenger.send(text, 'RESPONSE')

 ## Messenger Profile

Greeting Text
~~~~~~~~~~~~~

.. code:: python


    from fbmessenger.thread_settings import GreetingText, MessengerProfile

    greeting_text = GreetingText('Welcome to my bot')
    messenger_profile = MessengerProfile(greetings=[greeting_text])
    messenger.set_messenger_profile(messenger_profile.to_dict())

Get Started Button
~~~~~~~~~~~~~~~~~~

.. code:: python

    from fbmessenger.thread_settings import GetStartedButton, MessengerProfile

    get_started = GetStartedButton(payload='GET_STARTED')
    messenger_profile = MessengerProfile(get_started=get_started)
    messenger.set_messenger_profile(messenger_profile.to_dict())

You can then check for this payload in the ``postback`` method

Persistent Menu
~~~~~~~~~~~~~~~

.. code:: python

    from fbmessenger.thread_settings import PersistentMenu, PersistentMenuItem, MessengerProfile

    menu_item_1 = PersistentMenuItem(item_type='web_url', title='Menu Item 1', url='https://facebook.com')
    menu_item_2 = PersistentMenuItem(item_type='postback', title='Menu Item 2', payload='PAYLOAD')

    menu = PersistentMenu(menu_items=[menu_item_1, menu_item_2])

    messenger_profile = MessengerProfile(persistent_menus=[menu])
    messenger.set_messenger_profile(messenger_profile.to_dict())

.. |PyPI| image:: https://img.shields.io/pypi/v/fbmessenger.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/fbmessenger
.. |Build Status| image:: https://travis-ci.org/rehabstudio/fbmessenger.svg?branch=master
   :target: https://travis-ci.org/rehabstudio/fbmessenger
.. |Coverage Status| image:: https://coveralls.io/repos/github/rehabstudio/fbmessenger/badge.svg?branch=master
   :target: https://coveralls.io/github/rehabstudio/fbmessenger?branch=master
.. |PyPI| image:: https://img.shields.io/pypi/l/fbmessenger.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/fbmessenger


