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
