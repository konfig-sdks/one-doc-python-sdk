<div align="left">

[![Visit Onedoc](./header.png)](https://onedoc.com)

# Onedoc<a id="onedoc"></a>

Onedoc is an innovative API solution for developers, offering a simple and secure way to create and manage PDF documents using familiar technologies like React.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`onedoc.document.generate_pdf_from_bucket`](#onedocdocumentgenerate_pdf_from_bucket)
  * [`onedoc.document.rendering_bucket`](#onedocdocumentrendering_bucket)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=OneDoc&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from one_doc_python_sdk import OneDoc, ApiException

onedoc = OneDoc(
    api_key_auth="YOUR_API_KEY",
)

try:
    # Generates a PDF from a specified bucket.
    generate_pdf_from_bucket_response = onedoc.document.generate_pdf_from_bucket(
        title="document",
        bucket="string_example",
        password="string_example",
        username="string_example",
        test=True,
        save=False,
        expires_in=1,
    )
except ApiException as e:
    print("Exception when calling DocumentApi.generate_pdf_from_bucket: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from one_doc_python_sdk import OneDoc, ApiException

onedoc = OneDoc(
    api_key_auth="YOUR_API_KEY",
)


async def main():
    try:
        # Generates a PDF from a specified bucket.
        generate_pdf_from_bucket_response = (
            await onedoc.document.agenerate_pdf_from_bucket(
                title="document",
                bucket="string_example",
                password="string_example",
                username="string_example",
                test=True,
                save=False,
                expires_in=1,
            )
        )
    except ApiException as e:
        print("Exception when calling DocumentApi.generate_pdf_from_bucket: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from one_doc_python_sdk import OneDoc, ApiException

onedoc = OneDoc(
    api_key_auth="YOUR_API_KEY",
)

try:
    # Generates a PDF from a specified bucket.
    generate_pdf_from_bucket_response = onedoc.document.raw.generate_pdf_from_bucket(
        title="document",
        bucket="string_example",
        password="string_example",
        username="string_example",
        test=True,
        save=False,
        expires_in=1,
    )
    pprint(generate_pdf_from_bucket_response.headers)
    pprint(generate_pdf_from_bucket_response.status)
    pprint(generate_pdf_from_bucket_response.round_trip_time)
except ApiException as e:
    print("Exception when calling DocumentApi.generate_pdf_from_bucket: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `onedoc.document.generate_pdf_from_bucket`<a id="onedocdocumentgenerate_pdf_from_bucket"></a>

This route is responsible for generating a PDF from a bucket.  It expects a JSON body with details of the bucket, user credentials, and PDF generation options.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_pdf_from_bucket_response = onedoc.document.generate_pdf_from_bucket(
    title="document",
    bucket="string_example",
    password="string_example",
    username="string_example",
    test=True,
    save=False,
    expires_in=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

The title of the PDF, defaults to \\\"document\\\".

##### bucket: `str`<a id="bucket-str"></a>

The identifier of the bucket.

##### password: `str`<a id="password-str"></a>

The password of the bucket.

##### username: `str`<a id="username-str"></a>

The username of the bucket.

##### test: `bool`<a id="test-bool"></a>

Whether or not to generate a test PDF, defaults to true.

##### save: `bool`<a id="save-bool"></a>

Whether or not to save the PDF to the bucket, defaults to false.

##### expires_in: `int`<a id="expires_in-int"></a>

The expiration time of the PDF in days, default is 1 day.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DocumentGeneratePdfFromBucketRequest`](./one_doc_python_sdk/type/document_generate_pdf_from_bucket_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/docs/generate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `onedoc.document.rendering_bucket`<a id="onedocdocumentrendering_bucket"></a>

This endpoint creates a bucket for the html and all specified assets. It returns signed urls to the buckets.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rendering_bucket_response = onedoc.document.rendering_bucket(
    assets=[{}],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### assets: [`DocumentRenderingBucketRequestAssets`](./one_doc_python_sdk/type/document_rendering_bucket_request_assets.py)<a id="assets-documentrenderingbucketrequestassetsone_doc_python_sdktypedocument_rendering_bucket_request_assetspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DocumentRenderingBucketRequest`](./one_doc_python_sdk/type/document_rendering_bucket_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DocumentRenderingBucketResponse`](./one_doc_python_sdk/pydantic/document_rendering_bucket_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/docs/initiate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
