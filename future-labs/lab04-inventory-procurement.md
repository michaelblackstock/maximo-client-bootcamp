[< Previous Module](./../modules/04-inventory-procurement.md) | [Home](../README.md) | [Next >](./lab5-spatial.md)

# Lab 4: Managing Inventory and Procurement

## Objective
Learn how to create an inventory item, add it to a storeroom, issue it to a Work Order, and create a purchase order for an out-of-stock item.

---

## Steps:

### **Step 1: Create a New Inventory Item**
1. Navigate to **Inventory → Item Master**.
2. Click **New Item** and enter:
   - **Item Number**: `ITEM-1001`
   - **Description**: `Cooling Fan`
   - **Commodity Group**: `Electrical`
   - **Issue Unit**: `EA`
3. Save the item.

---

### **Step 2: Add Item to a Storeroom**
1. From the **Item Master**, click **Storerooms** tab.
2. Add:
   - **Storeroom**: `MAIN`
   - **Balance**: `10`
   - **Cost**: `$120`
3. Save.

---

### **Step 3: Issue Item to a Work Order**
1. Go to **Work Order Tracking**.
2. Open `Repair Inverter Overheating` (created in Lab 3).
3. In the **Plans → Materials** tab, add:
   - **Item**: `ITEM-1001`
   - **Quantity**: `1`
4. Approve the Work Order and **Issue the Item**.

---

### **Step 4: Create a Purchase Order**
1. Navigate to **Purchasing → Purchase Orders**.
2. Click **New PO** and enter:
   - **Vendor**: `ELECTRO SUPPLY`
   - **Item**: `ITEM-1001`
   - **Quantity**: `5`
3. Save and **Submit for Approval**.

---

## Expected Outcome:
- Item created and stocked in a storeroom.
- Item issued to a Work Order.
- Purchase Order created for replenishment.

---

### Associated Module:
- [Module 4: Inventory & Procurement](./../modules/04-inventory-procurement.md)
