// Call function when DOM Loaded
document.addEventListener('DOMContentLoaded', () => {
    displaySection();

    // Add get parameters to URL based on click
    document.getElementById('overview-btn').onclick = () => {
        // 'Overview' button clicked
        history.pushState('', '', '?section=overview');
        displaySection();
    };
    document.getElementById('course-btn').onclick = () => {
        // 'Course' button clicked
        history.pushState('', '', '?section=course');
        displaySection();
    };
    document.getElementById('notes-btn').onclick = () => {
        // 'Notes' button clicked
        history.pushState('', '', '?section=notes');
        displaySection();
    };
})

function displaySection() {
    // Get parameters URL
    const url = new URL(window.location.href)
    const param = url.searchParams.get('section');

    var chaptersAvailable = chapters();

    // Display data based on URL get parameters
    if (param === 'course') {
        // Display 'Course' section if requested
        document.getElementById('overview-btn').className = 'btn btn-light';
        document.getElementById('notes-btn').className = 'btn btn-light';
        document.getElementById('course-btn').className = 'btn btn-light active';
        document.getElementById('course-overview').style.display = 'none';
        document.getElementById('course-notes').style.display = 'none';
        if (chaptersAvailable) document.getElementById('course-chapters').style.display = 'block';
    } else if (param === 'notes') {
        // Display 'Notes' section if requested
        document.getElementById('notes-btn').className = 'btn btn-light active';
        document.getElementById('overview-btn').className = 'btn btn-light';
        document.getElementById('course-btn').className = 'btn btn-light';
        document.getElementById('course-overview').style.display = 'none';
        if (chaptersAvailable) document.getElementById('course-chapters').style.display = 'none';
        document.getElementById('course-notes').style.display = 'block';
    } else {
        // Display 'Overview' section by default
        document.getElementById('overview-btn').className = 'btn btn-light active';
        document.getElementById('notes-btn').className = 'btn btn-light';
        document.getElementById('course-btn').className = 'btn btn-light';
        if (chaptersAvailable) document.getElementById('course-chapters').style.display = 'none';
        document.getElementById('course-notes').style.display = 'none';
        document.getElementById('course-overview').style.display = 'block';
    }
};

// Function to check if chapters are available
function chapters() {
    try {
        document.querySelector('#course-chapters').textContent;
        return true;
    } catch (error) {
        return false;
    }
};

// Function to display course videos
function displayVideo() {
    // Get URL parameters
    const url = new URL(window.location.href);
    const c = url.searchParams.get('c');
    const v = url.searchParams.get('v');

    // Get div to append video to
    var div = document.getElementById('js-video');
    
    // Display video based on URL
    if (videoList.filter(x => x.id === `video-c${c}-v${v}`).length === 1) {
        // Display requested video
        div.textContent = '';
        div.append(videoList.find(x => x.id === `video-c${c}-v${v}`));
        $(`#chapter-${c}`).collapse('show');
    } else if (videoList.filter(x => x.id === `video-c1-v1`).length === 1) {
        // Display first video by default
        div.textContent = '';
        div.append(videoList.find(x => x.id === `video-c1-v1`));
        $(`#chapter-1`).collapse('show');
    }
};
