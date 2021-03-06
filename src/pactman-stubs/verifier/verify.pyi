"""
This type stub file was generated by pyright.
"""

from pactman.mock.pact import Pact, Request
from pactman.mock.pact_request_handler import RecordResult, Request

class RequestVerifier:
    interaction_name: str = ...
    def __init__(self, pact: Pact, interaction: Request, result: RecordResult) -> None: ...
    def log_context(self) -> None: ...
    def verify(self, request: Request) -> bool: ...
    def verify_query(self, spec_query: str, request: Request) -> bool: ...
    def compare_dict(self, data: object, spec: object, path: str) -> bool: ...
