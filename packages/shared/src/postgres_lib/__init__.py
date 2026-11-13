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
# packages/shared/src/postgres_lib/__init__.py
# ==================================================================================================

from .config import postgres_config
from .session import async_engine, async_session_factory
from .models import (
    Base, IdModel, CreatedAtMixin, 
    User, UserRole, Role, RolePermission, 
    PermissionEnum, RoleEnum, PermissionSQL
)
from .repositories import BaseRepository, UserRepository, RoleRepository

# ==================================================================================================
