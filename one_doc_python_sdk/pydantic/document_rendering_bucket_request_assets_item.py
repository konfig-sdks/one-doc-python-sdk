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


class DocumentRenderingBucketRequestAssetsItem(BaseModel):
    # Relative path where the asset will be stored in the bucket.
    path: typing.Optional[str] = Field(None, alias='path')

    content: typing.Optional[typing.Union[str, str]] = Field(None, alias='content')
    class Config:
        arbitrary_types_allowed = True
