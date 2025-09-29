[< Previous](./../modules/09-monitor.md) | [Home](../README.md) | [Next >](./lab9-mobile.md)

# Lab 8: Exploring Maximo Predict – Asset Predictions

## Objective
Access the Maximo Predict application, view predictions such as failure probability and time-to-failure, and explore anomaly detection.

---

## Prerequisites
- Maximo Application Suite with **Predict** deployed and activated.
- Predictive models trained and deployed (built-in or via data science).
- User with access to Maximo Predict/Health application.

---

## Steps

### **1. Launch Maximo Predict**
1. Log in to your MAS environment.
2. Navigate via **Applications** → **Predict** (or, if integrated, via the **Health & Predict** tile) :contentReference[oaicite:9]{index=9}.
3. Confirm access to the **Asset Table View** listing assets with associated prediction scores.

---

### **2. Review Asset Predictions**
1. In the table view, locate columns such as **Failure Probability**, **Days to Failure**, and **Anomaly Score** :contentReference[oaicite:10]{index=10}.
2. Sort or filter to find high-risk assets for further investigation.

---

### **3. Investigate Individual Asset**
1. Select a critical asset from the list.
2. In the asset detail view, explore the **Predictions tab**, which includes:
   - **Failure probability history**
   - **Time to failure curve**
   - **Anomaly score trends**

---

### **4. Visualize Findings**
1. Use available widgets or charts to monitor these prediction metrics.
2. If spatial data is enabled, view asset location via **Map View** for geospatial context :contentReference[oaicite:11]{index=11}.

---

### **5. Take Action**
1. Create a work order or maintenance task directly from the asset details if prediction indicates high failure risk.
2. Document the predicted issue and expected failure timeframe for proactive planning.

---

## Expected Outcome
- Successful launch of Maximo Predict application.
- Visibility into predictive metrics like failure probability and time-to-failure.
- Ability to triage and act on high-risk assets early.

---

### Associated Module:
- [Module 2: Hand'on Lab Health Part Two Module](./../modules/02-health-part-two.md)
