<?php
// Open the database:
if (!($db = sqlite_open('example.db'))) {
    // Handle errors
    die('SQL ERROR: Open failed: ' .
        sqlite_error_string(sqlite_last_error($db)));
}

// Prepare the database creation:
$sql = "
create table example (
    id   integer  primary key,
    desc text     not null,
    qty  integer  not null
);

insert into example (desc, qty) values ('test1', 10);
insert into example (desc, qty) values ('test2', 1);
insert into example (desc, qty) values ('test3', 2);
";

// Create it all:
if (!(sqlite_exec($db, $sql))) {
    // Give an error statement:
    die('SQL ERROR: ' . sqlite_error_string(sqlite_last_error($db)) .
        " - Query was: {$sql}");
} else {
    echo 'SUCCESS!';
}

// Now close the database
sqlite_close($db);

// Open the database:
if (!($db = sqlite_open('example.db'))) {
    // Handle errors
    die('SQL ERROR: Open failed: ' .
        sqlite_error_string(sqlite_last_error($db)));
}

// Prepare a SQL insert: assume we received the description from the user
$desc = 'TEST';
$escaped = sqlite_escape_string($desc);
$sql = "insert into example (desc, qty) values ('{$escaped}', 0)";

// Do the insert
if (!(sqlite_query($db, $sql))) {
    // Give an error statement:
    die('SQL ERROR: ' . sqlite_error_string(sqlite_last_error($db)) .
        " - Query was: {$sql}");
}

// Select data from the table:
$sql = 'select id, desc from example order by id asc';
if (!($result = sqlite_query($db, $sql))) {
    // Give an error statement:
    die('SQL ERROR: ' . sqlite_error_string(sqlite_last_error($db)) .
        " - Query was: {$sql}");
}

// Read all the data back in as associative arrays
while ($row = sqlite_fetch_array($result)) {
    echo "{$row['id']}. {$row['desc']}
\n";
}

// Now close the connection
sqlite_close($db);


?>