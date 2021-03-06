"""
This type stub file was generated by pyright.
"""
from typing import Dict

from pactman.mock.pact import Interaction, Pact
from urllib3.response import HTTPResponse

from ..verifier.result import Result

class Request:
    def __init__(self, method: str, path: str, query: str, headers: Dict[str, str], body: Dict[str, object]) -> None: ...

class RecordResult(Result):
    reason: str
    def start(self, interaction: Interaction) -> None: ...
    def fail(self, message: str, path: str = ...) -> bool: ...

class PactRequestHandler:
    def __init__(self, pact: Pact) -> None: ...
    def validate_request(self, method: str) -> HTTPResponse: ...
    def get_body(self) -> Dict[str, object]: ...
    def respond_for_interaction(self, reason: str) -> HTTPResponse: ...
    def handle_response_encoding(self, response: Dict[str, object], headers: Dict[str, str]) -> bytes: ...
    def write_pact(self, interaction: Interaction) -> None: ...
