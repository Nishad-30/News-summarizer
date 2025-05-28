create database News;

use news;

create table accounts(
email varchar(100),
name varchar(100),
passwaord varchar(50)
);

INSERT into accounts values("nishad@gmail.com","Nishad Sutar", "12345");

create table bookmark(
email varchar(100),
title varchar(5000),
content varchar(5000),
link varchar(5000)
);

insert into bookmark values("dem0@gmail.com", "", "", "", "");