# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .search_action_py3 import SearchAction
    from .suggestions_suggestion_group_py3 import SuggestionsSuggestionGroup
    from .suggestions_py3 import Suggestions
    from .query_context_py3 import QueryContext
    from .search_results_answer_py3 import SearchResultsAnswer
    from .answer_py3 import Answer
    from .thing_py3 import Thing
    from .action_py3 import Action
    from .response_py3 import Response
    from .identifiable_py3 import Identifiable
    from .error_py3 import Error
    from .error_response_py3 import ErrorResponse, ErrorResponseException
    from .response_base_py3 import ResponseBase
    from .creative_work_py3 import CreativeWork
except (SyntaxError, ImportError):
    from .search_action import SearchAction
    from .suggestions_suggestion_group import SuggestionsSuggestionGroup
    from .suggestions import Suggestions
    from .query_context import QueryContext
    from .search_results_answer import SearchResultsAnswer
    from .answer import Answer
    from .thing import Thing
    from .action import Action
    from .response import Response
    from .identifiable import Identifiable
    from .error import Error
    from .error_response import ErrorResponse, ErrorResponseException
    from .response_base import ResponseBase
    from .creative_work import CreativeWork
from .auto_suggest_search_api_enums import (
    ScenarioType,
    SearchKind,
    ErrorCode,
    SafeSearch,
    ResponseFormat,
)

__all__ = [
    'SearchAction',
    'SuggestionsSuggestionGroup',
    'Suggestions',
    'QueryContext',
    'SearchResultsAnswer',
    'Answer',
    'Thing',
    'Action',
    'Response',
    'Identifiable',
    'Error',
    'ErrorResponse', 'ErrorResponseException',
    'ResponseBase',
    'CreativeWork',
    'ScenarioType',
    'SearchKind',
    'ErrorCode',
    'SafeSearch',
    'ResponseFormat',
]
