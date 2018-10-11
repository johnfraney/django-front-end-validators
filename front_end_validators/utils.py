import pkg_resources


def get_transcrypt_version():
    """Returns installed Transcrypt version as a string"""
    transcrypt_version = pkg_resources.get_distribution('transcrypt').version
    return transcrypt_version
