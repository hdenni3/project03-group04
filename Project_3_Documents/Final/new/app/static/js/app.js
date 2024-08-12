document.addEventListener("DOMContentLoaded", () => {
  createPlot("top-channels", top_channels);
  createPlot("top-channels-by-country", top_channels_by_country);

  // Initialize dropdown event listeners
  const countryDropdown = document.getElementById("countryDropdown");

  if (countryDropdown) {
    countryDropdown.addEventListener("change", async function (e) {
      const { value } = e.currentTarget;
      const response = await fetch(`/api/v1.0/get_data/${value}`);
      const top_channels_by_country = await response.json();
      createPlot("top-channels-by-country", top_channels_by_country);
      const tbody = document.querySelector(
        "#top-channels-by-country-table tbody"
      );
      const innerHTML = [];
      for (const row of top_channels_by_country) {
        innerHTML.push(`
          <tr>
              <td>${row.youtuber}</td>
              <td>${Math.round(row.subscribers / 1000000)}M</td>
              <td>${row.country}</td>
              <td>${row.channel_type}</td>
              <td>${row.category}</td>
              <td>${Math.round(row.video_views / 1000000)}M</td>
          </tr>
        `);
      }
      tbody.innerHTML = innerHTML.join("");
    });
  }
});

function createPlot(target, data) {
  const xData = [];
  const yData = [];

  // Function to truncate labels
  function truncateLabel(label, maxLength) {
    return label.length > maxLength
      ? label.substring(0, maxLength) + "..."
      : label;
  }

  data.forEach(({ youtuber, subscribers }, index) => {
    xData.unshift(subscribers);
    yData.unshift(truncateLabel(`${index + 1}) ${youtuber}`, 20));
  });

  Plotly.newPlot(
    target,
    [
      {
        type: "bar",
        x: xData,
        y: yData,
        orientation: "h",
      },
    ],
    {
      margin: {
        l: 200, // Adjust the left margin to make room for the labels
        r: 20,
        t: 20,
        b: 20,
        pad: 8,
      },
      xaxis: {
        title: "Values",
        showgrid: false, // Remove grid lines
        zeroline: false, // Remove zero line
      },
      yaxis: {
        automargin: true, // Ensure the y-axis labels have enough space
        showgrid: false, // Remove grid lines
        zeroline: false, // Remove zero line
        tickfont: {
          color: "white", // Set the color of the labels to white
        },
      },
      paper_bgcolor: "rgba(0,0,0,0)", // Transparent background for the entire chart
      plot_bgcolor: "rgba(0,0,0,0)", // Transparent background for the plot area
    }
  );
}
