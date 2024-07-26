-- Request all the weaponary names with 9x18 as a caliber
SELECT w_name FROM weapons_specs WHERE caliber = '9x18'

-- Request all the orders of 'Вепрь-12' (Vepr-12, Russian tactical shotgun) 
-- dated between Mar 1, 2022 and Apr 1, 2022
SELECT * FROM orders WHERE (SELECT w_name FROM weapons_specs 
	WHERE weapons_specs.weapon_id = orders.what_weapon) = 'Вепрь-12' 
AND order_date BETWEEN '2022-03-01' AND '2022-04-01'

-- Request names and weight of the models which cost more than 50 000 some-kind-of-a-urrency lol
SELECT ALL model_name, weight FROM weapons_gen_specs 
WHERE avg_price > 50000

-- Pull up the name and a phone mumber of the buyer of a rifle 
-- with a serial mentioned below from the MVD's (Russian Ministry of Internal Affairs) database
SELECT name, phone_num FROM clients 
WHERE  Name = (SELECT mvd_client FROM mvd_data 
        WHERE weapon_serial = 'ORSIS12949285')

-- Count all the 'Револьверы' (revolvers)
SELECT COUNT(*) FROM weapons_gen_specs WHERE type_weapon = 'Револьвер'
