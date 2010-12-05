# Twilio Notifier
by [Jason Ardell](http://github.com/ardell)

A command to pull down notifications from your Twilio log and email them to you.

Command line usage:
-e, --email: The email address that you want notifications sent to.
-s, --account-sid: Your Account SID (from your Twilio account)
-t, --auth-token: Your Auth Token (from your Twilio account)

I recommend you add it as a command to your crontab...
twilio-notifier --account-sid AC1234567890FOOBAR1234567890 --auth-token 9876543210BAZ9876543210 2>&1 | mail -s 'Twilio Errors' my.email@example.com

## Installation
I highly recommend installing via pearfarm:
pear install channel://ardell.pearfarm.org/twilioNotifier

## Requirements:
PHP 5+
CLImax--installing via pearfarm will install this for you. (https://github.com/apinstein/climax)

## License
MIT.

## Todo
* Perhaps support a callback for what to do on each error? That way people could have SMSs sent to them, or do custom error handling.
