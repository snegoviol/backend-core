# ==================================================================================================
#
# Copyright (c) 2026 Ilya Snegov
#
# Dedicated to the public domain under the Creative Commons
# CC0 1.0 Universal Public Domain Dedication (the "Dedication").
# You may obtain a copy of the Dedication at
#
# https://creativecommons.org/publicdomain/zero/1.0/legalcode.en
#
# ==================================================================================================
# justfile
# ==================================================================================================

# --------------------------------------------------------------------------------------------------
# Justfile Settings
# --------------------------------------------------------------------------------------------------
set dotenv-load := true
set export := true

# --------------------------------------------------------------------------------------------------
# Environment Mappings: justfile variable -> pixi environment
# --------------------------------------------------------------------------------------------------`

ENV_DEFAULT := "pixi run"

# --------------------------------------------------------------------------------------------------
# Scripts
# --------------------------------------------------------------------------------------------------

# Generate .env from template with secure random passwords
gen-env:
    {{ENV_DEFAULT}} python -m scripts.utils.init_env

# Generate Redis ACL rules for Docker init
gen-acl:
    {{ENV_DEFAULT}} python -m scripts.utils.generate_redis_acl

# Generate PostgreSQL user creation script for Docker init
gen-sql:
    {{ENV_DEFAULT}} python -m scripts.utils.generate_postgres_sql

# Export OpenAPI/Swagger specification for the API
export-swagger:
	{{ENV_DEFAULT}} python -m scripts.utils.export_swagger

# --------------------------------------------------------------------------------------------------
# Infrastructure
# --------------------------------------------------------------------------------------------------

# Generate new revision
db-revision message='New migration':
    {{ENV_DEFAULT}} alembic -c ./migrations/alembic.ini revision -m "{{message}}"

# Generate new revision with auto-detected changes
db-revision-auto message='Auto migration':
    {{ENV_DEFAULT}} alembic -c ./migrations/alembic.ini revision --autogenerate -m "{{message}}"

# Apply pending migrations to sync database schema
db-migrate:
    {{ENV_DEFAULT}} alembic -c ./migrations/alembic.ini upgrade head

# Revert the latest migration step
db-rollback:
    {{ENV_DEFAULT}} alembic -c ./migrations/alembic.ini downgrade -1

# --------------------------------------------------------------------------------------------------
# Runtime
# --------------------------------------------------------------------------------------------------

# Launch FastAPI server
server:
    {{ENV_DEFAULT}} python -m server.main

# --------------------------------------------------------------------------------------------------
# Docker Local
# --------------------------------------------------------------------------------------------------

# Start infrastructure stack to be consumed by locally running services
docker-up:
    {{ENV_DEFAULT}} docker compose -f docker-compose.yml up -d

# Stop local containers and remove anonymous volumes
docker-down:
    {{ENV_DEFAULT}} docker compose -f docker-compose.yml down --remove-orphans --volumes

# Stream combined logs from all local services
docker-logs:
    {{ENV_DEFAULT}} docker compose -f docker-compose.yml logs -f

# --------------------------------------------------------------------------------------------------
# Quick Start
# --------------------------------------------------------------------------------------------------

# Start full local development environment and open Swagger in browser
quick-start:
    {{ENV_DEFAULT}} python -m scripts.quick_start

# ==================================================================================================`
