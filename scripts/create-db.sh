#!/bin/bash
set -e

# Check if database already exists
if psql -U "$POSTGRES_USER" -lqt | cut -d \| -f 1 | grep -qw "$POSTGRES_DB"; then
    echo "$POSTGRES_DB database already exists"
else
    echo "Creating $POSTGRES_DB database..."
    createdb -U postgres "$POSTGRES_DB"
fi
