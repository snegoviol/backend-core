<!--    
    ================================================================================================
    
    Copyright (c) 2026 Ilya Snegov
    
    Dedicated to the public domain under the Creative Commons
    CC0 1.0 Universal Public Domain Dedication (the "Dedication").
    You may obtain a copy of the Dedication at
    
    https://creativecommons.org/publicdomain/zero/1.0/legalcode.en

    ================================================================================================
    README.md
    ================================================================================================
-->

# Backend Core

> *An educational project demonstrating how to build a backend web server with Python. While designed for learning, its architecture — authentication, authorization, rate limiting, and consistent error handling — provides a solid foundation for real-world projects.*

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](#license)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-blue.svg)](#license)

<!--    
    ================================================================================================
-->

## Project Structure at a Glance

```sh
backend-core/
├── packages/           # Monorepo root containing all independently deployable
│   │                   # Python modules and shared libraries. Each package
│   │                   # strictly follows the standard `src/` layout (e.g.
│   │                   # `packages/server/src/server/`) for clean imports and
│   │                   # packaging.
│   │
│   ├── server/         # FastAPI application handling HTTP routing, request
│   │                   # validation, authentication, authorization, rate
│   │                   # limiting, access logging, and global error handling.
│   │
│   ├── shared/         # Cross-process shared infrastructure. Contains base
│   │                   # configurations and unified client abstractions for
│   │                   # external services.
│   │
│   ├── services/       # Cross-process business logic built on top of shared
│   │                   # infrastructure. Contains self-contained service
│   │                   # modules that implement domain-specific behaviour.
│   │
│   └── scripts/        # Standalone automation scripts for environment
│                       # bootstrapping, infrastructure initialization, and
│                       # auxiliary utility tasks.
│
├── migrations/         # Alembic migration environment and database schema
│                       # change scripts.
│
├── docs/               # Technical documentation covering project dependencies,
│                       # codebase layout, and request flow diagrams for every
│                       # endpoint.
│
├── LICENSES/           # Full texts of all licenses used in the project.
│
├── LICENSE.txt         # Licensing overview: which license applies to which files.
│
├── docker-compose.yml  # Docker Compose stack for running infrastructure
│                       # services (PostgreSQL, Redis) locally.
│
├── .env.example        # Environment variable template. Copied to .env during
│                       # bootstrapping with auto-generated credentials for
│                       # credential fields.
│
├── pixi.toml           # Pixi configuration defining a single shared
│                       # development environment.
│
├── pixi.lock           # Fully resolved and reproducible dependency lockfile.
│
└── justfile            # Task runner: bootstrap commands, database migration
                        # targets, runtime process launchers, and Docker Compose
                        # shortcuts.
```

<!--    
    ================================================================================================
-->

## Quick Start

### I. Prerequisites

| **Component**               | **Requirement**                |
| :-------------------------- | :----------------------------- |
| **CPU**                     | Supports `x86_64` architecture |
| **Operating System**        | `GNU/Linux`-based              |
| **Package Management Tool** | [`Pixi`](https://pixi.prefix.dev/latest/#installation) |
| **Container Tool**          | [`Docker`](https://docs.docker.com/engine/install/) |

> **Note:**  
> These are not strict requirements, but rather the baseline environment where the code is 
guaranteed to run out of the box. Alternative setups are possible but may require manual 
configuration.

<!--    
    ================================================================================================
-->

### II. Setup

1. **Clone the repository**

    ```sh
    git clone https://github.com/snegoviol/backend-core.git
    cd backend-core
    ```

2. **Install dependencies**

    ```sh
    pixi install
    ```

3. **Activate environment**

    ```sh
    pixi shell
    ```

<!--    
    ================================================================================================
-->

### III. Launch

Once the environment is activated, the service can be launched with a single command:

```sh
just quick-start
```

The launch script will automatically execute all necessary setup steps, start the server, and open the Swagger UI in your default web browser once the API is ready.

> **Want to see what happens under the hood?**  
> The launch script is fully documented with step-by-step comments explaining each action. You can find it here:
> - [Quick start script](./packages/scripts/src/scripts/quick_start.py)

<!--    
    ================================================================================================
-->

### IV. Cleanup

When you are done, shut down the running services by terminating the server terminal process, then bring down the infrastructure containers:

```sh
just docker-down
```

<!--    
    ================================================================================================
-->

## License

Each file in this repository is licensed under one of the following licenses:

- [Apache License, Version 2.0](LICENSES/Apache-2.0.txt),
- [Creative Commons CC0 1.0 Universal Public Domain Dedication](LICENSES/CC0-1.0.txt).

The applicable license is stated in the header comment of each file. 
See [LICENSE.txt](LICENSE.txt) for details.

<!--    
    ================================================================================================
-->
