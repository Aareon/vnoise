from .vnoise import Noise


def _get_version() -> str:
    import pkg_resources

    try:
        return pkg_resources.get_distribution("vnoise").version
    except pkg_resources.DistributionNotFound:
        return None


__version__ = _get_version()
