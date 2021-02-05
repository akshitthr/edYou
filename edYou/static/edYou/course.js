// Call edit_course function when DOM Loaded
document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('course-btn').innerText === 'Edit') {
        document.querySelector('#edit-form').style.display = 'none';
        document.getElementById('course-btn').addEventListener('click', () => edit_course());
    }
})

// Function to display edit_course form
function edit_course() {
    // Hide course content, edit button and display edit form
    document.querySelector('#course').style.display = 'none';
    document.querySelector('#course-btn').style.display = 'none'
    document.querySelector('#edit-form').style.display = 'block';

    // Fill the form with existing values
    document.getElementById('id_name').value = document.getElementById('course-name').innerText;
    document.getElementById('id_subject').value = document.getElementById('course-sub').innerText.slice(9);
    document.getElementById('id_language').value = document.getElementById('course-lang').innerText.slice(17);
    document.getElementById('id_difficulty').value = document.getElementById('course-dif').innerText.slice(12);
    document.getElementById('id_duration').value = document.getElementById('course-dur').innerText.slice(10);
    document.getElementById('id_description').value = document.getElementById('course-desc').innerText.slice(13);
}
