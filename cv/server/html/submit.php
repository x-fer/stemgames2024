<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Check if all fields are filled
    if (!empty($_POST['name']) && !empty($_POST['surname']) && !empty($_POST['email']) && !empty($_FILES['cv']['name'])) {
        // Retrieve form data
        $name = $_POST['name'];
        $surname = $_POST['surname'];
        $email = $_POST['email'];
	
	if ($_FILES['cv']['size'] > (1024*100)){
		die("File size limit is 100KB");
	}
        // Check if the file is uploaded without errors
        if ($_FILES['cv']['error'] == UPLOAD_ERR_OK) {
            // Specify the upload directory
            $upload_dir = '/var/www/html/uploads/';

            // Generate a unique filename
            $filename = uniqid('cv_') . '_' . basename($_FILES['cv']['name']);

            // Move the uploaded file to the upload directory
            if (move_uploaded_file($_FILES['cv']['tmp_name'], $upload_dir . $filename)) {
                // File uploaded successfully
                echo "CV uploaded successfully at /uploads/".$filename;
		echo "<script>location.href=\"index.html\"</script>";

            } else {
                // Error while moving file
                echo "Sorry, there was an error uploading your CV.";
            }
        } else {
            // File upload error
            echo "Sorry, there was an error uploading your CV.";
        }
    } else {
        // Missing fields error
        echo "Please fill out all fields.";
    }
}
?>

