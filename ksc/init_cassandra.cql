CREATE KEYSPACE ddt WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};


CREATE TABLE ddt.tweets (

    tweet_id uuid,

    text text,

    created_at timestamp,

    url text,

    PRIMARY KEY (tweet_id, text)

);
