document.addEventListener('DOMContentLoaded', () => {
  // Initialize dropdown event listeners
  const dataDropdown = document.getElementById('data-dropdown');
  const countryDropdown = document.getElementById('countryDropdown');

  if (dataDropdown) {
    dataDropdown.addEventListener('change', updateVisualization);
    updateVisualization(); // Initial call to populate the visualization
  }

  if (countryDropdown) {
    countryDropdown.addEventListener('change', updateTable);
    updateTable(); // Initial call to populate the table
  }
});

async function updateVisualization() {
  const selectedValue = document.getElementById('data-dropdown').value;

  try {
    const response = await fetch(`/data?param=${selectedValue}`);
    const data = await response.json();
    createPlot(data);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

function createPlot(data) {
  const xData = data.map(item => item.title);
  const yData = data.map(item => item.video_views);

  const trace = {
    x: xData,
    y: yData,
    type: 'bar',
    text: yData.map(String),
    textposition: 'auto'
  };

  const layout = {
    title: 'YouTube Channel Metrics',
    xaxis: { title: 'Channel Titles' },
    yaxis: { title: 'Video Views' },
    margin: { t: 50, b: 100 }
  };

  Plotly.newPlot('chart', [trace], layout);
}

function make_table(filtered_data) {
  // Select the table body
  const countryTableBody = document.querySelector('#countryTable tbody');
  countryTableBody.innerHTML = ''; // Clear existing rows

  // Iterate over filtered data to build table rows
  filtered_data.forEach(channel => {
    const row = `
      <tr>
        <td>${channel.rank}</td>
        <td>${channel.youtuber}</td>
        <td>${channel.subscribers}</td>
        <td>${channel.country}</td>
        <td>${channel.channel_type}</td>
        <td>${channel.category}</td>
      </tr>`;
    countryTableBody.insertAdjacentHTML('beforeend', row);
  });
}

function updateTable() {
  const selectedCountry = document.getElementById('countryDropdown').value;
  const countryData = JSON.parse(document.getElementById('countryData').textContent);

  // Filter data based on the selected country
  const filteredData = countryData.filter(channel => channel.country === selectedCountry || selectedCountry === '');

  // Call the function to build and populate the table
  make_table(filteredData);
}
