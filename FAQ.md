# FAQ

How many numbers for a Flow?
> * 1 Twilio number can route incoming calls/messages to 1 Studio Flow (one-to-one) 
> * 1 Flow can process multiple phone numbers (one-to-many)

Can you message across multiple channels (Whatsapp, Chat, SMS)?
> * Yes, using the Conversations Trigger and API
> * But media messages are not supported

How long is data stored?
> * 30 days after an Execution starts

Can I store Payment data?
> * Use the Capture Payments Widget to store payments.
> * It is PCI compliant.

Can you receive multiple incoming calls from the same number?
> * Yes, Studio handles concurrent calls from the same number by default.
> * You can turn this off in the widget settings

Can you connect to a database in Studio?
> * Yes, use the Run Function Widget then call a Function hosted on Twilio that you’ve created. Inside that Function, you’ll call the database server.

How do you know what data is available in Context?
> * Flow: data associated to the Flow, like a phone number
> * Trigger: data set when the Flow starts, like incoming message, call, or REST API
> * Widget: data that each widget has, like body of an incoming message
> * Contact: dat about the contact engaging in the Flow, like a phone number

How can you modify a variable?
> * Liquid Filters on the variable
> * Ex: To split a string:
> `{{ "a~b" | split:"~" }} #=> ['a','b']`
> * Ex: To convert Liquid object to JSON
> `{{ flow.data | to_json }} #=> {"foo":"bar","baz":"bat"}`

How can you add logic to a variable?
> * You can add if/else statements and for loops using Liquid Filters.
> * EX: If else statement
> ```{% if flow.data.first_name %}
> Hello {{flow.data.first_name}}
> {% else %}
> Hello friend
> {% endif %}
> ```


Can you add comments with Liquid Filters?
> * Yes
> * `We made 1 million dollars {% comment %} in cash {% endcomment %} this year`

When does a variable get assigned?
> *At the end of a Step (after the Widget is exiting)

Widget doesn’t work
> *Widget names must start with a letter.
> *Separate names with ( _ )
> *Some widgets have required configurations (denoted by *)

How many Widgets can you add to a Flow?
> *Max of 1,000

Can you access Studio via an API?
> *Yes, you would do this for outgoing messages/calls
> *There is a REST API V2 that you can use with Helper Libraries (SDK) of via the Twilio CLI

How does pricing work?
> *Pay-as-you go and enterprise plans.
> *That is on top of normal charges from other products.

How should numbers be formatted?
> *E.164 (e.g. +1XXXXXXXXXX)
