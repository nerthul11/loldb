
    // Load google charts
    function loadCharts() {
        google.charts.load('current', {'packages':['corechart']})
        google.charts.setOnLoadCallback(drawCharts)
    }

    // Draw the chart and set the chart values
    function drawCharts() {

        var gameModes = google.visualization.arrayToDataTable([
        ['Mode', 'Games played'],
        ['Normal', parseInt(document.getElementById('normal').innerHTML)],
        ['Ranked', parseInt(document.getElementById('ranked').innerHTML)],
        ['Flex', parseInt(document.getElementById('flex').innerHTML)],
        ['ARAM', parseInt(document.getElementById('aram').innerHTML)]
    ]);

        var role = google.visualization.arrayToDataTable([
        ['Role', 'Games played'],
        ['Top', parseInt(document.getElementById('top').innerHTML)],
        ['JG', parseInt(document.getElementById('jg').innerHTML)],
        ['Mid', parseInt(document.getElementById('mid').innerHTML)],
        ['ADC', parseInt(document.getElementById('adc').innerHTML)],
        ['Support', parseInt(document.getElementById('sup').innerHTML)],
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
        const request = new XMLHttpRequest(),
        filters = {
        "game_mode": document.querySelector('#mode').value != '' ? document.querySelector('#mode').value : null,
        "champ": document.querySelector('#champ').value != '' ? document.querySelector('#champ').value : null,
        "role": document.querySelector('#role').value != '' ? document.querySelector('#role').value : null,
        "gameNumber": document.querySelector('#number').value
        }

        // Callback function for when request completes
        request.onreadystatechange = () => {
            // Extract data
            if (request.readyState == 4 && request.status == 200) {
            const data = JSON.parse(request.responseText)

            // Update HTML
            if (data.success === true) {
                document.getElementById('normal').innerHTML = data.gameModes.normal
                document.getElementById('ranked').innerHTML = data.gameModes.ranked
                document.getElementById('flex').innerHTML = data.gameModes.flex
                document.getElementById('aram').innerHTML = data.gameModes.aram
                document.getElementById('top').innerHTML = data.roles.top
                document.getElementById('jg').innerHTML = data.roles.jg
                document.getElementById('mid').innerHTML = data.roles.mid
                document.getElementById('adc').innerHTML = data.roles.adc
                document.getElementById('sup').innerHTML = data.roles.sup
                document.getElementById('games').innerHTML = data.gamesPlayed
                document.getElementById('winrate').innerHTML = data.winrate
                document.getElementById('kda').innerHTML = data.kda
                document.getElementById('csm').innerHTML = data.csm
                document.getElementById('gpm').innerHTML = data.gpm
                document.getElementById('duration').innerHTML = data.averageDuration
                document.getElementById('vision').innerHTML = data.vision
                loadCharts()
            }
            else {
                console.log("No games found")
            }
            }
        }
        request.open('POST', '/query')
        request.send(JSON.stringify(filters))
    }
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('mode').setAttribute('onchange', 'updateData()')
    document.getElementById('champ').setAttribute('onchange', 'updateData()')
    document.getElementById('role').setAttribute('onchange', 'updateData()')
    document.getElementById('number').setAttribute('onchange', 'updateData()')
    updateData()
})