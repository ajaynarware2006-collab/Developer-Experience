from database.connection import get_connection


SCHEMA = """

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,

    name VARCHAR(120) NOT NULL,

    email VARCHAR(255) UNIQUE NOT NULL,

    password_hash TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS developer_profiles (
    id SERIAL PRIMARY KEY,

    user_id INTEGER UNIQUE NOT NULL
        REFERENCES users(id)
        ON DELETE CASCADE,

    career_goal TEXT NOT NULL,

    experience_level VARCHAR(30) NOT NULL,

    experience TEXT NOT NULL,

    target VARCHAR(100) NOT NULL,

    timeline VARCHAR(50) NOT NULL,

    daily_time VARCHAR(50) NOT NULL
);


CREATE TABLE IF NOT EXISTS profile_skills (
    id SERIAL PRIMARY KEY,

    profile_id INTEGER NOT NULL
        REFERENCES developer_profiles(id)
        ON DELETE CASCADE,

    skill VARCHAR(100) NOT NULL,

    UNIQUE(profile_id, skill)
);


CREATE TABLE IF NOT EXISTS roadmaps (
    id SERIAL PRIMARY KEY,

    user_id INTEGER NOT NULL
        REFERENCES users(id)
        ON DELETE CASCADE,

    career_goal TEXT NOT NULL,

    timeline VARCHAR(50) NOT NULL,

    progress INTEGER DEFAULT 0,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS roadmap_phases (
    id SERIAL PRIMARY KEY,

    roadmap_id INTEGER NOT NULL
        REFERENCES roadmaps(id)
        ON DELETE CASCADE,

    title VARCHAR(200) NOT NULL,

    description TEXT,

    project VARCHAR(300),

    phase_order INTEGER NOT NULL
);


CREATE TABLE IF NOT EXISTS roadmap_tasks (
    id SERIAL PRIMARY KEY,

    phase_id INTEGER NOT NULL
        REFERENCES roadmap_phases(id)
        ON DELETE CASCADE,

    title VARCHAR(300) NOT NULL,

    task_order INTEGER NOT NULL,

    completed BOOLEAN DEFAULT FALSE
);

"""


def create_schema():

    with get_connection() as connection:

        with connection.cursor() as cursor:

            cursor.execute(SCHEMA)

        connection.commit()


if __name__ == "__main__":
    create_schema()

    print(
        "DEV/XP database schema created successfully."
    )