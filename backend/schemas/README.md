# Pydantic Schemas

Each SQLAlchemy model has three Pydantic schemas:

- `*Create` — input when creating a record.
- `*Update` — partial input when updating a record; fields are optional.
- `*Response` — safe output returned by the API.

`from_attributes=True` allows FastAPI/Pydantic to build response schemas directly from SQLAlchemy ORM objects.

`EmailVerificationCreate.code` is the plaintext verification code accepted at the API/service boundary. It should be hashed before saving to the `code_hash` database column. `code_hash` is intentionally never exposed by the response schema.
