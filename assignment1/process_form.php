<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $firstname = $_POST["firstname"];
    $lastname = $_POST["lastname"];
    $gender = $_POST["gender"];
    $dob = $_POST["dob"];
    $emailaddress = $_POST["emailaddress"];
    $educationlevel = $_POST["educationlevel"];
    $country = $_POST["country"];
    $employmentstatus = $_POST["employmentstatus"];
    $phonenumber = $_POST["phonenumber"];
    $chooseschool = $_POST["chooseschool"];
    $courseofstudy = $_POST["courseofstudy"];
    $refer = $_POST["refer"];
    $discount = $_POST["discount"];

    $formData = "First Name: " . $firstname . "\n" .
    "Last Name: " . $lastname . "\n" .
    "Gender: " . $gender . "\n" .
    "Date of Birth: " . $dob . "\n" .
    "Email Address: " . $emailaddress . "\n" .
    "Education Level: " . $educationlevel . "\n" .
    "Country: " . $country . "\n" .
    "Employment Status: " . $employmentstatus . "\n" .
    "Phone Number: " . $phonenumber . "\n" .
    "Choose School: " . $chooseschool . "\n" .
    "Course of Study: " . $courseofstudy . "\n" .
    "How did you hear about us: " . $refer . "\n" .
    "Scholarship/Discount Code: " . $discount;

    $file = fopen("form_data.txt", "a");
    fwrite($file, $form_data);
    fclose($file);
}
?>
