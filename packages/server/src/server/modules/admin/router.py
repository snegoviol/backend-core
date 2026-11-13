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
# packages/server/src/server/modules/admin/router.py
# ==================================================================================================

from fastapi import APIRouter
from .users import users_admin_router
from .roles import roles_admin_router

admin_router = APIRouter(prefix="/admin", tags=["admin"])

admin_router.include_router(users_admin_router)
admin_router.include_router(roles_admin_router)

# ==================================================================================================
