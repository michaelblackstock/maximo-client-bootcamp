[Previous](lab9-03-lease-management.md) | [Home](../README.md)

# Capital Projects and Planning
## Project Setup
It explains how to prepare MREF for creating and managing capital projects efficiently. This setup process involves defining project cost codes, approval workflows, budget templates, and project templates. By doing this, organizations ensure that every new project follows consistent standards and financial structures. Essentially, it’s about
building the foundation in MREF so that future capital projects can be created, tracked, and approved smoothly.

## Exercise 1. Capital Project Template Creation
In this exercise we will see how a project template can be created and how it can be applied later in the project directly.

1. Login to Real Estate and Facilities application with your id:

* Username- xxLastName - Where xx represents your initals and LastName is your last name
* Password- xxxxxxxxxx

![Login](/labs/images/capital_projects/ex1-step2.png)

3. From the Navigation menu, launch the **Real Estate and Facilities** application.

![REF](/labs/images/capital_projects/ex1-step3.png)

4. Go to **Projects -> Project Set Up -> Project Templates -> Capital Project**.

![Capital project](/labs/images/capital_projects/ex1-step4.png)

5. Click on **Add** to create a new template.
![Add](/labs/images/capital_projects/ex1-step5.png)

6. Fill in all the general details to create the Charlotte Watson Center First Floor Construction template (assumed), as shown in the attached screenshot.
* ID-**XX-CWC-1F-C** (Replace XX with your initials)
* Name-**Charlotte Watson Center First Floor Construction**
![General details](/labs/images/capital_projects/ex1-step6.png)

7. Navigate to **Schedule** Tab and fill the summary and click on **Create Template**.
![General details](/labs/images/capital_projects/ex1-step7.png)

8. Click on **Add** under the Project Tasks section. A list of available Task Templates will be displayed. Let’s create each task template and observe how it reflects in the Project Gantt Schedule. Click on a Schedule Task Template to begin.
![Add](/labs/images/capital_projects/ex1-step8.png)

9. Enter the Task **Name** and **Create Template -> Save & Close**.
![Create template](/labs/images/capital_projects/ex1-step9.png)

10. Similarly create **Inspection Task Template** for Structural Inspection.
![Inspection Task Template](/labs/images/capital_projects/ex1-step10.png)

11. Similarly create a **Punchlist Task Template** for broken light fix.
![Punchlist task](/labs/images/capital_projects/ex1-step11.png)

12. Similarly create a **Submittal Task Template** for electrical drawings.
![Submittal task](/labs/images/capital_projects/ex1-step12.png)

13. Similarly create **Work Task Template** for HVAC-Corrective Maintenance.
![Work task](/labs/images/capital_projects/ex1-step13.png)

14. Similarly create a **Contract Review Template**.
![Contract Review](/labs/images/capital_projects/ex1-step14.png)

15. Finally Create a **Schedule Task Template** reflecting the project completion.
![Project Handover](/labs/images/capital_projects/ex1-step15.png)

16. Once all tasks have been created, navigate to the Gantt schedule and tasks list to review and confirm that all tasks are displayed as below.
![Task display](/labs/images/capital_projects/ex1-step16.png)

17. **Save** the template.

## Funding Source
**Funding sources** are financial resources used to support programs and projects, such as grants, bonds, government awards, donations, or internal funds. Each funding source record includes details like the funding organization, dates, and allocation amounts. Funding must often be identified and approved before a project begins, especially in regulated or non-profit environments. These sources ensure projects are properly financed and used as intended. If funding is in a different currency, it is converted to match the project's currency upon approval.

## Exercise 2: Funding Source Creation
1. Login to Real Estate and Facilities application with your id:

* Username- xxLastName - Where xx represents your initals and LastName is your last name
* Password- xxxxxxxxxx

2. Go to **Projects -> Funding Sources**.

![Funding sources](/labs/images/capital_projects/ex2-step2.png)

3. Expand **Related Links - Funding Sources -> Create a Funding Source**.
![Create funding source](/labs/images/capital_projects/ex2-step3.png)

