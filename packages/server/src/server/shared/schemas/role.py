# ==================================================================================================
# 
# Copyright (c) 2026 Ilya Snegov
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# ==================================================================================================
# packages/server/src/server/shared/schemas/role.py
# ==================================================================================================

from pydantic import Field

# ==================================================================================================

class NameMixin:
    """
    Shared name field for response schemas that expose a human-readable identifier.
    """

    name: str = Field(
        description="Unique human-readable identifier for the role.",
    )

# ==================================================================================================
