drop table if exists users;
create table users (
  id int(11) auto_increment PRIMARY KEY,
  name varchar(100),
  email varchar(100),
  username varchar(30),
  password varchar(100),
  register_date timestamp not null
);

drop table if exists articles;
create table articles (
  id int(11) PRIMARY KEY,
  title varchar(255),
  author varchar(100),
  body text,
  create_date timestamp not null
);

