// Call function when DOM Loaded
document.addEventListener('DOMContentLoaded', () => {
    displayData()

    // Add get parameters to URL based on click
    document.getElementById('user-courses-btn').onclick = () => {
        // 'My Courses' button clicked
        history.pushState('', '', '?courses=mycourses');
        displayData()
    };
    document.getElementById('enrolled-courses-btn').onclick = () => {
        // 'Enrolled Courses' button clicked
        history.pushState('', '', '?courses=enrolled');
        displayData()
    };
})

// Function to display data on click
function displayData() {
    // Get URL
    const url = new URL(window.location.href);

    // Display data based on URL get parameters
    if (url.searchParams.get('courses') === 'enrolled') {
        // Display 'Enrolled Courses' section if requested
        document.getElementById('enrolled-courses-btn').className = 'btn btn-light active';
        document.getElementById('user-courses-btn').className = 'btn btn-light';
        document.getElementById('user-courses').style.display = 'none';
        document.getElementById('enrolled-courses').style.display = 'block';
    } else {
        // Display 'My Courses' section by default
        document.getElementById('user-courses-btn').className = 'btn btn-light active';
        document.getElementById('enrolled-courses-btn').className = 'btn btn-light';
        document.getElementById('enrolled-courses').style.display = 'none';
        document.getElementById('user-courses').style.display = 'block';
    }
};
