<?php
// Simulasi Expected Value (EV) judi online
// ⚠️ Edukasi, bukan untuk praktik judi

$probWin = 0.49;   // peluang menang
$probLose = 0.51;  // peluang kalah
$payoutWin = 1;    // untung jika menang
$payoutLose = -1;  // rugi jika kalah

$EV = ($probWin * $payoutWin) + ($probLose * $payoutLose);

echo "Expected Value per taruhan: $EV\n";
echo "Artinya: rata-rata rugi " . abs($EV * 100) . "% per taruhan\n";
?>
