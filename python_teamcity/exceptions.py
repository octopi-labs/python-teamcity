

class TeamcityAPIException(Exception):
    """Base class for all errors
    """
    def __init__(self):
        super(TeamcityAPIException, self).__init__()


class NotFound(TeamcityAPIException):
    """Resource cannot be found
    """
    pass


class ArtifactsMissing(NotFound):
    """Cannot find a build with all of the required artifacts.
    """
    pass


class UnknownJob(KeyError, NotFound):
    """Jenkins does not recognize the job requested.
    """
    pass


class UnknownView(KeyError, NotFound):
    """Jenkins does not recognize the view requested.
    """
    pass


class UnknownNode(KeyError, NotFound):
    """Jenkins does not recognize the node requested.
    """
    pass


class UnknownQueueItem(KeyError, NotFound):
    """Jenkins does not recognize the requested queue item
    """
    pass


class UnknownPlugin(KeyError, NotFound):
    """Jenkins does not recognize the plugin requested.
    """
    pass


class NoBuildData(NotFound):
    """A job has no build data.
    """
    pass


class NotBuiltYet(NotFound):
    """A job has no build data.
    """
    pass


class ArtifactBroken(TeamcityAPIException):
    """An artifact is broken, wrong
    """
    pass


class TimeOut(TeamcityAPIException):
    """Some jobs have taken too long to complete.
    """
    pass


class NoResults(TeamcityAPIException):
    """A build did not publish any results.
    """
    pass


class FailedNoResults(NoResults):
    """A build did not publish any results because it failed
    """
    pass


class BadURL(ValueError, TeamcityAPIException):
    """A URL appears to be broken
    """
    pass


class NotAuthorized(TeamcityAPIException):
    """Not Authorized to access resource"""
    # Usually thrown when we get a 403 returned
    pass


class NotSupportSCM(TeamcityAPIException):
    """
    It's a SCM that does not supported by current version of jenkinsapi
    """
    pass


class NotConfiguredSCM(TeamcityAPIException):
    """It's a job that doesn't have configured SCM
    """
    pass


class NotInQueue(TeamcityAPIException):
    """It's a job that is not in the queue
    """
    pass


class PostRequired(TeamcityAPIException):
    """Method requires POST and not GET
    """
    pass


class BadParams(TeamcityAPIException):
    """Invocation was given bad or inappropriate params
    """
    pass


class AlreadyExists(TeamcityAPIException):
    """
    Method requires POST and not GET
    """
    pass
