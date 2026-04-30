[Previous](lab9-01-portfolio-management.md) | [Next](lab9-03-lease-management.md) | [Home](../README.md)

# Space Management
This lab exercise focuses on using the MREF application to manage various aspects of facility operations, including planning, space utilization, move coordination, and resource reservations.

**Strategic Facility Planning**: MREF Strategic Facility Planning is used to analyze business requirements, simplify complex planning processes, and develop actionable strategies for effective facility management.

**Dynamic Space Planning**: The MREF Dynamic Space Planning (DSP) module enables the creation and evaluation of spatial scenarios to optimize space utilization. Activities include analysing floors for social distancing, updating space classifications, reallocating departments and personnel, and defining reservable or dedicated areas. Scenario outputs can automatically update active space records to reflect the planned changes.

**Managing Drawings**: The Drawing Manager application provides a centralized platform within MREF for managing uploaded drawings. It supports functions such as searching, viewing, modifying, exporting to PDF, downloading, and deleting drawings, ensuring efficient drawing management and version control.

**Managing Spaces and Moves**: The MREF Space Management feature supports the creation and maintenance of space plans, tracking of utilization data, and management of people, assets, and property information. The Move Management feature facilitates the submission and processing of move requests, development of move designs, and organization of move projects. Integration with MREF CAD Integrator/Publisher allows direct synchronization between CAD applications and the MREF platform for streamlined updates.

**Managing Reservations and Reservable Resources**: The MREF Workplace Reservation Manager application enables the scheduling and management of shared rooms, workspaces, equipment, and vehicles. It supports reservation requests, processing of event and workspace bookings, and coordination of related services such as room setup, catering, and equipment delivery. Integration with Microsoft Exchange and Outlook
provides additional flexibility for managing room and resource reservations.

## Dynamic Space Planning
The Dynamic Space Planning (DSP) app is used to create visual scenarios for analysing and managing floor layouts. It allows scenarios to be designed for social distancing, space classification updates, and organization or personnel rearrangements. Spaces can be marked as reservable or dedicated within these scenarios. The scenario data can
then be applied to automatically update active space details to match the planned layout.

### Exercise 1. Reviewing the existing floor plan layout
In this exercise we will learn how to view, ﬁlter, and analyse ﬂoor plan data using the
Dynamic Space Planning features.
1. Login to Maximo Application Suite and Launch Real Estate and Facilities as space
planner.
* Username: **pplanner**
* Password: **xxxxxxxx**

2. Go to Portfolio-> Locations.

![Locations](/labs/images/space_management/spacemanage-004-011.png)

3. Expand **Offices –> North America -> Open Charlotte Watson Center** Building.

\* Note: This is different from the Charlotte Watson Center created in the portfolio manager lab, this is a building pre-populated with demo data.

![Expand](/labs/images/space_management/open-cwc.png)

4. Navigate to **Area Measurements** tab and open the ﬂoor record.
![Area Measurements](/labs/images/space_management/spacemanage-005-014.png)

5. In the floor record open **Dynamic Space Planning** tab.
![Dynamic planning](/labs/images/space_management/spacemanage-005-015.png)

6. To view specific types of space information on the floor plan, use the Legend options-
On the **left side** of the horizontal toolbar, select the **Legend** icon or arrow to open the **Legend sidebar**. The sidebar includes the following options:

a) **Show By** – Displays spaces based on criteria such as Charge to Org,
Occupancy Org by People, Occupancy by People, Space Class, or Work
Points.

b) **Filter By** – Filters spaces using options like Charge to Org, Occupancy Org, Occupancy by People, Reservable Flag, Work Points, or Available Spaces.
![Floor plan](/labs/images/space_management/spacemanage-006-017.png)

7. To view workstation assignments for specific people on the floor plan:

a) On the **right side** of the horizontal toolbar, select the **People** icon or arrow to open the **People sidebar**.

b) On the toolbar, use the **Show/Hide People** icon to display or hide people
on the floor plan.

c) In the **People sidebar**, choose the **All** tab to view all people or the **Removed** tab to view people who were removed from the plan.
![Workstation assignments](/labs/images/space_management/spacemanage-006-018.png)



8. To view additional space details on the floor plan:

a) On the **horizontal toolbar**, select the **Layers** icon to turn on or off specific layers from the source CAD drawing.

b) On the **horizontal toolbar**, select the **Open Record** icon to enable space
selection.

c) Click on a space in the floor plan to open its corresponding record and view detailed information.

![Image for Page 7](/labs/images/space_management/spacemanage-007-020.png)

## Scenario Planning
Scenario Planning is used to create and analyse different space layout options before making real changes. It allows planners to test “what-if” situations, such as rearranging people, updating space types, or adjusting organizational allocations. These scenarios help visualize the impact of changes on space utilization without affecting live data.
Once a scenario is finalized, it can be applied to update the active floor plan automatically, supporting better planning and decision-making for workplace management.

### Exercise 2. Creating a Scenario Plan for the floor
1. Login to Maximo Application Suite and Launch Real Estate and Facilities as space
planner.
* Username: **pplanner**
* Password: **xxxxxxxx**

2. Go to Portfolio-> Locations.

![Locations](/labs/images/space_management/spacemanage-004-011.png)

3. Expand **Offices –> North America -> Open Charlotte Watson Center** Building.

\* Note: This is different from the Charlotte Watson Center created in the portfolio manager lab, this is a building pre-populated with demo data.

