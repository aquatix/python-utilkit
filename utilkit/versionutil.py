"""
Version checking utilities
"""

## Check for an update of the notifier
def get_repo_version(url):
    """
    Get the current version on GitHub
    `url` looks like 'https://raw.githubusercontent.com/aquatix/ns-notifications/master/VERSION'
    """
    response = requests.get(url)
    if response.status_code == 404:
        return None
    else:
        return response.text.replace('\n', '')


def get_local_version():
    """
    Get the locally installed version
    """
    with open ("VERSION", "r") as versionfile:
        return versionfile.read().replace('\n', '')


def version_changed(url):
    """
    Compare the remote version against the locally installed version
    `url` looks like 'https://raw.githubusercontent.com/aquatix/ns-notifications/master/VERSION'
    """
    return get_repo_version(url) != get_local_version()
