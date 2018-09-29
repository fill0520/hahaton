<?php

require "request.php";





$us = file_get_contents('http://104.233.107.149/hahaton/per.json');
$tar = file_get_contents('http://104.233.107.149/hahaton/tarif.json');

$user =  json_decode($us, true);
$tarif = json_decode($tar, true);
$o_number = array("0500", "0501", "0502", "0505", "0507","0700", "0702", "0703", "0704", "0705", "0707", "0708", "0709");

for ($k = 0; $k < 13; $k++) {

//-----INFO
$requires = intval($tarif[$k]['Info']['Requires']); // check activity 0 - No, 1 - Yes
$payday = intval($tarif[$k]['Info']['PaymentDay']);
$reset= intval($tarif[$k]['Info']['Reset']);

//----------

//-----Call
$freecall = intval($tarif[$k]['Call']['Free']);
$free_nightcall = intval($tarif[$k]['Call']['Free1']);
$free_daycall = intval($tarif[$k]['Call']['Free2']);
$freeoutcall = intval($tarif[$k]['Call']['FreeOut']);
$costcall = intval($tarif[$k]['Call']['Cost']);
$cost_outcall = intval($tarif[$k]['Call']['CostOut']); 
//---------


//------Internet
$freeinternet = intval($tarif[$k]['Internet']['Free']);
$costinternet = intval($tarif[$k]['Internet']['Cost']);
//--------------



//----------SMS
$freesms = intval($tarif[$k]['SMS']['Free']);
$free_nightsms = intval($tarif[$k]['SMS']['Free1']);
$free_daysms = intval($tarif[$k]['SMS']['Free2']);
$freeoutsms = intval($tarif[$k]['SMS']['FreeOut']);
$costsms = intval($tarif[$k]['SMS']['Cost']);
//-------------


//-----------Call/SMS/Internet

$main_summary = 0;
$call_sum = 0;
$sms_sum = 0;
$internet_sum = 0;


//----Call
$call_day_in = 0;
$call_day_out = 0;
$call_night_in = 0;
$call_night_out = 0;
//--------

//-----Internet
$mb_cnt = 0;
//------------

//-------SMS
$sms_day_out = 0;
$sms_night_out = 0;
$sms_day_in = 0;
$sms_night_in = 0;
//----------


//----------------------------




$fl = 0;
if ($requires == 0) {
  $main_summary = 1;
  $main_summary *= $payday;
}
else $fl = 1;


for ($i = 0; $i < 30; $i++) {
  $sum_mb = 0;

  //----------------PERSON


//-----Call
$timecall = $user[$i]['Call']['Time'];
$numbcall = $user[$i]['Call']['NumberTo'];
$dialtimecall = intval($user[$i]['Call']['DialingTime']);
//---------


//-----Internet
$mb = intval($user[$i]['Internet']['Megabytes']);
$timeinternet = $user[$i]['Internet']['Time'];
//-------------


//----------SMS
$msg_cnt = intval($user[$i]['SMS']['MessageCount']);
$numbsms = $user[$i]['SMS']['NumberTo'];
$timesms = $user[$i]['SMS']['Time'];
//-------------


//----------------------CALL

$timecall = intval(substr($timecall, 0, 2));
$numbcall = intval(substr($numbcall, 0, 4));
if ($timecall >= 17 && $timecall<=23) {
  if (in_array($numbcall, $o_number)) {
    $call_night_in += $dialtimecall;
  }
  else $call_night_out += $dialtimecall;
}
else {
  if (in_array($numbcall, $o_number)) {
    $call_day_in += $dialtimecall;
  }
  else {
    $call_day_out += $dialtimecall;
  }
}


$sum_mb += $mb;

//------------------------


//--------------------------SMS
$timesms = intval(substr($timesms, 0, 2));
$numbsms = intval(substr($numbsms, 0, 4));
if ($timesms >= 17 && $timesms<=23) {
  if (in_array($numbsms, $o_number)) {
    $sms_night_in += $msg_cnt;
  }
  else $sms_night_out += $msg_cnt;
}
else {
  if (in_array($numbsms, $o_number)) {
    $sms_day_in += $msg_cnt;
  }
  else {
    $sms_day_out += $msg_cnt;
  }
}
$sms_out = $sms_day_out + $sms_night_out - $freeoutsms;
if ($sms_out < 0) $sms_sum += 0;
else $sms_sum + $sms_out*$costsms;




//-----------------------------



if (($call_day_in == 0 || $call_day_out == 0 || $call_night_in == 0 || $call_night_out == 0) && $requires == 1) $main_summary += 0;
else $main_summary += $payday;




if ($i+1 == $reset && $reset != 0) {
//----------------------------------------------------------------------------CALL
if ((($call_night_out + $call_day_out) - $freeoutcall) < 0) $call_sum += 0;
else $call_sum += (($call_night_out + $call_day_out) - $freeoutcall)*$cost_outcall;

$cs1 = $call_night_in - $free_nightcall;
if ($cs1 < 0) $cs1 = 0;

$cs2 = $call_day_in - $free_daycall;
if ($cs2 < 0) $cs2 = 0;

$call_sum += ($cs1+$cs2)*$costcall;
//---------------------------------------------------------------------------------


  //----Call
$call_day_in = 0;
$call_day_out = 0;
$call_night_in = 0;
$call_night_out = 0;
//--------

//-----Internet
$mb_cnt = 0;
//------------

//-------SMS
$sms_day = 0;
$sms_night = 0;
//----------
  }

}
$internet_sum += $sum_mb*$costinternet;




}
?>
