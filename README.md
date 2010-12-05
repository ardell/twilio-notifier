# Twilio Notifier
by [Jason Ardell](http://github.com/ardell)

A command to pull down notifications from your Twilio log and email them to you.

Command line usage:
-e, --email: The email address that you want notifications sent to.
-s, --account-sid: Your Account SID (from your Twilio account)
-t, --auth-token: Your Auth Token (from your Twilio account)

## Requirements:
PHP 5+

## License
MIT.

## Todo
* Perhaps support a callback for what to do on each error? That way people could have SMSs sent to them, or do custom error handling.
