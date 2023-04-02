CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT,
    role INTEGER DEFAULT 0
);

CREATE TABLE profiles (
    id SERIAL PRIMARY KEY,
    username TEXT,
    age INTEGER,
    bio TEXT,
    opiskelu TEXT
    user_id INTEGER REFERENCES users(id) --Possibility to add image?
);
    
CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    user1_id INTEGER REFERENCES users(id),
    user2_id INTEGER REFERENCES users(id),
    match_time TIMESTAMP DEFAULT NOW()
);

CREATE TABLE swipes (
    id SERIAL PRIMARY KEY,
    swiper_id INTEGER REFERENCES users(id),
    swiped_id INTEGER REFERENCES users(id),
    direction INTEGER,
    swipe_time TIMESTAMP DEFAULT NOW()
);

CREATE TABLE chats (
    id SERIAL PRIMARY KEY,
    user1_id INTEGER REFERENCES users(id),
    user2_id INTEGER REFERENCES users(id),
    start_time TIMESTAMP DEFAULT NOW()
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    chat_id INTEGER REFERENCES chats(id),
    chatter1_id INTEGER REFERENCES users(id),
    chatter2_id INTEGER REFERENCES users(id),
    message TEXT,
    message_sent TIMESTAMP DEFAULT NOW()
);
