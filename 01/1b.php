<?php
$counter = 0;
$inventory = [];

while($line = fgets(STDIN)) {
    $line = trim($line);

    if (empty($line)) {
        array_push($inventory, $counter);
        $counter = 0;
        continue;
    }

    $counter += intval($line);
}

rsort($inventory);
$top3 = array_slice($inventory, 0, 3);
$sum = array_sum($top3);

echo $sum . PHP_EOL;
