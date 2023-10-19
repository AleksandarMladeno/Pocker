# app_poker

## project layout
- docs: project documentation will live in here.
- src: production code lives in folder and is divided in the modules below:
    - app_poker: project package
        - api:
            - the API to the application lives in this module.
            - the current implementation is a REST API, but a gRPC, CLI API, etc would be implemented in here.
        - core:
            - the domain logic of the application lives in this module.
        - gateway:
            - all external interaction objects(e.g. files, external APIs etc) live in this module.
        - model:
            - the domain models for Poker live in this in this module.
        - app.py:
            entry point to startup the application
- tests: test code lives in folder.
- utilities: any useful scripts, such as curl & postman requests, software installations.
