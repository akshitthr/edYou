// Function to display a list of requested courses
function displayData(id) {
    var allData = document.getElementsByClassName('filter-data');
    var filterData = document.getElementsByClassName(`filter-${id}`);
    var btns = document.getElementsByClassName('filter-options');
    var thisBtn = document.getElementById(`btn-${id}`);

    // Hide all data
    for (var i = 0; i < allData.length; i++) {
        allData[i].style.display = 'none';
    }
    // Display requested data
    for (var i = 0; i < filterData.length; i++) {
        filterData[i].style.display = 'block';
    }
    // Remove 'active' from classname of all buttons
    for (var i = 0; i < btns.length; i++) {
        btns[i].className = 'btn btn-light filter-options'
    }

    // Add 'active' to classname of clicked button
    thisBtn.className += ' active'
};

// Function to display all data
function displayAll() {
    var allData = document.getElementsByClassName('filter-data');
    var btns = document.getElementsByClassName('filter-options');

    // Make all data visible
    for (var i = 0; i < allData.length; i++) {
        allData[i].style.display = 'block';
    }
    // Remove 'active' from classname of all buttons
    for (var i = 0; i < btns.length; i++) {
        btns[i].className = 'btn btn-light filter-options'
    }

    // Add 'active' to classname of clicked button
    document.getElementById('btn-all').className += ' active';
};
