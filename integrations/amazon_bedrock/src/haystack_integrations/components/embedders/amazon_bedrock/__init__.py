# SPDX-FileCopyrightText: 2023-present khulnasoft GmbH <info@khulnasoft.com>
#
# SPDX-License-Identifier: Apache-2.0
from .document_embedder import AmazonBedrockDocumentEmbedder
from .text_embedder import AmazonBedrockTextEmbedder

__all__ = ["AmazonBedrockTextEmbedder", "AmazonBedrockDocumentEmbedder"]
