CREATE TABLE advertiser(
    id INTEGER,
    full_name varchar(50),
    views INTEGER DEFAULT 0,
    clicks INTEGER DEFAULT 0,
    PRIMARY KEY(id),
    
);

CREATE TABLE ad(
    id INTEGER,
    views INTEGER DEFAULT 0,
    clicks INTEGER DEFAULT 0,
    advertiser_id INTEGER,
    FOREIGN KEY(advertiser_id) REFERENCES advertiser(id)
    
);