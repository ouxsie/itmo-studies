INSERT INTO "Dealership"."Clients"(	"PK_ClientID", "ClientName", "ClientPhoneNo")	VALUES 
	(11, 'Третьяк Елизавета Сергеевна', 79110000000),
	(12, 'Николаев Никита Антонович', 12080000000),
	(13, 'Савченко Александр Петрович', 79210000000),
	(14, 'Розалес Диего Алонсо', 12080000000);

INSERT INTO "Dealership"."Staff" VALUES 
	(21, 'Пыркин Антон Александрович', 79110000000),
	(22, 'Мазурин Илья Владимирович', 79210000000),
	(23, 'Рогина Ольга Станиславовна', 79050000000),
	(24, 'Джефри Эндрю Фредерик', 79810000000);

INSERT INTO "Dealership"."Manufacturers" VALUES 
	(91, 'Germany', 'Porsche'), 
	(92, 'China', 'Zeekr'), 
	(93, 'China', 'LiXiang'), 
	(94, 'USA', 'Dodge');

INSERT INTO "Dealership"."Autos"
	VALUES (81, 91,'Porsche Cayman', 2, 3),
	(82, 91,'Porsche Cayenne', 5, 5),
	(83, 92,'Zeekr 009', 6, 5),
	(84, 93,'LiXiang L9', 6, 5),
	(85, 94,'Dodge Challenger', 5, 3),
	(86, 93,'LiXiang L7', 5, 5);

INSERT INTO "Dealership"."Configurations" VALUES
	(81, 2.9, true, 'Red'),
	(82, 4.8, true, 'Brown'),
	(83, 0, true, 'Yellow'),
	(84, 1.5, true, 'Grey'),
	(85, 6.2, false, 'Red'),
	(86, 1.5, true, 'White');

INSERT INTO "Dealership"."Requests" 
("PK_RequestID", "FK_ClientID", "FK_StaffID", "Client's request-description")
	VALUES (51, 11, 24, 'Хочу лучший порш в мире!'),
	(52, 13, 21, 'Мне нужна китайская бюджетная машина с кондиционером.'),
	(53, 12, 22, 'Какие у вас есть большие машины, чтобы я мог возить всю свою семью и дрова на 
дачу?'),
	(54, 14, 23, 'Hii, do u speak eng? I need a faast car! Really fast one!'),
	(55, 11, 22, 'Я ищу быструю красивую машину: с кондиционером и большим двигателем, чтобы 
ездить по хайвеям'),
	(56, 12, 23, 'Я хочу кабриолет! Любой, бюджет не ограничен.');

INSERT INTO "Dealership"."TestDriveDatabase" VALUES
	(51, 81, '2024-10-26 12:00:00'),
	(52, 86, '2024-11-05 10:30:00'),
	(54, 81, '2024-11-10 15:10:00'),
	(53, 84, '2024-11-10 12:00:00'),
	(55, 85, '2024-11-11 18:00:00'),
	(56, 81, '2024-11-25 14:00:00');

INSERT INTO "Dealership"."Contracts" VALUES
	(61, 51, 81, '2024-11-02'),
	(62, 52, 86, '2024-11-09'),
	(63, 53, 84, '2024-11-20'),
	(64, 54, 81, '2024-11-12'),
	(65, 55, 85, '2024-11-12'),
	(66, 56, 81, '2024-12-27');

INSERT INTO "Dealership"."Payments" VALUES
	(61, '2024-11-02 14:30:58', 11621500),
	(62, '2024-11-10 14:20:00', 4100000),
	(63, '2024-11-21 17:30:12', 8300000),
	(64, '2024-11-13 11:17:23', 11621500),
	(65, '2024-11-13 14:38:40', 5349000),
	(66, '2024-11-27 20:33:33', 30704990);
