CREATE TABLE dataopstpreviewtable(
    id SERIAL PRIMARY key,
    reviewername varchar (255),
    reviewtitle varchar (255),
    reviewrating decimal (1),
    reviewcontent text,
    emailaddress varchar (255),
    country varchar(60),
    reviewdate DATE
);