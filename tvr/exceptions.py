# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class EscapeInterrupt(Exception):
    "Signal that the ESC key has been pressed"


class ConfigError(Exception):
    "There was a problem with the configuration"


class TVRError(Exception):
    "Base TVR error class"


class AccountError(TVRError):
    "Could not access user account"


class SubmissionError(TVRError):
    "Submission could not be loaded"


class SubredditError(TVRError):
    "Subreddit could not be loaded"


class NoSubmissionsError(TVRError):
    "No submissions for the given page"

    def __init__(self, name):
        self.name = name
        message = '`{0}` has no submissions'.format(name)
        super(NoSubmissionsError, self).__init__(message)


class SubscriptionError(TVRError):
    "Content could not be fetched"


class InboxError(TVRError):
    "Content could not be fetched"


class ProgramError(TVRError):
    "Problem executing an external program"


class BrowserError(TVRError):
    "Could not open a web browser tab"


class TemporaryFileError(TVRError):
    "Indicates that an error has occurred and the file should not be deleted"


class MailcapEntryNotFound(TVRError):
    "A valid mailcap entry could not be coerced from the given url"


class InvalidRefreshToken(TVRError):
    "The refresh token is corrupt and cannot be used to login"
