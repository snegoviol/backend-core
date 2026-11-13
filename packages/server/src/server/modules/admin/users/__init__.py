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
# packages/server/src/server/modules/admin/users/__init__.py
# ==================================================================================================

from .router import users_admin_router
from .get import get_all_users_route, get_user_route
from .delete import delete_user_route
from .update import update_user_route
from .manage_roles import assign_role_route, revoke_role_route

# ==================================================================================================
