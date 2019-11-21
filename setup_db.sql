INSERT INTO "spatial_unit" (id, address)
VALUES (1, '10 Spicer Road, EX1 1AB'),
       (2, 'Flat 1, 10 Spicer Road, EX1 1AB'),
       (3, 'Flat 2, 10 Spicer Road, EX1 1AB'),
       (4, 'Flat 3, 10 Spicer Road, EX1 1AB'),
       (5, 'Flat 4, 10 Spicer Road, EX1 1AB'),
       (6, ''),
       (7, '30 Barnfield Road, EX1 1AB'),
       (8, 'Flat 1, 30 Barnfield Road, EX1 1AB'),
       (9, 'Flat 2, 30 Barnfield Road, EX1 1AB'),
       (10, 'Flat 3, 30 Barnfield Road, EX1 1AB'),
       (11, 'Flat 4, 30 Barnfield Road, EX1 1AB'),
       (12, 'Flat 5, 30 Barnfield Road, EX1 1AB'),
       (13, 'Flat 6, 30 Barnfield Road, EX1 1AB'),
       (14, 'Flat 7, 30 Barnfield Road, EX1 1AB'),
       (15, 'Flat 8, 30 Barnfield Road, EX1 1AB'),
       (16, 'St. Joseph Hospital, Denmark Road, EX1 1AB');

INSERT INTO "ba_unit" (id, name)
VALUES (1, 'ABCD123'),
       (2, 'EFGH123'),
       (3, 'IJKL123'),
       (4, 'MNOP123'),
       (5, 'QRST123'),
       (6, 'UVWX123'),
       (7, 'YZAB123'),
       (8, 'CDEF123'),
       (9, 'GHIJ123'),
       (10, 'KLMN123'),
       (11, 'OPQR123'),
       (12, 'STUV123'),
       (13, 'WXYZ123'),
       (14, 'ABCD456'),
       (15, 'EFGH456'),
       (16, 'IJKL456');

INSERT INTO "price_paid" (id, spatial_unit_id, amount, date)
VALUES (1, 1, 500000, DATE '2006-10-05'),
       (2, 2, 105000, DATE '2008-01-18'),
       (3, 1, 1000000, DATE '2009-12-03'),
       (4, 5, 140000, DATE '2010-04-01'),
       (5, 4, 139000, DATE '2010-11-21'),
       (6, 2, 104000, DATE '2011-06-13'),
       (7, 2, 153000, DATE '2013-05-08'),
       (8, 3, 145000, DATE '2016-02-26'),
       (9, 6, 200000, DATE '2019-03-15'),
       (10, 7, 120000, DATE '2019-08-01'),
       (11, 8, 100000, DATE '2019-01-12'),
       (12, 9, 113000, DATE '2019-12-29'),
       (13, 10, 100000, DATE '2019-09-07'),
       (14, 11, 950000, DATE '2019-05-03'),
       (15, 12, 980000, DATE '2019-06-14'),
       (16, 13, 102000, DATE '2019-02-23'),
       (17, 14, 105000, DATE '2019-01-18'),
       (18, 15, 110000, DATE '2019-06-06'),
       (19, 16, 1000000, DATE '1998-03-26');

INSERT INTO "spatial_unit_ba_unit_association" (spatial_unit_id, ba_unit_id)
VALUES (1, 1),
       (2, 2),
       (3, 3),
       (4, 4),
       (5, 5),
       (6, 6),
       (7, 7),
       (8, 8),
       (9, 9),
       (10, 10),
       (11, 11),
       (12, 12),
       (13, 13),
       (14, 14),
       (15, 15),
       (16, 16);

INSERT INTO "party" (id, name, type)
VALUES  (1, 'Peter Morris', 'Individual'),
        (2, 'Alexandra Bailey', 'Individual'),
        (3, 'Jack Farrell', 'Individual'),
        (4, 'Jennifer Patterson', 'Individual'),
        (5, 'Hollister Bank', 'Organisation'),
        (6, 'Jacob Daniels', 'Individual'),
        (7, 'Airspace Limited', 'Organisation'),
        (8, 'Woodbury Bank', 'Organisation'),
        (9, 'Royal Bank', 'Organisation'),
        (10, 'Western Bank', 'Organisation'),
        (11, 'NHS', 'Organisation');

