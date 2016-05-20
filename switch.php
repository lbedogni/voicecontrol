<?php

//to keep it simple using require
require 'Milight.php';

$action = $argv[1];
$location = $argv[2];

$milight = new Milight('192.168.1.150');

if ($action == "on") {
    if ($location == 0) {
        $milight->rgbwAllOn();
    } else if ($location == 1) {
        $milight->rgbwGroup1On();
    } else if ($location == 2) {
        $milight->rgbwGroup2On();
    } else if ($location == 3) {
        $milight->rgbwGroup3On();
    } else if ($location == 4) {
        $milight->rgbwGroup4On();
    }
} else {
    if ($location == 0) {
        $milight->rgbwAllOff();
    } else if ($location == 1) {
        $milight->rgbwGroup1Off();
    } else if ($location == 2) {
        $milight->rgbwGroup2Off();
    } else if ($location == 3) {
        $milight->rgbwGroup3Off();
    } else if ($location == 4) {
        $milight->rgbwGroup4Off();
    }
}
?>
