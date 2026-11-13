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
# packages/server/src/server/modules/account/change_bio/schemas.py
# ==================================================================================================

from pydantic import BaseModel, ConfigDict
from ....shared.schemas import BioMixin

# ==================================================================================================

class ChangeBioRequest(BioMixin, BaseModel):
    """Request body for updating the authenticated user's biographical text."""

    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "examples": [
                {
                    "bio": "Software engineer passionate about open source.",
                }
            ]
        },
    )

# ==================================================================================================
