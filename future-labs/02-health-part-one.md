[< Previous Module](../modules/01-introduction.md) | [Home](../README.md) | [Next >](./03-health-part-two.md)

# Lab 2: Maximo Health Score Setup

## Objective
Set up a Health Scoring Group for assets, configure contributors, and activate Health, Criticality, and Risk scores.

---

## Steps:

### **Step 1: Create an Asset**
1. Navigate to **Assets** application.
2. Click **New Asset** and enter:
   - Asset Number: `PUMP-1001`
   - Description: `Water Pump`
   - Location: Create new location if needed (Type = Operating).
3. Add:
   - Priority: `3`
   - Installation Date: `2024-01-15`
   - Expected End of Life: `2030-01-15`
   - Budgeted Cost: `5000`
   - Replacement Cost: `15000`
4. Add an **image** of the asset via **More Actions → Add/Update Image**.
5. Update status to **Operating**.

---

### **Step 2: Add Meters**
1. Navigate to **Meters** tab in the asset.
2. Add:
   - `TEMP-F` (Temperature)
   - `PRESSURE`
   - `OILCOLOR`
3. Enter initial readings via **More Actions → Enter Meter Readings**.

---

### **Step 3: Create Health Scoring Group**
1. Go to **Maximo Health → Score Settings**.
2. Click **Create Scoring Group**.
3. Name: `Pump Health Group`
4. Link to asset query:
   - From Assets app, save current query for PUMP assets.
   - Select that query during group creation.

---

### **Step 4: Define Contributors**
Create the following contributors:
- **MTBF for CM**  
  Formula: `MTBF("CMWO",-1,DURATION(0,13,0,0,0,0),"reportdate","actfinish")/30`
  Best: 100 | Worst: 0
- **Total Cost of CM**  
  Formula: `(CMWO$ACTTOTALCOST)/REPLACECOST`
  Best: 25% | Worst: 100%
- **Pressure Meter**  
  Meter: `PRESSURE` | Limits: 30–60 PSI
- **Oil Color**  
  Formula: Nested IF for values (`CLEAR`, `BROWN`, `LBROWN`, etc.)
- **Temperature**  
  Meter: `TEMP-F` | Limits: 150–200°F

---

### **Step 5: Configure Scores**
1. Add Health Score with two contributor groups:
   - **Maintenance History**:
     - MTBF (50%)
     - Total Cost of CMs (10%)
     - Open CM Work Orders (40%)
   - **Meters**:
     - Motor Temperature (15%)
     - Oil Quality (50%)
     - Pressure (35%)
2. Add contributors for RUL, Criticality, and Risk:
   - Criticality = Priority & Replacement Cost
   - Risk = Health * Criticality

---

### **Step 6: Activate and Calculate Scores**
- Click **Activate** in Health Score settings.
- Validate calculation results on the **Matrix View** dashboard.

---

## Expected Outcome:
- Assets grouped with Health, Criticality, and Risk scores displayed.
- Matrix view shows priority for maintenance based on scores.
