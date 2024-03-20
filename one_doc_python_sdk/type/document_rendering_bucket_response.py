# coding: utf-8

"""
    API Doc

    Onedoc is an innovative API solution for developers, offering a simple and secure way to create and manage PDF documents using familiar technologies like React.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from one_doc_python_sdk.type.document_rendering_bucket_response_signed_urls import DocumentRenderingBucketResponseSignedUrls

class RequiredDocumentRenderingBucketResponse(TypedDict):
    pass

class OptionalDocumentRenderingBucketResponse(TypedDict, total=False):
    # URL for the upload.
    uploadURL: str

    # Generated username.
    username: str

    # Generated password.
    password: str

    # Identifier of the bucket.
    bucket: str

    signedUrls: DocumentRenderingBucketResponseSignedUrls

class DocumentRenderingBucketResponse(RequiredDocumentRenderingBucketResponse, OptionalDocumentRenderingBucketResponse):
    pass
