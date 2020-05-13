from project import main

async def get_refresh_token(name: str):
    db = main.get_db()
    query = ("""
        SELECT
            refresh_tokens.id as id,
            refresh_tokens.name as name,
            refresh_tokens.token as token
        FROM
            refresh_tokens
        WHERE
            refresh_tokens.name = :name;
    """)
    values = {
        'name': name
    }
    return await db.fetch_one(query, values)

async def create_refresh_token(name: str, token: str):
    db = main.get_db()
    query = ("""
        INSERT INTO refresh_tokens (
            id,
            name,
            token,
            created_at
        )
        VALUES (
            uuid_generate_v4(),
            :name,
            :token,
            clock_timestamp()
        )
        RETURNING refresh_tokens.id;
    """)
    values = {
        'name': name,
        'token': token
    }
    return await db.execute(query, values)

async def update_refresh_token(token_id: str, name: str, token: str):
    db = main.get_db()
    query = ("""
        UPDATE refresh_tokens
            SET name = :name,
                token = :token,
                updated_at = clock_timestamp()
        WHERE
            refresh_tokens.id = :token_id
            AND refresh_tokens.deleted_at IS NULL
        RETURNING
            refresh_tokens.id AS token_id;
    """)
    values = {
        'token_id': token_id,
        'name': name,
        'token': token
    }
    return await db.execute(query, values)