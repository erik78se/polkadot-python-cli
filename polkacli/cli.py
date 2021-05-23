from argparse import ArgumentParser
from polkacli import rpc

SERVER_ADDRESS = 'http://localhost:9933'
HEADERS = {'Content-Type': 'application/json'}

cli = ArgumentParser()
subparsers = cli.add_subparsers(dest="subcommand")


def argument(*name_or_flags, **kwargs):
    """Convenience function to properly format arguments to pass to the
    subcommand decorator.

    """
    return (list(name_or_flags), kwargs)


def subcommand(args=[], parent=subparsers):
    """Decorator to define a new subcommand in a sanity-preserving way.
    The function will be stored in the ``func`` variable when the parser
    parses arguments so that it can be called directly like so::

        args = cli.parse_args()
        args.func(args)

    Usage example::

        @subcommand([argument("-d", help="Enable debug mode", action="store_true")])
        def subcommand(args):
            print(args)

    Then on the command line::

        $ python cli.py subcommand -d

    """

    def decorator(func):
        parser = parent.add_parser(func.__name__, description=func.__doc__)
        for arg in args:
            parser.add_argument(*arg[0], **arg[1])
        parser.set_defaults(func=func)

    return decorator


# @subcommand()
# def nothing(args):
#     print("Nothing special!")
#
#
# @subcommand([argument("-d", help="Debug mode", action="store_true")])
# def test(args):
#     print(args)
#
#
# @subcommand([argument("-f", "--filename", help="A thing with a filename")])
# def filename(args):
#     print(args.filename)
#
#
# @subcommand([argument("name", help="Name")])
# def name(args):
#     print(args.name)

@subcommand()
def polkaversion(help="Get running version of polkadot via rpc."):
    """
    Get running version of polkadot via rpc.
    """
    try:
        print(rpc.get_version())
    except:
        print("Failed getting polkadot version. Is polkadot running on localhost?")


@subcommand()
def syncing(help="Get sync status for polkadot via rpc."):
    """
    Get sync status for polkadot via rpc.
    """
    try:
        print(rpc.is_syncing())
    except:
        print("Failed getting polkadot sync status. Is polkadot running on localhost?")


@subcommand()
def validating(help="Checks if system_nodeRoles is Authority via rpc (E.g. validating)."):
    """
    Checks if system_nodeRoles == Authority, via rpc (E.g. validating).
    """
    try:
        print(rpc.is_validating())
    except:
        print("Failed getting system_nodeRoles to check validator status. Is polkadot running on localhost?")


@subcommand()
def newkey(help="Get a new session key via rpc."):
    """
    Get a new session key via rpc.
    """
    try:
        print(rpc.get_session_key())
    except:
        print("Failed getting new session key. Is polkadot running on localhost?")


@subcommand([argument("sessionkey", help="A sessionkey on the format: 0xb75f94a5eec...")])
def haskey(args):
    """
    Checks if the supplied session key is hosted on this node.
    """
    print(args.sessionkey)
    try:
        print(rpc.has_sessionKey(args.sessionkey))
    except:
        print("Failed checking for session key. Is polkadot running on localhost?")


def main():
    """
    See __main__.py
    """
    args = cli.parse_args()
    if args.subcommand is None:
        cli.print_help()
    else:
        args.func(args)


if __name__ == "__main__":
    args = cli.parse_args()
    if args.subcommand is None:
        cli.print_help()
    else:
        args.func(args)