4. Fill the general details required for creating a funding source as per the screenshot and click on **Create Draft**.
* ID-**XX-CWC-FS** (Replace XX with your initials)
* Name-**Funding Source for CWC**
![General details](/labs/images/capital_projects/ex2-step4-1.png)
After draft, fill **Funding Pending Approval and Click on Save -> Update Allocations -> Issue**.
![Advanced info](/labs/images/capital_projects/ex2-step4-2.png)

5. Reopen the funding source and verify **Approved Funding** as below.
![Approved funding](/labs/images/capital_projects/ex2-step5.png)

## Program
A **program** is used to manage and coordinate multiple related projects under a common objective. It provides centralized planning, oversight, and control. Programs allow for the consolidation of finances, where all project budgets roll up to the program level. They also maintain a master schedule to track key milestones across projects. This ensures alignment between projects and helps manage dependencies. Overall, programs enhance visibility and strategic management.

## Exercise 3: Program Creation
1. Login to Real Estate and Facilities application with your id:

* Username- xxLastName - Where xx represents your initals and LastName is your last name
* Password- xxxxxxxxxx

2. Select **Projects** and go to **Programs**.

![Programs](/labs/images/capital_projects/ex3-step2.png)

3. Go to the **Related Links - Program > Programs and Funding Sources > Create a Program**.
![Create a program](/labs/images/capital_projects/ex3-step3.png)

4. Fill all the general details for the program and click **Create Draft**.
* ID-**XX-CWC-P** (Replace XX with your initials)
* Program Name-**Program for CWC Building**
![General details](/labs/images/capital_projects/ex3-step4.png)

5. If a warning appears prompting you to assign a Program Manager, navigate to the **Contacts** tab and add a person to fulfil this role. Follow the below sub-steps to add the program maanger.
![Contacts](/labs/images/capital_projects/ex3-step5-1.png)
a. Click on **Program Manager**.
![Program manager](/labs/images/capital_projects/ex3-step5-2.png)
b. Click on **Find**.
![Find](/labs/images/capital_projects/ex3-step5-3.png)
c. Search for **Patti** and select **Patti Program** from the list and click on **OK**.
![Patti](/labs/images/capital_projects/ex3-step5-4.png)
d. The Program Manager gets added. Click on **Save & Close**.
![Save](/labs/images/capital_projects/ex3-step5-5.png)
e. The Patti Program gets added to the Program. Click on **Create Draft** and then **Issue**.
![Create draft](/labs/images/capital_projects/ex3-step5-6.png)

6. Navigate to **Financials** Tab to add Funding Source by following these below sub-steps:

a. Select Funding Type as **Capital** and click on **Add Funding**.
![Add funding](/labs/images/capital_projects/ex3-step6-1.png)
b. Click on **Import Funding Sources**.
![Import funding](/labs/images/capital_projects/ex3-step6-2.png)
c. Search for your funding source created in the last exercise (XX-CWC-FS). Click on the checkbox an click on **OK**.
![Funding source](/labs/images/capital_projects/ex3-step6-3.png)
d.  Allocate the required money to the program from the funding source as required per year under **Commit to Program -> Click on all checkboxes -> Continue**.
![Allocate money](/labs/images/capital_projects/ex3-step6-4.png)

7. The Financials tab will look like below once funding gets added to the program.
![Financials tab](/labs/images/capital_projects/ex3-step7.png)

8. Click on **Issue**.

## Funding Request
A **Funding Request** is a formal request object used to initiate the process of securing financial resources needed to create one or more programs, capital projects, or facilities projects. It serves as the starting point for project funding by outlining the required budget and justification for the request. 

## Exercise 4: Creating a Funding Request
1. Login to Real Estate and Facilities application with your id:

* Username- xxLastName - Where xx represents your initals and LastName is your last name
* Password- xxxxxxxxxx

2. Select **Projects -> Funding Requests**.

![Funding requests](/labs/images/capital_projects/ex4-step2.png)

3. Go to the **Related Links - Program > Programs and Funding Sources > Create a Funding Request**.
![Create](/labs/images/capital_projects/ex4-step3.png)

4. Fill the general details for the funding request and click **Create Draft** and then **Issue**.
* Name-**XX_Funding Request for CWC First Floor Construction**
* Select **Charlotte Watson Center Building** details
* Attach Program as created in the last exercise
* Proposed Start Date > Program Start Date
* Proposed End Date < Program End Date
* Manual Cost
![General details](/labs/images/capital_projects/ex4-step4.png)

