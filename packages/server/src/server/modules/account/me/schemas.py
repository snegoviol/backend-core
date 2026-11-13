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
# packages/server/src/server/modules/account/me/schemas.py
# ==================================================================================================

from pydantic import BaseModel, ConfigDict
from ....shared.schemas import IdMixin, EmailMixin, IsVerifiedMixin, BioMixin, CreatedAtMixin

# ==================================================================================================

class UserResponse(IdMixin, EmailMixin, IsVerifiedMixin, BioMixin, CreatedAtMixin, BaseModel):
    """
    Response body containing the full profile of a registered user.
    """

    model_config = ConfigDict(
        extra="forbid",
        from_attributes=True,
        json_schema_extra={
            "examples": [
                {
                    "id": 1,
                    "email": "user@example.com",
                    "is_verified": True,
                    "bio": "Software engineer passionate about open source.",
                    "created_at": "2024-05-20T14:30:00Z",
                }
            ]
        },
    )

# ==================================================================================================
