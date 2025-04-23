CREATE TABLE "Dealership"."Autos" (
    "PK_AutoID" smallint NOT NULL,
    "FK_ManufacturerID" smallint NOT NULL,
    "CarName" text NOT NULL,
    "Seatings" smallint NOT NULL,
    "Doors" smallint NOT NULL
);
ALTER TABLE "Dealership"."Autos" OWNER TO postgres;

CREATE TABLE "Dealership"."Clients" (
    "PK_ClientID" smallint NOT NULL,
    "ClientName" text NOT NULL,
    "ClientPhoneNo" character varying(15) NOT NULL
);
ALTER TABLE "Dealership"."Clients" OWNER TO postgres;

CREATE TABLE "Dealership"."Configurations" (
    "PF_AutoID" smallint NOT NULL,
    "EngineV" real NOT NULL,
    "AC" boolean NOT NULL,
    "Colour" text NOT NULL
);
ALTER TABLE "Dealership"."Configurations" OWNER TO postgres;

CREATE TABLE "Dealership"."Contracts" (
    "PK_ContractID" smallint NOT NULL,
    "FK_RequestID" integer NOT NULL,
    "FK_AutoID" smallint NOT NULL,
    "ContractDate" date NOT NULL
);
ALTER TABLE "Dealership"."Contracts" OWNER TO postgres;

CREATE TABLE "Dealership"."Manufacturers" (
    "PK_ManufacturerID" smallint NOT NULL,
    "Country" text NOT NULL,
    "Brand" text NOT NULL
);
ALTER TABLE "Dealership"."Manufacturers" OWNER TO postgres;

CREATE TABLE "Dealership"."Payments" (
    "PF_ContractID" smallint NOT NULL,
    "PaymentDate" timestamp without time zone NOT NULL,
    "Price" integer NOT NULL
ALTER TABLE "Dealership"."Payments" OWNER TO postgres;

CREATE TABLE "Dealership"."Requests" (
    "PK_RequestID" integer NOT NULL,
    "Client's request-description" text NOT NULL,
    "FK_ClientID" smallint NOT NULL,
    "FK_StaffID" smallint NOT NULL
);
ALTER TABLE "Dealership"."Requests" OWNER TO postgres;

CREATE SEQUENCE "Dealership"."Request_PK_RequestID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER SEQUENCE "Dealership"."Request_PK_RequestID_seq" OWNER TO postgres;
ALTER SEQUENCE "Dealership"."Request_PK_RequestID_seq" OWNED BY "Dealership"."Requests"."PK_RequestID";

CREATE TABLE "Dealership"."Staff" (
    "PK_StaffID" smallint NOT NULL,
    "StaffName" text NOT NULL,
    "StaffPhoneNo" character varying(15) NOT NULL
);
ALTER TABLE "Dealership"."Staff" OWNER TO postgres;

CREATE TABLE "Dealership"."TestDriveDatabase" (
    "PF_RequestID" integer NOT NULL,
    "FK_AutoID" smallint NOT NULL,
    "Date" timestamp without time zone NOT NULL
);
ALTER TABLE "Dealership"."TestDriveDatabase" OWNER TO postgres;

ALTER TABLE ONLY "Dealership"."Autos"
    ADD CONSTRAINT "Autos_pkey" PRIMARY KEY ("PK_AutoID");
ALTER TABLE ONLY "Dealership"."Clients"
    ADD CONSTRAINT "Clients_pkey" PRIMARY KEY ("PK_ClientID");
ALTER TABLE ONLY "Dealership"."Configurations"
    ADD CONSTRAINT "Configurations_pkey" PRIMARY KEY ("PF_AutoID");
ALTER TABLE ONLY "Dealership"."Contracts"
    ADD CONSTRAINT "Contracts_pkey" PRIMARY KEY ("PK_ContractID");
ALTER TABLE ONLY "Dealership"."Manufacturers"
    ADD CONSTRAINT "Manfactuers_pkey" PRIMARY KEY ("PK_ManufacturerID");
ALTER TABLE ONLY "Dealership"."Payments"
    ADD CONSTRAINT "Payments_pkey" PRIMARY KEY ("PF_ContractID");
ALTER TABLE ONLY "Dealership"."Requests"
    ADD CONSTRAINT "Request_pkey" PRIMARY KEY ("PK_RequestID");
ALTER TABLE ONLY "Dealership"."Staff"
    ADD CONSTRAINT "Staff_pkey" PRIMARY KEY ("PK_StaffID");
ALTER TABLE ONLY "Dealership"."TestDriveDatabase"
    ADD CONSTRAINT "TestDriveDatabase_pkey" PRIMARY KEY ("PF_RequestID");

ALTER TABLE ONLY "Dealership"."Autos"
    ADD CONSTRAINT "Autos_FK_ManufacturerID_fkey" FOREIGN KEY ("FK_ManufacturerID") REFERENCES "Dealership"."Manufacturers"("PK_ManufacturerID") ON UPDATE CASCADE NOT VALID;
ALTER TABLE ONLY "Dealership"."Configurations"
    ADD CONSTRAINT "Configurations_PF_AutoID_fkey" FOREIGN KEY ("PF_AutoID") REFERENCES "Dealership"."Autos"("PK_AutoID") ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
ALTER TABLE ONLY "Dealership"."Contracts"
    ADD CONSTRAINT "Contracts_FK_AutoID_fkey" FOREIGN KEY ("FK_AutoID") REFERENCES "Dealership"."Autos"("PK_AutoID") ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
ALTER TABLE ONLY "Dealership"."Contracts"
    ADD CONSTRAINT "Contracts_FK_RequestID_fkey" FOREIGN KEY ("FK_RequestID") REFERENCES "Dealership"."Requests"("PK_RequestID") ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
ALTER TABLE ONLY "Dealership"."Payments"
    ADD CONSTRAINT "Payments_PF_ContractID_fkey" FOREIGN KEY ("PF_ContractID") REFERENCES "Dealership"."Contracts"("PK_ContractID") ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
ALTER TABLE ONLY "Dealership"."Requests"
    ADD CONSTRAINT "Request_FK_ClientID_fkey" FOREIGN KEY ("FK_ClientID") REFERENCES "Dealership"."Clients"("PK_ClientID") ON UPDATE RESTRICT ON DELETE SET NULL NOT VALID;
ALTER TABLE ONLY "Dealership"."Requests"
    ADD CONSTRAINT "Request_FK_StaffID_fkey" FOREIGN KEY ("FK_StaffID") REFERENCES "Dealership"."Staff"("PK_StaffID") ON UPDATE RESTRICT ON DELETE SET NULL NOT VALID;
ALTER TABLE ONLY "Dealership"."TestDriveDatabase"
    ADD CONSTRAINT "TestDriveDatabase_FK_AutoID_fkey" FOREIGN KEY ("FK_AutoID") REFERENCES "Dealership"."Autos"("PK_AutoID") ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
ALTER TABLE ONLY "Dealership"."TestDriveDatabase"
    ADD CONSTRAINT "TestDriveDatabase_PF_RequestID_fkey" FOREIGN KEY ("PF_RequestID") REFERENCES "Dealership"."Requests"("PK_RequestID") ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
	   
