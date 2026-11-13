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
# packages/server/src/server/modules/admin/roles/get/schemas.py
# ==================================================================================================

from pydantic import BaseModel, ConfigDict
from .....shared.schemas import IdMixin, CreatedAtMixin, NameMixin

# ==================================================================================================

class RoleResponse(IdMixin, NameMixin, CreatedAtMixin, BaseModel):
    """
    Response body containing the record of a defined role.
    """

    model_config = ConfigDict(
        extra="forbid",
        from_attributes=True,
        json_schema_extra={
            "examples": [
                {
                    "id": 1,
                    "name": "admin",
                    "created_at": "2024-05-20T14:30:00Z",
                }
            ]
        },
    )

# ==================================================================================================
