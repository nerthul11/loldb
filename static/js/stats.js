
    // Load google charts
    function loadCharts() {
        google.charts.load('current', {'packages':['corechart']})
        google.charts.setOnLoadCallback(drawCharts)
    }

    // Draw the chart and set the chart values
    function drawCharts() {
        var gameModes = google.visualization.arrayToDataTable([
        ['Mode', 'Games played'],
        ['Normal', 2],
        ['Ranked', 2],
        ['Flex', 2],
        ['ARAM', 2]
    ]);

        var role = google.visualization.arrayToDataTable([
        ['Role', 'Games played'],
        ['Top', 2],
        ['JG', 2],
        ['Mid', 2],
        ['ADC', 2],
        ['Support', 2],
    ]);

        // Optional; add a title and set the width and height of the chart
        var gameModesTitle = {'title':'Game modes', 'width': 500, 'height': 300};
        var roleTitle = {'title': 'Role distribution', 'width': 500, 'height': 300}

        // Display the chart inside the <div> element with id="piechart"
        var piechart1 = new google.visualization.PieChart(document.getElementById('piechart1'));
        var piechart2 = new google.visualization.PieChart(document.getElementById('piechart2'));
        piechart1.draw(gameModes, gameModesTitle);
        piechart2.draw(role, roleTitle);
    }

    function updateData() {
        // Create AJAX request and define values
        const request = new XMLHttpRequest()
        const filters = {
        "mode": document.querySelector('#mode').value,
        "champ": document.querySelector('#champ').value,
        "gameNumber": document.querySelector('#number').value
        }

        // Callback function for when request completes
        request.onreadystatechange = () => {
            // Extract data
            if (request.readyState == 4 && request.status == 200) {
            const data = JSON.parse(request.responseText)

            // Update HTML
            loadCharts()
            }
        }
        request.open('POST', '/query')
        request.send(JSON.stringify(filters))
    }
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('mode').setAttribute('onchange', 'updateData()')
    document.getElementById('champ').setAttribute('onchange', 'updateData()')
    document.getElementById('number').setAttribute('onchange', 'updateData()')

    updateData()
})