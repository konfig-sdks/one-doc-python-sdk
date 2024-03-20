import typing_extensions

from one_doc_python_sdk.apis.tags import TagValues
from one_doc_python_sdk.apis.tags.document_api import DocumentApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DOCUMENT: DocumentApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DOCUMENT: DocumentApi,
    }
)
