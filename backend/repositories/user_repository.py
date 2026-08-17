from backend.database.connection import get_connection


def create_user(
    name: str,
    email: str,
    password_hash: str,
):
    query = """
        INSERT INTO users (
            name,
            email,
            password_hash
        )
        VALUES (%s, %s, %s)
        RETURNING id, name, email;
    """

    with get_connection() as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                query,
                (
                    name,
                    email,
                    password_hash,
                ),
            )

            user = cursor.fetchone()

        connection.commit()

    return user


def get_user_by_email(email: str):

    query = """
        SELECT
            id,
            name,
            email,
            password_hash
        FROM users
        WHERE email = %s;
    """

    with get_connection() as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                query,
                (email,),
            )

            return cursor.fetchone()