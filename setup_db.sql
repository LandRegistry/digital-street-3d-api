INSERT INTO "spatial_unit" (id, address)
VALUES (1, 'Princesshay'),
       (2, 'Princesshay'),
       (3, 'Princesshay'),
       (4, 'Princesshay'),
       (5, 'Princesshay'),
       (6, 'Princesshay'),
       (7, 'Princesshay'),
       (8, 'Princesshay'),
       (9, 'Princesshay'),
       (10, 'Princesshay'),
       (11, 'Princesshay'),
       (21, 'Princesshay'),
       (22, 'Princesshay'),
       (23, 'Princesshay'),
       (24, 'Princesshay'),
       (25, 'Princesshay'),
       (26, 'Princesshay'),
       (27, 'Princesshay'),
       (28, 'Princesshay'),
       (29, 'Princesshay');

INSERT INTO "ba_unit" (id, name)
VALUES (1, 'Test'),
       (2, 'Test'),
       (3, 'Test'),
       (4, 'Test'),
       (5, 'Test'),
       (6, 'Test'),
       (7, 'Test'),
       (8, 'Test'),
       (9, 'Test'),
       (10, 'Test'),
       (11, 'Test'),
       (12, 'Test'),
       (13, 'Test'),
       (14, 'Test'),
       (15, 'Test'),
       (16, 'Test'),
       (17, 'Test'),
       (18, 'Test'),
       (19, 'Test'),
       (20, 'Test');

INSERT INTO "spatial_unit_ba_unit_mapping" (spatial_unit_id, ba_unit_id)
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
       (21, 12),
       (22, 13),
       (23, 14),
       (24, 15),
       (25, 16),
       (26, 17),
       (27, 18),
       (28, 19),
       (29, 20);

INSERT INTO "interest" (id, description, ba_unit_id)
VALUES (1, 'An interest', 1),
       (2, 'An interest', 1),
       (3, 'An interest', 1),
       (4, 'An interest', 2),
       (5, 'An interest', 3),
       (6, 'An interest', 4),
       (7, 'An interest', 5),
       (8, 'An interest', 5),
       (9, 'An interest', 6),
       (10, 'An interest', 6),
       (11, 'An interest', 7),
       (12, 'An interest', 7),
       (13, 'An interest', 8),
       (14, 'An interest', 9),
       (15, 'An interest', 10),
       (16, 'An interest', 11),
       (17, 'An interest', 12),
       (18, 'An interest', 13),
       (19, 'An interest', 13),
       (20, 'An interest', 14),
       (21, 'An interest', 15),
       (22, 'An interest', 15),
       (23, 'An interest', 16),
       (24, 'An interest', 17),
       (25, 'An interest', 18),
       (26, 'An interest', 19),
       (27, 'An interest', 20);

INSERT INTO "party" (id, name, type)
VALUES (1, 'Peter Morris', 'Individual');

INSERT INTO "restriction" (id, interest_id, type, party_required)
VALUES (1, 1, 'Mortgage', TRUE),
       (2, 2, 'Easement', FALSE),
       (3, 5, 'Mortgage', TRUE),
       (4, 7, 'Mortgage', TRUE),
       (5, 8, 'Mortgage', TRUE),
       (6, 9, 'Easement', FALSE),
       (7, 12, 'Mortgage', TRUE),
       (8, 14, 'Mortgage', TRUE),
       (9, 16, 'Mortgage', TRUE),
       (10, 17, 'Mortgage', TRUE),
       (11, 18, 'Mortgage', TRUE),
       (12, 20, 'Easement', FALSE),
       (13, 22, 'Mortgage', TRUE),
       (14, 23, 'Mortgage', TRUE),
       (15, 25, 'Easement', FALSE),
       (16, 27, 'Mortgage', TRUE);

INSERT INTO "mortgage" (id, restriction_id, type, amount, interest_rate)
VALUES (1, 1, 'Fixed Rate Mortgage', 257000, 3.5),
       (2, 3, 'Variable Mortgage', 123000, 2),
       (3, 4, 'Variable Mortgage', 450000, 1.5),
       (4, 5, 'Fixed Rate Mortgage', 335000, 3.1),
       (5, 7, 'Fixed Rate Mortgage', 275500, 2.4),
       (6, 8, 'Fixed Rate Mortgage', 181000, 5.5),
       (7, 9, 'Variable Mortgage', 234000, 3),
       (8, 10, 'Fixed Rate Mortgage', 110000, 2.7),
       (9, 11, 'Variable Mortgage', 366000, 1.9),
       (10, 13, 'Fixed Rate Mortgage', 645000, 2.8),
       (11, 14, 'Fixed Rate Mortgage', 521500, 3.3),
       (12, 16, 'Fixed Rate Mortgage', 415000, 4.3);

INSERT INTO "right" (id, interest_id, type)
VALUES (1, 3, 'Ownership'),
       (2, 4, 'Ownership'),
       (3, 6, 'Ownership'),
       (4, 10, 'Ownership'),
       (5, 13, 'Ownership'),
       (6, 15, 'Ownership'),
       (7, 19, 'Ownership'),
       (8, 21, 'Ownership'),
       (9, 24, 'Ownership'),
       (10, 26, 'Ownership');

INSERT INTO "responsibility" (id, interest_id, type)
VALUES (1, 11, 'Monument maintenance');


ALTER SEQUENCE "ba_unit_id_seq" RESTART WITH 21;
ALTER SEQUENCE "interest_id_seq" RESTART WITH 28;
ALTER SEQUENCE "party_id_seq" RESTART WITH 2;
ALTER SEQUENCE "restriction_id_seq" RESTART WITH 17;
ALTER SEQUENCE "mortgage_id_seq" RESTART WITH 13;
ALTER SEQUENCE "right_id_seq" RESTART WITH 11;
ALTER SEQUENCE "responsibility_id_seq" RESTART WITH 2;
