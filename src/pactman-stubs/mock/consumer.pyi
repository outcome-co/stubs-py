"""
This type stub file was generated by pyright.
"""

import os
from typing import Generic, Optional, TypeVar

from pactman.mock.pact import Pact
from pactman.mock.provider import Provider

P = TypeVar('P', bound=Pact)

"""Classes and methods to describe contract Consumers."""
USE_MOCKING_SERVER = os.environ.get("PACT_USE_MOCKING_SERVER", "no") == "yes"

class Consumer(Generic[P], object):
    """
    A Pact consumer.

    Use this class to describe the service making requests to the provider and
    then use `has_pact_with` to create a contract with a specific service:

    >>> from pactman import Consumer, Provider
    >>> consumer = Consumer('my-web-front-end')
    >>> consumer.has_pact_with(Provider('my-backend-serivce'))
    """

    def __init__(self, name: str, service_cls: P = ...) -> None:
        """
        Constructor for the Consumer class.

        :param name: The name of this Consumer. This will be shown in the Pact
            when it is published.
        :type name: str
        :param service_cls: Pact, or a sub-class of it, to use when creating
            the contracts. This is useful when you have a custom URL or port
            for your mock service and want to use the same value on all of
            your contracts.
        :type service_cls: pact.Pact
        """
        ...
    def has_pact_with(
        self,
        provider: Provider,
        host_name: str = ...,
        port: int = ...,
        log_dir: str = ...,
        ssl: bool = ...,
        sslcert: Optional[str] = ...,
        sslkey: Optional[str] = ...,
        pact_dir: str = ...,
        version: str = ...,
        file_write_mode: str = ...,
        use_mocking_server: bool = ...,
    ) -> P:
        """
        Create a contract between the `provider` and this consumer.

        If you are running the Pact mock service in a non-default location,
        you can provide the host name and port here:

        >>> from pactman import Consumer, Provider
        >>> consumer = Consumer('my-web-front-end')
        >>> consumer.has_pact_with(
        ...   Provider('my-backend-serivce'),
        ...   host_name='192.168.1.1',
        ...   port=8000)

        :param provider: The provider service for this contract.
        :type provider: pact.Provider
        :param host_name: An optional host name to use when contacting the
            Pact mock service. This will need to be the same host name used by
            your code under test to contact the mock service. It defaults to:
            `localhost`.
        :type host_name: str
        :param port: The TCP port to use when contacting the Pact mock service.
            This will need to tbe the same port used by your code under test
            to contact the mock service. It defaults to a port >= 8050.
        :type port: int
        :param log_dir: The directory where logs should be written. Defaults to
            the current directory.
        :type log_dir: str
        :param ssl: Flag to control the use of a self-signed SSL cert to run
            the server over HTTPS , defaults to False.
        :type ssl: bool
        :param sslcert: Path to a custom self-signed SSL cert file, 'ssl'
            option must be set to True to use this option. Defaults to None.
        :type sslcert: str
        :param sslkey: Path to a custom key and self-signed SSL cert key file,
            'ssl' option must be set to True to use this option.
            Defaults to None.
        :type sslkey: str
        :param pact_dir: Directory where the resulting pact files will be
            written. Defaults to the current directory.
        :type pact_dir: str
        :param version: The Pact Specification version to use, defaults to
            '2.0.0'.
        :type version: str
        :param file_write_mode: `overwrite` or `merge`. Use `merge` when
            running multiple mock service instances in parallel for the same
            consumer/provider pair. Ensure the pact file is deleted before
            running tests when using this option so that interactions deleted
            from the code are not maintained in the file. Defaults to
            `overwrite`.
        :type file_write_mode: str
        :param use_mocking_server: If True the mocking will be done using a
            HTTP server rather than patching urllib3 connections. Can be set
            by the environment variable PACT_USE_MOCKING_SERVER which has
            values "no" (default) or "yes".
        :type use_mocking_server: bool
        :return: A Pact object which you can use to define the specific
            interactions your code will have with the provider.
        :rtype: pact.Pact
        """
        ...