5. Navigate to **Funding** tab and Request Funding for the Project by clicking on **Add Funding** and Import the Funding Source and click **Continue**.

a. Select Funding Type – Capital and click on Add Funding.
![Funding type](/labs/images/capital_projects/ex4-step5-1.png)
b. Click on **Importing Funding Sources**.
![Importing funding sources](/labs/images/capital_projects/ex4-step5-2.png)
c. Fill the Requested Fund -> Select the checkboxes and click on **Continue**.
![Requested fund](/labs/images/capital_projects/ex4-step5-3.png)

6. **Submit** the Funding Request.

7. Open the Funding Request again and check the status.
![Status](/labs/images/capital_projects/ex4-step7.png)

8. The status shows **Review in Progress** which means it needs further approval.
![Status](/labs/images/capital_projects/ex4-step8.png)

9. To see the approver name go to **Notifications** Tab
![Notifications](/labs/images/capital_projects/ex4-step9.png)

**Note**: The Patti Program name appears in the funding request because we assigned Patti as the Program Manager when creating the program in the previous exercise.

Since the funding request is being submitted under the same program, it will require further approval from the Program Manager before it can be converted into a project.

## Approvals
After the submission of programs and funding requests, the Program Manager receives a notification on their dashboard. They are responsible for reviewing the submitted items and taking the necessary actions, such as approving, querying, or rejecting them.

## Exercise 5: Approve the Funding Request

1. Login to Maximo Application Suite with Program Manager credentials and Launch **Real Estate and Facilities**.

• Username-**pprogram**
• Password-**xxxxxxxxx**

**Note**: If the user doesn't exist, then create this user with id: **pprogram** and name: **Patti Program** following the steps of exercise 1 Portfolio Management

2. Go to the Program Manager dashboard and check the Reminders section to view the pending approval requests for both the program and the funding request.
![PM dashboard](/labs/images/capital_projects/ex5-step2.png)

3. Click on **Action Items** to view the request details along with any associated notifications.
![Action Items](/labs/images/capital_projects/ex5-step3.png)

4. Based on the review the program manager can **Approve, Escalate, Reassign, Request Clarification or Return** the request.
![Actions](/labs/images/capital_projects/ex5-step4.png)

5. Click on **Approve -> Enter the Comments -> Continue**.
![Approve](/labs/images/capital_projects/ex5-step5.png)

6. Once the request is approved, **refresh** the Action Items. You will no longer see any pending approval requests related to this exercise.
![Refresh](/labs/images/capital_projects/ex5-step6.png)

7. Logout and login with your credentials. (Ensure to clear browser history & cache)
* Username- **xxLastName**
* Password- **xxxxxxxx**

8. You will see 1 action items under Reminders
![Action items](/labs/images/capital_projects/ex5-step8.png)

9. Click on **Action Items** to see the action required for the funding request. One response is needed from the user for the funding request. Click on **Please Respond**.
![Please Respond](/labs/images/capital_projects/ex5-step9.png)

10. Review the request and click on **Respond**.
![Respond](/labs/images/capital_projects/ex5-step10.png)

11. Enter the response in comments and click on **Send**.
![Send](/labs/images/capital_projects/ex5-step11.png)

12. Naviagate the **Projects -> Programs**.

![Programs](/labs/images/capital_projects/ex5-step12.png)

13. Expand **Related Links-Programs -> Programs and Funding Sources-> View Programs**.

![View programs](/labs/images/capital_projects/ex5-step13.png)

14. Search your Program (XX-CWC-P)

![Search](/labs/images/capital_projects/ex5-step14.png)

15. You will see the funding request gets added to the program. Now we will create a capital project for this request.
![Funding request](/labs/images/capital_projects/ex5-step15.png)

## Capital Project
Creating a capital project involves setting up and managing key elements of a project such as its scope, schedule, budget, tasks, and assigned roles. This process helps organize all aspects necessary for successful project execution. For instance, you can establish a project team and assign specific responsibilities to each member. Additionally, you can control security access to ensure that team members have the appropriate permissions to view or edit project information. Overall, creating a capital project provides a structured framework for effective planning and management.

