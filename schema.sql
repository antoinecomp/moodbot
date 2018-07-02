drop table if exists users;
create table users (
  id int auto_increment PRIMARY KEY,
  name varchar,
  email varchar,
  username varchar,
  password varchar,
  register_date timestamp not null
);

drop table if exists articles;
create table articles (
  id int PRIMARY KEY,
  title varchar,
  author varchar,
  body text,
  create_date timestamp not null
);