INSERT INTO "restriction" (id, ba_unit_id, description, type, party_id, start_date, end_date)
VALUES (1, 1, '', 'Mortgage', 8, '2006-10-05', '2041-10-05'),
       (2, 2, '', 'Easement', 3, NULL, NULL),
       (3, 2, '', 'Mortgage', 9, '2008-01-18', '2033-01-18'),
       (4, 3, '', 'Mortgage', 5, '2016-02-26', '2036-02-26'),
       (5, 4, '', 'Mortgage', 5, '2010-11-21', '2040-11-21'),
       (6, 5, '', 'Mortgage', 10, '2010-04-01', '2035-04-01'),
       (7, 5, '', 'Easement', 7, NULL, NULL),
       (8, 6, '', 'Mortgage', 9, '2019-03-15', '2034-03-15'),
       (9, 7, '', 'Mortgage', 10, '2019-03-15', '2034-03-15'),
       (10, 8, '', 'Mortgage', 10, '2019-03-15', '2034-03-15'),
       (11, 9, '', 'Mortgage', 8, '2019-03-15', '2034-03-15'),
       (12, 10, '', 'Mortgage', 5, '2019-03-15', '2034-03-15'),
       (13, 11, '', 'Mortgage', 8, '2019-03-15', '2034-03-15'),
       (14, 12, '', 'Mortgage', 9, '2019-03-15', '2034-03-15'),
       (15, 15, '', 'Mortgage', 9, '2019-03-15', '2034-03-15');

INSERT INTO "right" (id, ba_unit_id, description, type, party_id, start_date, end_date)
VALUES (1, 1, 'Ownership of the land, its subsoil and airspace', 'Absolute Freehold', 1, '2006-10-05', NULL),
       (2, 2, 'Ownership of entire flat', 'Leasehold', 2, '2008-01-18', '2128-01-18'),
       (3, 3, 'Ownership of entire flat', 'Leasehold', 3, '2016-02-26', '2136-02-26'),
       (4, 4, 'Ownership of entire flat', 'Leasehold', 4, '2010-11-21', '2130-11-21'),
       (5, 5, 'Ownership of entire flat', 'Leasehold', 6, '2010-04-01', '2145-04-01'),
       (6, 6, 'Ownership of the airspace above the building, rising 15 metres vertically from the outer edge and flat roof of the building', 'Airspace Leasehold', 7, '2019-03-15', '2139-03-15'),
       (7, 7, 'Ownership of the land, its subsoil and airspace', 'Absolute Freehold', 2, '2008-01-18', NULL),
       (8, 8, 'Ownership of entire flat', 'Leasehold', 3, '2016-02-26', '2136-02-26'),
       (9, 9, 'Ownership of entire flat', 'Leasehold', 4, '2010-11-21', '2130-11-21'),
       (10, 10, 'Ownership of entire flat', 'Leasehold', 2, '2010-04-01', '2145-04-01'),
       (11, 11, 'Ownership of entire flat', 'Leasehold', 3, '2010-04-01', '2145-04-01'),
       (12, 12, 'Ownership of entire flat', 'Leasehold', 4, '2010-04-01', '2145-04-01'),
       (13, 13, 'Ownership of entire flat', 'Leasehold', 6, '2010-04-01', '2145-04-01'),
       (14, 14, 'Ownership of entire flat', 'Leasehold', 2, '2010-04-01', '2145-04-01'),
       (15, 15, 'Ownership of entire flat', 'Leasehold', 3, '2010-04-01', '2145-04-01'),
       (16, 16, 'Ownership of the land, its subsoil and airspace', 'Absolute Freehold', 11, '1998-03-26', NULL);

INSERT INTO "responsibility" (id, ba_unit_id, description, type, party_id, start_date, end_date)
VALUES (1, 1, '', 'Building maintenance', 1, NULL, NULL),
       (2, 1, '', 'Monument maintenance', 1, NULL, NULL),
       (3, 2, '', 'Building maintenance', 2, NULL, NULL),
       (4, 3, '', 'Building maintenance', 3, NULL, NULL),
       (5, 4, '', 'Building maintenance', 4, NULL, NULL),
       (6, 5, '', 'Building maintenance', 6, NULL, NULL),
       (7, 6, '', 'Building maintenance', 7, NULL, NULL);


ALTER SEQUENCE "ba_unit_id_seq" RESTART WITH 17; 
ALTER SEQUENCE "price_paid_id_seq" RESTART WITH 20;
ALTER SEQUENCE "party_id_seq" RESTART WITH 12;
ALTER SEQUENCE "restriction_id_seq" RESTART WITH 16;
ALTER SEQUENCE "right_id_seq" RESTART WITH 17;
ALTER SEQUENCE "responsibility_id_seq" RESTART WITH 7;
