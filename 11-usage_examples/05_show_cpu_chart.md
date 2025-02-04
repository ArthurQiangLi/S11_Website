# Showing CPU line chart

[2025/2/3]

![Alt text](../../90-markdown_media/Screenshot%20from%202025-02-03%2020-09-46.png)

## Data and Control flows

1. You **MUST** include the npm's `chart.js`, otherwise you'll see a hidden error in the browser which could be very hard to debug.
1. The control flow:
   - (1)when frontend html is loaded, it loads the your `script.js` and `chart.js`
   - (2)the setInterval() is called, which cause the..
   - (3)updateCharts() to execute, this function request the `\data` url
   - (4)and the backend server receives the request, data() is called, it collects the backend data, which here is a json package of 'cpu_list' and 'memory_list'
   - (5)backend return the json package to js, js set the data into the chart, which update the frontend.
1. Data flow:
   1. html has the `id="cpuChart"` in the `<canvas>` placeholder.
   2. js get the element by id and store to `cpuCtx`
   3. js creates instance of the chart basing on `cpuCtx` and some style setting, as `cpuChart`
   4. in updatesCharts(), `cpuChart` is used to reflect effects to the element in `<canvas>`

## ** Project File Structure**

```
/flask-system-monitor
│── app.py                 # Flask application (backend)
│── templates/
│   ├── index.html         # HTML template (frontend)
│── static/
│   ├── script.js          # JavaScript for real-time updates
```

---

## **🔹 How It Works**

1. **Backend (`app.py`)**

   - Runs a **Flask server** on port **5000**.
   - Provides an API (`/data`) that returns **real-time CPU & memory usage**.

2. **Frontend (`index.html`)**

   - Uses **Chart.js** to create two **line charts**.

3. **JavaScript (`script.js`)**
   - Fetches data from **Flask every 1000ms**.
   - Updates the **CPU & memory usage charts** dynamically.

## Running effect

![21](../../90-markdown_media/Screenshot%20from%202025-02-03%2019-39-51.png)