## Exercise 6: Creating a Capital Project
1. Login to Real Estate and Facilities application with your id:

* Username- xxLastName - Where xx represents your initals and LastName is your last name
* Password- xxxxxxxxxx

2. Select **Projects -> Capital**

![Capital](/labs/images/capital_projects/ex6-step2.png)

3. Go to the **Related Links - Program > Projects > Create a Capital Project**.

![Capital project](/labs/images/capital_projects/ex6-step3.png)

4. Fill the general details of the project related to the funding request for CWC first floor construction.
* ID: **XX-CWC-1F-C-CP** (Replace XX with your initials)
* Name: **Capital Project for Charlotte Watson Center First Floor Construction**
![General details](/labs/images/capital_projects/ex6-step4.png)

5. Navigate to **Schedule** tab and assign the start and end dates for the project and click on Create Draft.
![Schedule](/labs/images/capital_projects/ex6-step5.png)

6. Now we will add tasks to the project. We will utilize the project template which we created in exercise 1. Click on **More -> Apply Template**.
![Template](/labs/images/capital_projects/ex6-step6.png)

7. Search the template you created. Select it and click on **Continue**.
![Continue](/labs/images/capital_projects/ex6-step7.png)

8. All the tasks get imported and start reflecting in the project Gantt and project tasks list. **Rearrange** the task sequence and adjust the planned start date and planned end date accordingly from the Gantt schedule.

9. To create dependencies between the tasks, resource assignment, progress, budget, etc. **Open** a task under the Project Tasks list.
![Project tasks](/labs/images/capital_projects/ex6-step9.png)

10. Assign the resource from the person list (assign to any person/technician), enter the planned cost, actual working days. Click on **Save -> Baseline -> Activate**.
![Project tasks](/labs/images/capital_projects/ex6-step10.png)

11. Open the next task **Structural Inspection**, and fill in the details as described in the previous step. Click **Save**. 

12. Go to the **Dependencies** tab, click on **Find Tasks**, select the previous task (Project Initiation), and click **OK**. Select Dependency Relationship as **Finish-to-Start** and click on **Save**.
![Project tasks](/labs/images/capital_projects/ex6-step12.png)

13. Repeat the same steps for the remaining tasks. Once all tasks are completed with the required details, the Gantt schedule will appear as shown below.
![Gantt Schedule](/labs/images/capital_projects/ex6-step13.png)

14. **Save** the Project and Go to **Budget** Tab and Allocate the Funding by clicking on Add Funding Allocations -> Import Funding Sources -> Select the funding source you created -> Allocating the yearly amount. (We have already done this in previous exercises)
![Allocate amount](/labs/images/capital_projects/ex6-step14.png)

**Note**: You might not able to view your funding source that you created in the list because we have already used all the funds and there is no available funds to allocate to this project. In such case select any funding source from the list or create a new funding source.

15. Now add the Project Fund by clicking on **Add**.
![Add](/labs/images/capital_projects/ex6-step15.png)

16. Click on **Project Original Budget** from the list and fill the General Details and add Items by clicking on **Find** based on the Cost Codes.
• ID: **XX-CWC-OB** (Replace XX with your initials)
• Name: **CWC Original Budget for first floor Construction**
![General details](/labs/images/capital_projects/ex6-step16.png)

17. Similarly add Project Budget Change, Project Budget Forecast and Project Budget Transfer and save the project.

18. (**Optional**) Navigate to **Procurements tab -> Contracts and Purchase Orders -> Add -> Standard Contract**.
![General details](/labs/images/capital_projects/ex6-step18.png)

19. (**Optional**) Similarly add values and complete the billing.
![General details](/labs/images/capital_projects/ex6-step19.png)

20. Once budgeting, forecasting, procurements, and billing are completed, the Budget Summary will be populated.
![Budget Summary](/labs/images/capital_projects/ex6-step20.png)

21. Click on **Calculate -> Activate** the Project.

**End of lab**

References: https://www.ibm.com/docs/en/SSFCZ3_11.6/pdf/pdf_tri_pgm_proj_mng.pdf