![Expand](/labs/images/space_management/spacemanage-004-012.png)

4. Open the ﬂoor record in the CWC building.
![Floor record](/labs/images/space_management/spacemanage-008-026.png)

5. In the ﬂoor record, select the **Dynamic Space Planning** tab.
![Dynamic space](/labs/images/space_management/spacemanage-008-027.png)

6. To create a new scenario for the ﬂoor plan, you can take the following steps:

a) On the secondary toolbar, select the **Create Scenario** icon at bottom.
![Create scenario](/labs/images/space_management/spacemanage-008-028.png)
b) In the dialog box, enter the **Scenario Name**, then click **Create**.
![Create](/labs/images/space_management/spacemanage-009-030.png)
c) In the lower-left area of the tab, select the name of the new scenario.
![Name](/labs/images/space_management/spacemanage-009-031.png)

7. To move people from one workstation to another workstation, you can take the following steps:

a) On the right side of the horizontal toolbar, select the **People** icon or arrow to expand the People sidebar.
![People](/labs/images/space_management/spacemanage-009-032.png)

b) Click and drag each person from one workstation to another workstation.
![Workstation](/labs/images/space_management/spacemanage-010-034.png)

8. To change the available (workpoint) and unavailable (non-workpoint) spaces that
are shown, you can take the following steps:

a) On the left side of the horizontal toolbar, select the Legend icon or arrow to
expand the Legend sidebar.

b) Select **Filter By ->Available Spaces** and choose **Show All Available**, or **Not Available**.
![Filter](/labs/images/space_management/spacemanage-010-035.png)

9. To remove people from workstations, you can take the following steps:

a) On the horizontal toolbar, select the **Enable drag selection** icon to enable it.
![Enable drag selection](/labs/images/space_management/spacemanage-010-036.png)

b) Click and drag your cursor over a rectangular area of workstations with people.
**Tip:** To clear the selected spaces, click the Clear Selection icon.

c) On the horizontal toolbar, select the Edit icon, then Remove People.
![Image for Page 11](/labs/images/space_management/spacemanage-011-039.png)

d) In the dialog box, select all people or select one or more organizations, then
click Remove.

10. To convert workstations into reservable spaces, you can take the following steps:

a) On the horizontal toolbar, select the **Enable drag selection** icon to enable it.

b) Click and drag your cursor over a rectangular area of workstations without people.

**Hint:** To clear the selected spaces, click the **Clear Selection** icon.

c) On the horizontal toolbar, select the **Edit** icon, then **Edit Reservable**.

d) In the dialog box, click **Update**.

**Hint:** To conﬁrm, use the left-side **Filter By** to ﬁlter spaces by the **Reservable Flag**.
![Update reservable status](/labs/images/space_management/spacemanage-011-040.png)

11. To update the space classiﬁcations of spaces, you can take the following steps:

a) On the horizontal toolbar, select the **Enable drag selection** icon to enable it.

b) Click and drag your cursor over a rectangular area of spaces to select them.

c)On the horizontal toolbar, select the **Edit** icon, then **Edit Space Details**.

d)In the dialog box, enter the new details, then click **Update**.

**Hint:** To conﬁrm, use the left-side **Show By** to show spaces by the **Space Class** classiﬁcation.

**Hint:** As an alternative, when the People sidebar is collapsed, you can select the **Space Classes** icon to display a palette or list of space classes. Drag the colored dot of the space class to your selected spaces.
![Space classes](/labs/images/space_management/spacemanage-012-044.png)

12. To replace the **Charge To** organization allocation of spaces, you can take the following steps:

a) On the horizontal toolbar, select the **Enable drag selection** icon to enable it.

b) Click and drag your cursor over a rectangular area of spaces to select them.

c)On the horizontal toolbar, select the **Edit** icon, then **Edit Charge To Details**.

d)In the dialog box, select the new organization, then click **Replace**.

**Hint:** To conﬁrm, use the left-side **Show By** to show spaces by the **Charge to Org** organization.

**Hint:** As an alternative, when the People sidebar is collapsed, you can select the **Charge to Org** icon to display a palette or list of chargeback organizations. Drag the colored dot of the chargeback organization to your selected spaces.
![Charge to org](/labs/images/space_management/spacemanage-013-050.png)

13. To add another **Charge To** organization allocation to spaces, you can take the following steps:

a) Again, select the **Edit** icon, then **Edit Charge To Details**. 

b) In the dialog box, select the new organization, then click **Add**.

**Hint:** To conﬁrm, use the left-side **Show By** to show spaces by the **Charge to Org** organization.

**Hint:** As an alternative, when the People sidebar is collapsed, you can select the **Charge to Org** icon to display a palette or list of chargeback organizations. While you press the **Shift** key, drag the colored dot of the chargeback organization to your selected spaces.

14. To remove the **Charge To** organization allocation from spaces, you can take the
following steps:

a) Again, select the **Edit** icon, then **Edit Charge To Details**.

b) In the dialog box, select the organization to remove, then click **Clear**.

**Hint:** To conﬁrm, use the left-side **Show By** to show spaces by the **Charge to Org** organization.

15. Click **Save Draft**.

16. When you're ready, click **Stage Changes** to create a staged Floor Scenario record with a summary of the scenario changes.
![Staged floor](/labs/images/space_management/spacemanage_14_Im26.png)

**End of lab**

References: https://www.ibm.com/docs/en/tririga/11.6.0?topic=moves-dynamic-space-planning