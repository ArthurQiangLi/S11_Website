const cpuCtx = document.getElementById("cpuChart").getContext("2d");
const combinedCtx = document.getElementById("combinedChart").getContext("2d");

const cpuChart = new Chart(cpuCtx, {
  type: "line",
  data: {
    labels: [],
    datasets: [
      {
        label: "CPU Usage (%)",
        borderColor: "red",
        borderWidth: 2,
        fill: false,
        data: [],
      },
    ],
  },
  options: {
    responsive: true,
    scales: {
      x: { display: true },
      y: { beginAtZero: true, max: 100 },
    },
  },
});

const combinedChart = new Chart(combinedCtx, {
  type: "line",
  data: {
    labels: [],
    datasets: [
      {
        label: "CPU Usage (%)",
        borderColor: "red",
        borderWidth: 2,
        fill: false,
        data: [],
      },
      {
        label: "Memory Usage (%)",
        borderColor: "blue",
        borderWidth: 2,
        fill: false,
        data: [],
      },
    ],
  },
  options: {
    responsive: true,
    scales: {
      x: { display: true },
      y: { beginAtZero: true, max: 100 },
    },
  },
});

function updateCharts() {
  fetch("/data")
    .then((response) => response.json())
    .then((data) => {
      // CPU Chart: Update last 30 values
      cpuChart.data.labels = data.cpu.map((d) => d.time);
      cpuChart.data.datasets[0].data = data.cpu.map((d) => d.cpu);
      cpuChart.update('none');

      // Combined Chart: Add both datasets
      combinedChart.data.labels = data.cpu.map((d) => d.time);
      combinedChart.data.datasets[0].data = data.cpu.map((d) => d.cpu);
      combinedChart.data.datasets[1].data = data.memory.map((d) => d.memory);
      combinedChart.update();
    });
}

// Update charts every second
setInterval(updateCharts, 1000);
