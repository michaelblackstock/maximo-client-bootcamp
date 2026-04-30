[Previous](lab9-02-space-management.md) | [Next](lab9-04-capital-projects.md) | [Home](../README.md)

# Lease Management
To improve the efficiency of updates, queries, and reporting, MREF allows lease data to be digitally stored as structured lease records. Real estate lease records can be created either through manual data entry or by approving and completing lease abstract records,
while asset lease records are created exclusively through manual entry.

**Lease Creation**: When lease records are entered and stored, they are presented in dedicated lease forms organized into multiple tabs. The system provides separate forms for Real Estate Leases and Asset Leases, with key sections such as Clauses, Options and Terms, and Accounting to capture all relevant contractual and financial details.

**Lease Accounting**: IBM TRIRIGA Real Estate Manager simplifies and standardizes lease accounting by incorporating processes that comply with major accounting standards-ASC 842, IFRS 16, GASB 87 (Lessee and Lessor), GASB 96 for Subscription-Based IT Arrangements (SBITA)—as well as legacy standards such as ASC 840 and IAS 17.

**Lease Accounting Concepts**: The Accounting tab within each lease form enables users to define essential financial parameters in accordance with the relevant standards set by FASB, IASB, and GASB. Users can enter details such as the borrowing rate, rent component assumptions, growth expectations, and the likely term of the lease. Based on this information, the system automatically determines the appropriate lease
classification. This functionality is accessible only to users with the Lease Accountant role and a Real Estate Manager license. 

## Exercise 1: Creating a Lease Abstract
1. Login to Maximo Application Suite and Launch Real Estate and Facilities as Lease Administrator

* Username: **lleases**
* Password: **xxxxxxxx**

2. Go to Contracts -> Leases.

![Leases](/labs/images/lease_management/ex1-step2.png)

3. Expand Related Links – Contracts and click on **New Lease Abstract**.
![New Lease Abstract](/labs/images/lease_management/ex1-step3.png)

4. Click on **Create Draft**
![New Lease Abstract](/labs/images/lease_management/ex1-step4.png)

5. Fill the below under the **Document Type** and General details of Lease Abstract.
![General details](/labs/images/lease_management/general-lease-info.png)

6. Click on **Save and Close** on the upper right corner.

7. Open the Lease Abstract that you created from **Work In Progress Lease Abstracts**.
![Lease Abstract](/labs/images/lease_management/ex1-step7.png)

8. In the **Primary Address** section, click the magnifying glass icon for the Location Lookup field and select this location from the list.
![Primary Address](/labs/images/lease_management/ex1-step8.png)

9. In the **Details** section, fill these below lease related details.
![Details](/labs/images/lease_management/ex1-step9.png)

10. In the **Critical Dates** section, enter the first day of the current month in the **Commencement Date** field, and enter the last day of the month exactly 12 months from today in the **Base Lease Expiration Date** field.
![Critical Dates](/labs/images/lease_management/ex1-step10.png)

11. In the **Management Company** section, click the magnifying glass icon for the Management Organization Lookup field and select from the list.
![Management Company](/labs/images/lease_management/ex1-step11.png)

12. In the **Default Remit To** section, click the magnifying glass icon for the Remit To Lookup field and select from the list.
![Default Remit To](/labs/images/lease_management/ex1-step12.png)

13.  Open the **Tax** Tab and enter:
* Tax Type: Sales Tax
* Tax Rate %: 3
![Tax tab](/labs/images/lease_management/ex1-step13.png)

14. Click on **Save -> Activate**.

15. Open the Lease Abstract and **Complete** it.
![Lease Abstract](/labs/images/lease_management/ex1-step15.png)

## Exercise 2: Creating a Lease

1. Login to Maximo Application Suite and Launch Real Estate and Facilities as lease manager

* Username: **lleases**
* Password: **xxxxxxxx**

2. In the related links section, expand RE Contracts and click on **Leases**.
![Leases](/labs/images/lease_management/ex2-step2.png)

3. Click on **Add**
![Add](/labs/images/lease_management/ex2-step3.png)

4. Fill the General details for the lease.
![General details](/labs/images/lease_management/ex2-step4.png)

5. In the Contact Details tab, Contacts section, click on **Contract Administrator** -> **Find** -> Select the person -> Click the **OK** action.
![Contract administrator](/labs/images/lease_management/contacts.png)

6. Click on **Create Draft**

7. Go to Payments tab and click on **Generate Payment Schedules**.
![Payment Schedules](/labs/images/lease_management/ex2-step7.png)

8. Fill the below details for generating the payment schedule.
![Fill in details](/labs/images/lease_management/payment-schedule.png)

9. Click on **Add** in the Payment Instruction section and add a Remit to Organization
![Additional Details](/labs/images/lease_management/remit-to-organization.png)

10. Click on **Create Schedule -> Save and Close**.

11. Submit the Lease for Accounting in Review.
![Submit](/labs/images/lease_management/ex2-step10.png)

**End of lab**

References: 