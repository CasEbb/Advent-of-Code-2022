<?php
const ROCK = 'r';
const PAPER = 'p';
const SCISSORS = 's';
const OPPONENT = [
    'A' => ROCK,
    'B' => PAPER,
    'C' => SCISSORS,
];

const ME = [
    'X' => ROCK,
    'Y' => PAPER,
    'Z' => SCISSORS,
];

$score = 0;
$fp = fopen("input", "r");

while($line = fgets($fp)) {
    $line = trim($line);
    [$opponentChoice, $myChoice] = explode(" ", $line);
    $round = 0;

    // Points for choice
    switch(ME[$myChoice]) {
        case ROCK:
            $round += 1;
            if (OPPONENT[$opponentChoice] === ROCK) $round += 3;  // draw
            if (OPPONENT[$opponentChoice] === SCISSORS) $round += 6;  // win
            break;
        case PAPER:
            $round += 2;
            if (OPPONENT[$opponentChoice] === PAPER) $round += 3;  // draw
            if (OPPONENT[$opponentChoice] === ROCK) $round += 6;  // win
            break;
        case SCISSORS:
            $round += 3;
            if (OPPONENT[$opponentChoice] === SCISSORS) $round += 3;  // draw
            if (OPPONENT[$opponentChoice] === PAPER) $round += 6;  // win
            break;
    }

    $score += $round;
}

echo $score . PHP_EOL;
