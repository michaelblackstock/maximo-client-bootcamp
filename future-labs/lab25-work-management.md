[< Previous Module](./../modules/05-work-management.md) | [Home](../README.md) | [Next >](./lab26-inventory-procurement.md)


# Lab 3: Creating and Managing Work Orders

## Objective
Learn how to create a Work Order (WO) for asset maintenance, add tasks, and assign resources.

---

## Steps:

### **Step 1: Open Work Order Tracking**
1. Log in to **Maximo Application Suite**.
2. From the navigation menu, select:
   **Applications → Work Order Tracking**.

---

### **Step 2: Create a New Work Order**
1. Click **New Work Order**.
2. Enter:
   - **Description**: `Repair Inverter Overheating`
   - **Asset**: `ASSET-1001` (created in Lab 2)
   - **Location**: `Plant A`
   - **Priority**: `1 (High)`
3. Save the work order.

---

### **Step 3: Add Tasks**
1. Go to the **Tasks** tab.
2. Add:
   - **Task 1**: `Inspect cooling fan`
   - **Task 2**: `Replace thermal pads`
   - **Task 3**: `Run temperature calibration`
3. Save changes.

---

### **Step 4: Assign Labor**
1. Open the **Plans → Labor** tab.
2. Assign:
   - **Labor Code**: `TECH-01`
   - **Craft**: `Electrical`
3. Save.

---

### **Step 5: Update Status**
1. In the **Workflow toolbar**, update:
   - **WAPPR → APPR → INPRG → COMP**.
2. Add completion notes: `Cooling system repaired successfully`.

---

## Expected Outcome:
- A Work Order created, assigned, and updated through the full lifecycle.
- Tasks and labor recorded for historical tracking.

---

### Associated Module:
- [Module 5: Work Management](./../modules/05-work-management.md)