# Deterministic Password Generator CLI

This script generates **deterministic passwords** based on a master password and a site name, ensuring that the same inputs always produce the same output. It is designed to create secure, fixed-length passwords that meet most common character requirements.

---

## Features

- **Deterministic Output**: Same inputs (master password and site name) always produce the same password.
- **Secure Hashing**: Uses `SHA-256` to create a base for the password.
- **Meets Common Requirements**: Includes lowercase letters, numbers, an uppercase letter, and a symbol.
- **Fixed Length**: Output passwords are always 12 characters long.

---

## How It Works

1. The script combines the master password and the site name.
2. It hashes the combination using `SHA-256`.
3. The first 10 characters of the hash are used as the base for the password.
4. A fixed uppercase letter (`A`) and a symbol (`@`) are appended to ensure compliance with character requirements.

---

## Example

**Inputs**:
- Master Password: `MySecretPassword`
- Site Name: `amazon`

**Output**:
- a1b2c3d4e5f6A@
