CREATE TABLE Weapons_gen_specs (
	Type_weapon VARCHAR(10),
	Model_name TEXT PRIMARY KEY,
	Brand TEXT NOT NULL,
	Speed VARCHAR(2) NOT NULL,
	Weight VARCHAR(2) NOT NULL,
	Avg_Price VARCHAR(7) NOT NULL
);

CREATE  TABLE Weapons_specs (
	Weapon_Id SERIAL PRIMARY KEY,
	W_Name TEXT REFERENCES Weapons_gen_specs (Model_name),
	Caliber VARCHAR(15) NOT NULL
);

CREATE TABLE Clients (
	Client_Id SERIAL PRIMARY KEY,
	Phone_num VARCHAR(20) UNIQUE NOT NULL,
	Name TEXT NOT NULL UNIQUE
);

CREATE TABLE Orders (
	Order_Id SERIAL PRIMARY KEY,
	Order_Date TIMESTAMP NOT NULL,
	O_Client_Id SERIAL REFERENCES Clients (Client_Id),
	Delivery_address TEXT NOT NULL,
	Order_Price VARCHAR(20) NOT NULL,
	What_weapon SERIAL REFERENCES Weapons_Specs (Weapon_Id)
);
-- hereinafter: MVD is an acronym for the Russian Ministry of Internal Affairs.
CREATE TABLE MVD_Data (
	MVD_Order_Id SERIAL REFERENCES Orders (Order_Id),
	MVD_client TEXT REFERENCES Clients (Name),
	MVD_Model_name TEXT REFERENCES Weapons_gen_specs (Model_name),
	Weapon_Serial VARCHAR(20) NOT NULL
