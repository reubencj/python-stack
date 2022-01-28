-- use dojos_and_ninjas_schema;

-- insert into dojos (name) values('New York');
-- insert into dojos (name) values('San Jose');
-- insert into dojos (name) values('Seattle');


-- delete from dojos;

-- insert into dojos (name) values('New York');
-- insert into dojos (name) values('San Jose');
-- insert into dojos (name) values('Seattle');


insert into ninjas(first_name, last_name, age, dojo_id) values('reuben','john',32,4);
insert into ninjas(first_name, last_name, age, dojo_id) values('karen','john',28,4);
insert into ninjas(first_name, last_name, age, dojo_id) values('judah','john',2,4);

insert into ninjas(first_name, last_name, age, dojo_id) values('bear','john',32,5);
insert into ninjas(first_name, last_name, age, dojo_id) values('cub','john',28,5);
insert into ninjas(first_name, last_name, age, dojo_id) values('cubby','john',2,5);

insert into ninjas(first_name, last_name, age, dojo_id) values('zip','john',32,6);
insert into ninjas(first_name, last_name, age, dojo_id) values('light','john',28,6);
insert into ninjas(first_name, last_name, age, dojo_id) values('fire','john',2,6);



select * from ninjas where dojo_id = (select id from dojos where name = 'New York');
select * from ninjas where dojo_id = (select id from dojos where name = 'San Jose');
select * from ninjas where id = (select max(id) from ninjas)

