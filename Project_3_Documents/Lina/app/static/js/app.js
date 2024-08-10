document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('data-dropdown').addEventListener('change', updateVisualization);
  updateVisualization(); // Initial call
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
