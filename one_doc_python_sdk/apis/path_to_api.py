import typing_extensions

from one_doc_python_sdk.paths import PathValues
from one_doc_python_sdk.apis.paths.api_docs_generate import ApiDocsGenerate
from one_doc_python_sdk.apis.paths.api_docs_initiate import ApiDocsInitiate

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_DOCS_GENERATE: ApiDocsGenerate,
        PathValues.API_DOCS_INITIATE: ApiDocsInitiate,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_DOCS_GENERATE: ApiDocsGenerate,
        PathValues.API_DOCS_INITIATE: ApiDocsInitiate,
    }
)
