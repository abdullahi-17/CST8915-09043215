# CST8915 Lab 3 – Algonquin Pet Store Part 3

**Student Name**: Abdullahi Omer
**Student ID**: 09043215
**Course**: CST8915 Full-stack Cloud-native Development
**Semester**: Fall 2026

---

## Demo Video

🎥 [Watch Demo Video](https://youtu.be/xK9cr06UFc4)

---

## Service Repositories

[Product Service Repository](https://github.com/abdullahi-17/product-service.git)

[Order Service Repository](https://github.com/abdullahi-17/order-service.git)

[Store Front Repository](https://github.com/abdullahi-17/store-front.git)

---

## Reflection Questions

### 1. What challenges did you encounter when configuring environment variables in the GitHub Actions workflow?

One challenge I had was making sure the environment variables had the correct URLs and formatting. For example, the frontend needed the base URLs for the product and order services without `/products` or `/orders` at the end because those paths were already added in the Vue code. I also had to restart the application after changing the variables so the new values would be loaded.

### 2. How does deploying microservices on Azure Web App Service differ from running them locally?

Running the services locally was simpler because I could use localhost and start each service directly from the terminal. On Azure App Service, I had to configure things like environment variables, startup commands, ports, and GitHub deployment. I also had to make sure the deployed services could communicate with each other over their public URLs instead of localhost.

### 3. Why is it important to use environment variables for configurations in a cloud environment?

Environment variables keep configuration values separate from the application code. This makes it easier to use different settings when moving between local development and Azure without changing the code each time. It is also useful for values such as service URLs and connection strings because they can be updated directly in the cloud environment instead of being hard-coded into the application.

## Setup Notes

The original lab required the `store-front` to be deployed using Azure Static Web Apps. My Azure for Students subscription had a policy restriction that prevented me from creating a Static Web App in the available regions. Based on the alternative provided by the professor, I deployed the Vue `store-front` on an Azure VM instead.

The `product-service` and `order-service` were deployed using Azure App Service. RabbitMQ was hosted on a separate Azure VM. The store front communicates with both App Services, and orders submitted through the application are sent to the RabbitMQ `order_queue`.
