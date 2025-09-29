[< Previous Module](./../modules/09-monitor.md) | [< Previous](./lab5-spatial.md) | [Home](../README.md) | [Next >](./lab7-health.md)

# Lab 6: Maximo Monitor Dashboard Creation

## Objective
Create a real-time monitoring dashboard in Maximo Monitor, connect to a data source, and configure alerts for anomaly detection.

---

## Prerequisites
- Access to **Maximo Application Suite** with **Monitor** enabled.
- An IoT device or **simulated data source**.
- Appropriate user role permissions for dashboard creation.

---

## Steps:

### **Step 1: Access Maximo Monitor**
1. Log in to **Maximo Application Suite**.
2. From the main menu, select **Monitor**.
3. The **Monitor Home** page displays an overview of connected devices and existing dashboards.

---

### **Step 2: Connect a Data Source**
1. Navigate to **Device Connections** → **Add Device**.
2. Choose **Simulated Device** (or select an existing device if available).
3. Enter:
   - **Device Name**: `Simulated Energy Device`
   - **Data Streams**: Temperature, Voltage, Energy Output
4. Click **Create** and confirm the data feed starts streaming.
5. Verify data points are updating in the **Device Details** view.

---

### **Step 3: Create a Custom Dashboard**
1. Go to **Dashboards** → **Create New Dashboard**.
2. Enter:
   - **Dashboard Name**: `Energy Monitoring Dashboard`
   - **Description**: `Tracks energy performance, temperature, and alerts.`
3. Click **Save** to create an empty dashboard canvas.

---

### **Step 4: Add Widgets to Visualize Data**
1. From the dashboard editor, click **Add Widget**.
2. Select and configure:
   - **Time Series Graph** → Bind to `Energy Output`.
   - **Gauge** → Bind to `Temperature`.
   - **Alert Summary Card** → Displays current alerts.
3. Arrange widgets for an easy-to-read layout.
4. Click **Save Layout** when done.

---

### **Step 5: Configure an Alert for Anomalies**
1. Navigate to **Alerts** → **Create Alert Rule**.
2. Define:
   - **Stream**: `Temperature`
   - **Condition**: `Greater than 85°C`
   - **Severity**: Critical
3. Set **Notification** method (e.g., email or in-app).
4. Click **Submit** to activate the alert.

---

### **Step 6: Validate Real-Time Monitoring**
1. Return to the dashboard.
2. Simulate a temperature spike by adjusting the simulated device value.
3. Verify:
   - Alert triggers and appears on the **Alert Summary Card**.
   - Event logs display the anomaly with timestamp.
4. Add a comment to the event log for traceability.

---

## Expected Outcome
- A custom dashboard with widgets showing **energy output**, **temperature**, and **active alerts**.
- An active alert rule that detects temperature anomalies in real time.

---

### Associated Module:
- [Module 7: Maximo Monitor](./../modules/07-monitor.md)
