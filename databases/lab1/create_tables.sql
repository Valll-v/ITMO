CREATE TABLE IF NOT EXISTS class (
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(64) UNIQUE NOT NULL,
    "description" TEXT
);

CREATE TABLE IF NOT EXISTS person (
    "id" SERIAL PRIMARY KEY,
    "firstname" VARCHAR(32) NOT NULL,
    "lastname" VARCHAR(32) NOT NULL
);

CREATE TABLE IF NOT EXISTS report (
    "id" SERIAL PRIMARY KEY,
    "description" TEXT
);

CREATE TABLE IF NOT EXISTS action (
    "id" SERIAL PRIMARY KEY,
    "person_id" INT NOT NULL,
    "name" VARCHAR(64) NOT NULL,
    "description" TEXT,
    "report_id" INT,
    CONSTRAINT fk_action_person FOREIGN KEY(person_id) REFERENCES person(id),
    CONSTRAINT fk_action_report FOREIGN KEY(report_id) REFERENCES report(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS item (
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(128) NOT NULL,
    "description" TEXT,
    "is_available" BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS action_item (
    "action_id" INT NOT NULL,
    "item_id" INT NOT NULL,
    PRIMARY KEY (action_id, item_id),
    CONSTRAINT fk_action_item_action FOREIGN KEY(action_id) REFERENCES action(id),
    CONSTRAINT fk_action_item_item FOREIGN KEY(item_id) REFERENCES item(id)
);

CREATE TABLE IF NOT EXISTS person_report (
    "person_id" INT NOT NULL,
    "report_id" INT NOT NULL,
    PRIMARY KEY (person_id, report_id),
    CONSTRAINT fk_person_report_person FOREIGN KEY(person_id) REFERENCES person(id),
    CONSTRAINT fk_person_report_report FOREIGN KEY(report_id) REFERENCES report(id)
);


CREATE TABLE IF NOT EXISTS person_class (
    "person_id" INT NOT NULL,
    "class_id" INT NOT NULL,
    PRIMARY KEY (person_id, class_id),
    CONSTRAINT fk_person_class_person FOREIGN KEY(person_id) REFERENCES person(id),
    CONSTRAINT fk_person_class_class FOREIGN KEY(class_id) REFERENCES class(id)
);