<?php
$counter = 0;
$max = 0;

while($line = fgets(STDIN)) {
    $line = trim($line);

    if (empty($line)) {
        $max = max($counter, $max);
        $counter = 0;
        continue;
    }

    $counter += intval($line);
}

echo $max . PHP_EOL;
