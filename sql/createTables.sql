CREATE TABLE subscription(
	name varchar(30),
	phone varchar(30),
	scoringPlays BOOLEAN,
	playerOfDay BOOLEAN,
	playerOfWeek BOOLEAN,
	weekSummary BOOLEAN,
	PRIMARY KEY (phone)
);
CREATE TABLE messages(
	name varchar(30),
	message varchar(500),
	PRIMARY KEY (name)
);
CREATE TABLE playerOfDay(
	id INT not null auto_increment,
	day varchar(30),
	message varchar(500),
	url varchar(500),
	stats varchar(500),
	PRIMARY KEY(id)
);

CREATE TABLE curPlayerOfDay(
	id INT,
	day varchar(30),
	name varchar(500),
	url varchar(500),
	stats varchar(500),
	teamPic varchar(500),
	PRIMARY KEY(id)
);
