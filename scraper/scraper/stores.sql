create table stores
(
    id int auto_increment
	storeID int not null,
	storeName varchar(200) not null,
	address varchar(200) not null,
	telephone varchar(40) null,
	constraint stores_pk
		primary key (id)
);

create index stores_storeName_index
	on stores (storeName desc);

create index stores_storeName_index
	on stores (storeID desc);

commit;