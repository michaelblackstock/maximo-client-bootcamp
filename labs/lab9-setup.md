[Home](../README.md) | [Next](lab9-01-portfolio-management.md)

# Lab 9: MREF Overview and Setup

This lab introduces the Maximo Real Estate and Facilities (MREF) module and explains the steps you must take before running the demo. MREF extends the Maximo Application Suite by unifying disparate real estate tools under a single configurable platform. Because MREF is role‑based, each persona sees a tailored interface. Before beginning the hands‑on work, complete the following preparations:

1. **Watch the** [**demo**](https://www.youtube.com/watch?feature=shared&%3Bt=882&v=teCzcDjxb1g) using the provided link so that you understand the high‑level flow.
2. **Has an MREF environment been provisioned?**
   - Yes, **Request access** to the MREF environment and wait for an email with the URL and credentials. If the page does not load, refresh the browser.
   - If not, **Follow the** [**Getting Started Guide**](https://github.ibm.com/michael-blackstock/maximo-client-bootcamp-instructors/blob/main/environment-setup/mas-mref-install-guide.md) to reserve an environment correctly.
3. **Obtain credentials** for four demo users: `pprogram`, `pplanner`, `lleases`, and `ssystem`. All users have the password **Facilities2025!**
4. **Verify bookmarks**: ensure that `pplanner` login has _"Building: Charlotte Watson Center"_ listed under _My Bookmarks_ and that the `lleases` user can access the bookmark _"Real Estate Lease: 1003554‑0‑GASB – Initial recognition"_.

## Finding Available Users

To find all possible users who can work through the FastStart labs, navigate to **Hamburger menu → Security → Security Groups** and search for **DEFLTREG**. All users in the DEFLTREG and EVERYONE security groups are configured to work through the labs. By default, there are 43 users available in this security group.

## Creating Additional Users (Optional)

If you need to create additional users:

1. **Login as MAS ADMIN** using credentials found in OpenShift under the **mas-masdemo-core** project: **Workloads → Secrets → masdemo-credentials-superuser**
2. Navigate to **Hamburger menu → Security → Users**
3. Click to create a new user and provide:
   - **Name**: Full name of the user
   - **User ID**: Make it the same as the user name
   - **Primary Email**: User's email address
   - **Password**: Set to **Facilities2025!**
4. **Save** the user record
5. **Add the user to security groups**:
   - Navigate to **Hamburger menu → Security → Security Groups**
   - For both **DEFLTREG** and **EVERYONE**:
     - Click into the security group
     - Navigate to the **Users** section
     - Click the **Add Users** button
     - Find the user you just created and add them
     - Save your changes

**Note**: All users created for the FastStart labs must use the password **Facilities2025!** for consistency.

---

MREF centralizes real estate data so you can see lease contracts, space data, maintenance information and capital projects from a single record. You will explore this unified view as you progress through the persona‑specific labs.
