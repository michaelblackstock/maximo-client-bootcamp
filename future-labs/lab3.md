[< Previous Module](./../modules/21-maximo-mobile.md) | [Home](../README.md) | [Next >](./lab4-mvi.md)

# Lab 3: Maximo Mobile

## Objective
In this lab, you will learn how to set up and use Maximo Mobile. You will connect the mobile app to your Maximo instance and explore its key features.

## Instructions
Follow the instructions in the [Maximo Mobile module](../modules/20-maximo-mobile.md) to complete this lab.

## Steps
1.  Install the Maximo Mobile app on your device.
2.  Connect the app to your Maximo environment.
3.  Explore the app's features, such as work order management and asset tracking.
4.  (Optional) Try deploying a simple customization to the mobile app.

---

# IBM Maximo Mobile Development Setup Guide

This guide explains how to set up your environment for IBM Maximo Mobile application development using **Podman**.

---

## ✅ 1. Obtain IBM Entitlement API Key

You need an IBM Entitlement API key to pull container images from IBM's container registry.

1. Navigate to the **[IBM Container Software Library](https://myibm.ibm.com/products-services/containerlibrary)**.
2. Sign in with your **IBMid** and password.
3. Generate or copy your **Entitlement API Key**.

---

## ✅ 2. Authenticate with IBM Container Registry

Use **Podman** to log in to IBM's container registry:

```bash
podman login cp.icr.io --username cp --password <YOUR_IBM_ENTITLEMENT_KEY>
```

---

## ✅ 3. Pull Maximo Mobile Tools Image

Download the IBM Maximo Mobile development tools container image:

```bash
podman pull cp.icr.io/cp/manage/maf-tools:8.11.10
```

**Optional:** For specific architecture (e.g., Mac M1/M2 or ARM systems):

```bash
podman pull --arch amd64 cp.icr.io/cp/manage/maf-tools:8.11.10
```

---

## ✅ 4. Create a Workspace Directory

Create a local directory to store your development files:

```bash
mkdir ~/MAFWorkspace
```

---

## ✅ 5. Run the Maximo Mobile Tools Container

Start the container and expose necessary ports:

```bash
podman run -it --privileged   -p 3001:3001   -p 3006:3006   -v ~/MAFWorkspace:/graphite/.workspace   cp.icr.io/cp/manage/maf-tools:8.11.10
```

---

### **What this does**
- **`-p 3001:3001 -p 3006:3006`** → Exposes ports for development.
- **`-v ~/MAFWorkspace:/graphite/.workspace`** → Mounts your local workspace inside the container.

---

## ✅ 6. Next Steps

Once the container is running:
- Edit XML and JavaScript files in your mounted workspace (`~/MAFWorkspace`).
- Build and deploy your customized Maximo Mobile application.
- Access the development UI through the exposed ports in your browser.

---

### ✅ Additional Resources
- [IBM Maximo Mobile Documentation](https://www.ibm.com/docs/en/maximo-mobile)
- [IBM Container Software Library](https://myibm.ibm.com/products-services/containerlibrary)

---