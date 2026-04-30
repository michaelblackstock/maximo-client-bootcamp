[Next](lab9-02-space-management.md) | [Home](../README.md)

# Portfolio Management

Portfolio data forms the foundation for managing workplaces. It includes key information about the organizations, locations, people, and assets connected to the spaces you oversee. In MREF, portfolio data records help you maintain the details needed to perform tasks across other applications. For instance, when planning space allocations or
relocating personnel, you rely on accurate and comprehensive data about the relevant spaces and individuals. These portfolio data records are structured hierarchically and can be linked to other records. Each record’s lifecycle events can be tracked, providing a complete history and audit trail. Real Estate Environmental Sustainability extends portfolio management by adding sections and features related to business objects such as My Company, Building, Land, Structure, and Retail Location.

All records in the Portfolio Data Manager follow the same set of states and actions. States are the major steps in the lifecycle of the record and the actions trigger state changes.
![Records](/labs/images/portfolio_management/ex0.png)

## Exercise 1. Creating a Location in Real Estate & Facilities

1. Login to Real Estate and Facilities application with your id:
* Username- xxLastName - Where xx represents your initals and LastName is your last name
* Password- xxxxxxxxxx

2. Click on the hamburger menu and open **Locations** under Portfolio module.

![Locations](/labs/images/portfolio_management/ex2-step2.png)

3. This interface serves as a location management dashboard designed to categorize and manage various types of real estate assets and facilities within an organization's portfolio.
![Dashboard](/labs/images/portfolio_management/ex2-step3.png)

**Note**: The hierarchical structure enables eeicient organization, navigation, and access to location data across categories such as Offices, Campuses, Healthcare, and other key asset types.

4. Select **Locations** from the Hierarchy and then click on **New**. Select **Location Category** from the List.
![Location Category](/labs/images/portfolio_management/ex2-step4.png)

5. Fill the General details for the location category and then **Create Draft -> Save -> Activate**.
* ID: XX-DEMO-OFC (Replace XX with your initials)
* Name: Demo Offices
![General details](/labs/images/portfolio_management/ex2-step5.png)

6. Similarly Click on **Demo Offices** and then Click on **New** and Select **Location Category** from the list.
![Demo offices](/labs/images/portfolio_management/ex2-step6.png)

7. Fill the General details for the location category and then **Create Draft -> Save -> Activate**.
* ID: XX- NA-OFC
* Name: North America
![General details](/labs/images/portfolio_management/ex2-step7.png)

8. Click on **North America** and then Click on **New** and **Select Building** from the list.
![North America Building](/labs/images/portfolio_management/ex2-step8.png)

9. Fill all the building related general details as provided in the screenshot and then click on **Create Draft -> Save -> Activate**.
* ID: XX-NA004
* Name: Charlotte Watson Center
![General details](/labs/images/portfolio_management/ex2-step9-1.png)
![General details](/labs/images/portfolio_management/ex2-step9-2.png)

10. Click on **Charlotte Watson Center** and then Click on **New** and Select **Floor** from the list.
![New floor](/labs/images/portfolio_management/ex2-step10.png)

11. Fill all general details for the First Floor of the building as provided in the screenshot and then click on Create Draft -> Save -> Activate.
* ID: XX-NA004-01
* Name: 01-First Floor
![First floor](/labs/images/portfolio_management/ex2-step11.png)

12. Click on **01 – First Floor** and then Click on **New** and **Select Space** from the list.
![New space](/labs/images/portfolio_management/ex2-step12.png)

13.  Complete all the space details in the General tab as shown in the screenshot. Once finished, click on **Create Draft**.
* ID: **XX-01-A020**
* Name: **01-A020**
![Create draft](/labs/images/portfolio_management/new-space.png)

14. You will be redirected to the **Reserve** tab of the space. Enter the reservation details as shown in the screenshot.
![Reserve](/labs/images/portfolio_management/reserve-tab.png)

15. After filling in all the details, click on **Create Draft**. An attention message will then appear on the screen.
![Create Draft](/labs/images/portfolio_management/ex2-step15.png)

16. Open Contact Details Tab and add your user as a Reservation Coordinator. Then click on **Create Draft -> Save -> Activate**. 

17. The hierarchy for the demo piece has been successfully created.

## Exercise 3: Creating an Asset in Real Estate & Facilities

1. Login to Real Estate and Facilities application with your id:
* Username- xxLastName
* Password- xxxxxxxxx

2. Click on the hamburger menu and open **Building Equipment** under Portfolio module.

![Create Draft](/labs/images/portfolio_management/ex3-step2.png)

3. Click on **Add** to create a new asset. 
![Add](/labs/images/portfolio_management/ex3-step3.png)

4. Fill all the general details as per the screenshot for the **Asset: Mechanical Equipment Hydronic Fin-Tube Radiator** installed on the first floor of Charlotte Watson center and click on **Create Draft -> Save -> Activate**.
* ID- XX-**RAD-01**(Replace XX with your initials)
* Name- XX **Mechanical Equipment Hydronic Fin-Tube Radiator**
![General details](/labs/images/portfolio_management/ex3-step4.png)

**Note**: Specifications are detailed attributes or characteristics that describe an asset.
They provide important information such as size, capacity, material, or performance details, depending on the type of asset. These details help in managing maintenance, compliance, and overall asset performance. 

It is mandatory to have a Specification Name created before Asset Creation in MREF.

5. Once Asset gets activated it will start reflecting in the List View
assigned to the building -> Floor -> Space.
![List view](/labs/images/portfolio_management/ex3-step5.png)

 
**End of lab**

References: https://www.ibm.com/docs/en/SSFCZ3_11.6/pdf/pdf_tri_portfolio_mng.pdf