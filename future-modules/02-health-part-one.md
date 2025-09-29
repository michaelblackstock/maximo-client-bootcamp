[< Previous](./01-introduction.md) | [Home](../README.md) | [Next >](./03-health-part-two.md)

# Module 2: Maximo Health

## Overview
Maximo Health is designed to provide a detailed view of the health of your assets and an overall perspective using comparison dashboards. It helps reliability engineers reduce unplanned downtime by combining data from multiple sources such as:
- IoT sensor data
- Work order history
- Manual meter readings
- Remaining Useful Life (RUL)

This creates a **one-stop shop for Reliability Centered Maintenance**.

---

## Business Value
- **Reduce Unplanned Downtime**  
  Avoid expensive failures by monitoring health scores.
- **Optimize Maintenance Practices**  
  Eliminate unnecessary PM tasks and avoid late CM.
- **Enable Condition-Based Maintenance**  
  Use real-time metrics for smarter decisions.

---

## Key Features:
- Health scoring with custom contributors.
- Criticality and Risk scoring alongside health.
- Dashboard visualization of assets by health and risk.
- Integration with Maximo Manage and Monitor.

---

## Personas:
- **Reliability Engineer**: Reviews asset health, prioritizes work.
- **Maintenance Manager**: Assigns work based on risk.
- **Technician**: Performs work, updates meters, captures failure codes.

---

## Setup Steps:
1. **Access MAS Suite Administration**
   - Use OpenShift → Networking → Routes → `{instanceid}-admin`.
   - Login with Super User credentials from MAS secrets.

2. **Create Admin Users**
   - Navigate to **Users** app.
   - Update `MAXADMIN` email and reset password.
   - Create a personal admin user with **Premium Application and Admin entitlements**.
   - Add the user to the `MAXADMIN` security group.

3. **Configure System Properties**
   - `mxe.oslc.webappurl` → Maximo Manage URL
   - `mxe.externaleam.url` → Manage URL + `/maximo`
   - `mxe.externaleam.apikey` → API key from **API Keys** app
   - Perform **Live Refresh** after changes.

4. **Disable GL Validations**
   - Navigate to **Chart of Accounts** → Validation Options → **Deactivate GL Validations**.

---

## Hands-On Activities:
- Create an **Asset Record** with location, meters, and costs.
- Build **Meter Groups** with Pressure, Temperature, and Oil Quality.
- Create **Health Scoring Group** and link assets.
- Define **Contributors** (e.g., MTBF, Maintenance Cost Ratio, Pressure, Oil Color).
- Configure **Health, Criticality, Risk Scores** with weights.
- Activate and calculate scores.
- Create **Health Dashboard** with Matrix View and custom filters.

---

### Associated Lab:
- [Lab 2: Maximo Health Score Setup](../labs/02-health-part-one.md)