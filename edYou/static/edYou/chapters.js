// Variables to record editVideo function calls
var vClickCounter = 0;
var vClickId = null;

// Function to display new video form
function newVideo(id) {
    document.getElementById(`form-new-${id}`).style.display = 'block';
};

// Function to display edit video form
function editVideo(id) {
    if (vClickCounter > 0) {
        cancelVideo(vClickId);
    }

    // Register click
    vClickCounter ++;
    vClickId = id;

    // Get video info
    videoName = document.getElementById(`vname-${id}`).value;
    videoBtn = document.getElementById(`btn-${id}`).innerHTML;
    videoURL = document.getElementById(`vurl-${id}`).value;
      
    // Enable editing
    document.getElementById(`btn-${id}`).innerHTML = 'Cancel';
    document.getElementById(`form-${id}`).style.display = 'block';

    // Cancel editing
    document.getElementById(`btn-${id}`).onclick = () => cancelVideo(id);
};

// Function to cancel changes
function cancelVideo(id) {
    document.getElementById(`btn-${id}`).innerHTML = videoBtn;
    document.getElementById(`vname-${id}`).value = videoName;
    document.getElementById(`vurl-${id}`).value = videoURL;
    document.getElementById(`form-${id}`).style.display = 'none';

    // Reset variables
    vClickCounter = 0;
    vClickId = null;
};

// Function to submit delete chapter form
function deleteChapter(id) {
    event.stopPropagation();
    document.getElementById(`ctr-delForm-${id}`).submit();
};

// Function to display edit chapter form
function editChapter(id) {
    event.stopPropagation();
    if (document.getElementById(`ctr-editForm-${id}`).className === 'collapse') {
        $(`#ctr-editForm-${id}`).collapse('show');
        $(`#chapter-${id}`).collapse('hide');
    } else {
        $(`#ctr-editForm-${id}`).collapse('hide');
    }
};
