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
from pydantic import BaseModel, Field, RootModel

from one_doc_python_sdk.pydantic.document_rendering_bucket_response_signed_urls_item import DocumentRenderingBucketResponseSignedUrlsItem

DocumentRenderingBucketResponseSignedUrls = typing.List[DocumentRenderingBucketResponseSignedUrlsItem]
