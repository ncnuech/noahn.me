CREATE TABLE subscription(
	name varchar(30),
	phone varchar(30),
	scoringPlays BOOLEAN,
	playerOfDay BOOLEAN,
	playerOfWeek BOOLEAN,
	weekSummary BOOLEAN,
	PRIMARY KEY (phone)
);
