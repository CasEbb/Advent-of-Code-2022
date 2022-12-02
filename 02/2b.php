<?php
const ROCK = 'r';
const PAPER = 'p';
const SCISSORS = 's';
const OPPONENT = [
    'A' => ROCK,
    'B' => PAPER,
    'C' => SCISSORS,
];
const WIN = 'w';
const DRAW = 'd';
const LOSE = 'l';
const ME = [
    'X' => LOSE,
    'Y' => DRAW,
    'Z' => WIN,
];

$score = 0;
$fp = fopen("input", "r");

while($line = fgets($fp)) {
    $line = trim($line);
    [$opponentChoice, $myChoice] = explode(" ", $line);
    $round = 0;

    // Points for choice
    switch(ME[$myChoice]) {
        case LOSE:
            if (OPPONENT[$opponentChoice] === ROCK) $round += 3;  // I chose scissors
            if (OPPONENT[$opponentChoice] === PAPER) $round += 1;  // I chose rock
            if (OPPONENT[$opponentChoice] === SCISSORS) $round += 2;  // I chose paper
            break;
        case DRAW:
            $round += 3;
            if (OPPONENT[$opponentChoice] === ROCK) $round += 1;  // I chose rock
            if (OPPONENT[$opponentChoice] === PAPER) $round += 2;  // I chose paper
            if (OPPONENT[$opponentChoice] === SCISSORS) $round += 3;  // I chose scissors
            break;
        case WIN:
            $round += 6;
            if (OPPONENT[$opponentChoice] === ROCK) $round += 2;  // I chose paper
            if (OPPONENT[$opponentChoice] === PAPER) $round += 3;  // I chose scissors
            if (OPPONENT[$opponentChoice] === SCISSORS) $round += 1;  // I chose rock
            break;
    }

    $score += $round;
}

echo $score . PHP_EOL;
