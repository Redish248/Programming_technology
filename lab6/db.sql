create table sites (
    id      integer CONSTRAINT id_url PRIMARY KEY,
    name    varchar(40) NOT NULL,
    url     varchar(40) NOT NULL
);

CREATE TABLE news_python (
    id          integer CONSTRAINT id_key PRIMARY KEY,
    site        integer NOT NULL REFERENCES sites (id),
    title       varchar(100) NOT NULL,
    link        varchar(40) NOT NULL,
    description  varchar NOT NULL,
    published   date
);