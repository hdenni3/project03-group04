// Ensure the DOM is fully loaded before running scripts
document.addEventListener('DOMContentLoaded', function() {
    
    // Handle filter change events
    const filterForm = document.getElementById('filter-form');
    if (filterForm) {
        filterForm.addEventListener('change', function(event) {
            event.preventDefault();
            // Capture the form data
            const formData = new FormData(filterForm);
            const params = new URLSearchParams(formData);
            
            // Fetch data and update visualizations
            fetch(`/update_dashboard?${params.toString()}`)
                .then(response => response.json())
                .then(data => {
                    // Update Plotly charts
                    updateCharts(data);

                    // Update Map
                    updateMap(data);
                })
                .catch(error => console.error('Error fetching data:', error));
        });
    }

    // Function to update Plotly charts with new data
    function updateCharts(data) {
        if (data.plotly_chart1) {
            Plotly.react('chart1', data.plotly_chart1.data, data.plotly_chart1.layout);
        }
        if (data.plotly_chart2) {
            Plotly.react('chart2', data.plotly_chart2.data, data.plotly_chart2.layout);
        }
    }

    // Function to update Leaflet map with new data
    function updateMap(data) {
        if (data.map_markers) {
            const map = L.map('map').setView([data.map_center.lat, data.map_center.lng], data.map_zoom);

            // Clear existing markers
            map.eachLayer(function(layer) {
                if (!!layer.toGeoJSON) {
                    map.removeLayer(layer);
                }
            });

            // Add new markers
            data.map_markers.forEach(markerData => {
                L.marker([markerData.lat, markerData.lng])
                    .addTo(map)
                    .bindPopup(markerData.popupContent);
            });
        }
    }

    // Initialize the map on page load
    if (document.getElementById('map')) {
        const map = L.map('map').setView([0, 0], 2); // Centered at [0, 0] with zoom level 2

        // Add a tile layer to the map
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);
    }

});
