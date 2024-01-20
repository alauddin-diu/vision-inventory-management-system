"""Version information for Vision_IMS.

Provides information on the current Vision_IMS version
"""

import os
import pathlib
import platform
import re
from datetime import datetime as dt
from datetime import timedelta as td

import django
from django.conf import settings

from dulwich.repo import NotGitRepository, Repo

from .api_version import Vision_IMS_API_VERSION

# Vision_IMS software version
Vision_IMS_SW_VERSION = "0.13.0 dev"

# Discover git
try:
    main_repo = Repo(pathlib.Path(__file__).parent.parent.parent)
    main_commit = main_repo[main_repo.head()]
except (NotGitRepository, FileNotFoundError):
    main_commit = None


def Vision_IMSInstanceName():
    """Returns the InstanceName settings for the current database."""
    import common.models

    return common.models.Vision_IMSSetting.get_setting("Vision_IMS_INSTANCE", "")


def Vision_IMSInstanceTitle():
    """Returns the InstanceTitle for the current database."""
    import common.models

    if common.models.Vision_IMSSetting.get_setting("Vision_IMS_INSTANCE_TITLE", False):
        return common.models.Vision_IMSSetting.get_setting("Vision_IMS_INSTANCE", "")
    else:
        return 'Vision_IMS'


def Vision_IMSVersion():
    """Returns the Vision_IMS version string."""
    return Vision_IMS_SW_VERSION.lower().strip()


def Vision_IMSVersionTuple(version=None):
    """Return the Vision_IMS version string as (maj, min, sub) tuple."""
    if version is None:
        version = Vision_IMS_SW_VERSION

    match = re.match(r"^.*(\d+)\.(\d+)\.(\d+).*$", str(version))

    return [int(g) for g in match.groups()]


def isVision_IMSDevelopmentVersion():
    """Return True if current Vision_IMS version is a "development" version."""
    return Vision_IMSVersion().endswith('dev')


def Vision_IMSDocsVersion():
    """Return the version string matching the latest documentation.

    Development -> "latest"
    Release -> "major.minor.sub" e.g. "0.5.2"
    """
    if isVision_IMSDevelopmentVersion():
        return "latest"
    else:
        return Vision_IMS_SW_VERSION  # pragma: no cover


def isVision_IMSUpToDate():
    """Test if the Vision_IMS instance is "up to date" with the latest version.

    A background task periodically queries GitHub for latest version, and stores it to the database as "_Vision_IMS_LATEST_VERSION"
    """
    import common.models
    latest = common.models.Vision_IMSSetting.get_setting('_Vision_IMS_LATEST_VERSION', backup_value=None, create=False)

    # No record for "latest" version - we must assume we are up to date!
    if not latest:
        return True

    # Extract "tuple" version (Python can directly compare version tuples)
    latest_version = Vision_IMSVersionTuple(latest)  # pragma: no cover
    Vision_IMS_version = Vision_IMSVersionTuple()  # pragma: no cover

    return Vision_IMS_version >= latest_version  # pragma: no cover


def Vision_IMSApiVersion():
    """Returns current API version of Vision_IMS."""
    return Vision_IMS_API_VERSION


def Vision_IMSDjangoVersion():
    """Returns the version of Django library."""
    return django.get_version()


def Vision_IMSCommitHash():
    """Returns the git commit hash for the running codebase."""
    # First look in the environment variables, i.e. if running in docker
    commit_hash = os.environ.get('Vision_IMS_COMMIT_HASH', '')

    if commit_hash:
        return commit_hash

    if main_commit is None:
        return None
    return main_commit.sha().hexdigest()[0:7]


def Vision_IMSCommitDate():
    """Returns the git commit date for the running codebase."""
    # First look in the environment variables, e.g. if running in docker
    commit_date = os.environ.get('Vision_IMS_COMMIT_DATE', '')

    if commit_date:
        return commit_date.split(' ')[0]

    if main_commit is None:
        return None

    commit_dt = dt.fromtimestamp(main_commit.commit_time) + td(seconds=main_commit.commit_timezone)
    return str(commit_dt.date())


def Vision_IMSInstaller():
    """Returns the installer for the running codebase - if set."""
    # First look in the environment variables, e.g. if running in docker

    installer = os.environ.get('Vision_IMS_PKG_INSTALLER', '')

    if installer:
        return installer
    elif settings.DOCKER:
        return 'DOC'
    elif main_commit is not None:
        return 'GIT'

    return None


def Vision_IMSBranch():
    """Returns the branch for the running codebase - if set."""
    # First look in the environment variables, e.g. if running in docker

    branch = os.environ.get('Vision_IMS_PKG_BRANCH', '')

    if branch:
        return branch

    if main_commit is None:
        return None

    try:
        branch = main_repo.refs.follow(b'HEAD')[0][1].decode()
        return branch.removeprefix('refs/heads/')
    except IndexError:
        return None  # pragma: no cover


def Vision_IMSTarget():
    """Returns the target platform for the running codebase - if set."""
    # First look in the environment variables, e.g. if running in docker

    return os.environ.get('Vision_IMS_PKG_TARGET', None)


def Vision_IMSPlatform():
    """Returns the platform for the instance."""

    return platform.platform(aliased=True)
