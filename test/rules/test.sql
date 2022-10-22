alter table tbl
add column col1 TEXT default ''
not null;

alter table tbl
add column col1 TEXT
not null;

alter table tbl
add column col1 TEXT default '';

alter table tbl
add column col1 TEXT default null not null;

alter table tbl
add column col1 TEXT not null,
add column col2 TEXT default '' not null,
add column col3 TEXT not null;

create table tbl (
    col1 TEXT not null,
    col2 TEXT default '' not null
);
