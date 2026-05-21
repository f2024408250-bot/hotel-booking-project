CREATE TABLE IF NOT EXISTS bookings (
    id               SERIAL PRIMARY KEY,
    full_name        VARCHAR(100)  NOT NULL,
    email            VARCHAR(150)  NOT NULL,
    phone            VARCHAR(30)   NOT NULL,
    check_in         DATE          NOT NULL,
    check_out        DATE          NOT NULL,
    room_type        VARCHAR(50)   NOT NULL,
    guests           INTEGER       NOT NULL,
    special_requests TEXT,
    created_at       TIMESTAMP     DEFAULT NOW()
);
